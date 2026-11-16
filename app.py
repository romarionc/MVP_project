from flask import Flask, render_template, request, redirect, url_for
from database import init_db
import sqlite3

app = Flask(__name__)

# Inicializa o banco de dados ao iniciar
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/entrega', methods=['POST'])
def entrega():
    subtotal = float(request.form.get('subtotal', 52.00))
    itens = request.form.get('itens', '1x Pizza Grande (Meio a Meio) + 1x Refri 1,5L')
    return render_template('entrega.html', subtotal=subtotal, itens=itens)

@app.route('/finalizar', methods=['POST'])
def finalizar():
    cliente = request.form.get('cliente', '').strip()
    endereco = request.form.get('endereco', '').strip()
    bairro = request.form.get('bairro', 'Centro')
    pagamento = request.form.get('pagamento', 'Dinheiro')
    itens = request.form.get('itens', '1x Pizza Grande + Bebida')
    
    # Define taxa conforme o bairro de Horizonte (RF02)
    taxas = {'Centro': 5.00, 'Planalto Horizonte': 6.00, 'Mangueiral': 7.00}
    taxa = taxas.get(bairro, 5.00)
    
    subtotal = float(request.form.get('subtotal', 52.00))
    total = subtotal + taxa

    # Tratamento seguro do campo troco (RNF02)
    troco_str = request.form.get('troco', '').strip()
    troco_para = float(troco_str) if troco_str else 0.0
    troco_devolver = max(0.0, troco_para - total) if pagamento == 'Dinheiro' and troco_para > 0 else 0.0

    # Gravação segura com Prepared Statement anti-SQLi (RF03 / RNF01)
    conn = sqlite3.connect('farinatto.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO pedidos (cliente, endereco, bairro, taxa_entrega, total, troco)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (cliente, endereco, bairro, taxa, total, troco_devolver))
    pedido_id = cursor.lastrowid
    
    # Busca resumo do turno (RF04)
    cursor.execute('SELECT COUNT(*), COALESCE(SUM(total), 0) FROM pedidos')
    qtd_pedidos, faturamento_total = cursor.fetchone()
    conn.commit()
    conn.close()

    return render_template(
        'resultado.html',
        pedido_id=pedido_id,
        cliente=cliente,
        endereco=endereco,
        bairro=bairro,
        pagamento=pagamento,
        itens=itens,
        taxa=taxa,
        total=total,
        troco_devolver=troco_devolver,
        qtd_pedidos=qtd_pedidos,
        faturamento_total=faturamento_total
    )

if __name__ == '__main__':
    app.run(debug=True)