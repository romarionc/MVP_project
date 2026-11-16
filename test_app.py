import unittest
from app import app
from database import init_db

class FarinattoMVPTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        init_db()

    def test_rota_inicial_carrega_cardapio(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Farinatto Pizzaria'.encode('utf-8'), response.data)

    def test_fluxo_entrega_subtotal(self):
        response = self.client.post('/entrega', data={'subtotal': '52.00', 'itens': '1x Pizza G'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('52.0'.encode('utf-8'), response.data)

    def test_finalizar_pedido_calculo_taxa_e_troco(self):
        response = self.client.post('/finalizar', data={
            'cliente': 'Cliente Teste Unitario',
            'endereco': 'Rua das Flores, 120',
            'bairro': 'Centro',
            'pagamento': 'Dinheiro',
            'subtotal': '52.00',
            'troco': '100.00',
            'itens': '1x Pizza G Meio a Meio'
        })
        self.assertEqual(response.status_code, 200)
        # Subtotal 52 + Taxa Centro 5 = 57.00 | Troco p/ 100 = 43.00
        self.assertIn('57.00'.encode('utf-8'), response.data)
        self.assertIn('43.00'.encode('utf-8'), response.data)

if __name__ == '__main__':
    unittest.main()