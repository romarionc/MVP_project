# 🍕 Farinatto Pizzaria — MVP (Minimum Viable Product)

Aplicação web desenvolvida como Trabalho Final de Projeto de Software, com o objetivo de otimizar o fluxo de atendimento de balcão e pedidos via WhatsApp da **Farinatto Pizzaria** (localizada em Horizonte, Ceará), eliminando cálculos manuais, erros de comanda e otimizando a produtividade da equipe em horário de pico.

---

## 🚀 Tecnologias e Arquitetura

O projeto adota uma arquitetura monolítica em camadas lógicas, priorizando simplicidade, desempenho e baixo custo de implantação:
* **Back-End / Controlador:** Python 3.12 com Flask 3.0+ (micro-framework leve para rotas HTTP, motor de templates Jinja2 e regras de negócio de cálculo de pedidos).
* **Banco de Dados:** SQLite (modalidade embarcada e local, arquivo único leve `farinatto.db`, com custo zero de infraestrutura e suporte a consultas parametrizadas).
* **Front-End:** HTML5, CSS3 (Tailwind CSS / responsivo) e JavaScript Vanilla (SPA leve, adaptada para computadores de balcão e smartphones básicos).
* **Segurança:** Diretrizes alinhadas ao OWASP Top 10 (proteção contra SQL Injection via Prepared Statements, anti-XSS e senhas seguras com hash `scrypt`).

---

## 📋 Funcionalidades Principais (Requisitos Funcionais)

* **RF01 — Catálogo e Cálculo de Produtos:** Seleção de pizzas inteiras, meio a meio (com regra de precificação de metades), calzones, bordas recheadas e bebidas, com cálculo instantâneo de subtotais.
* **RF02 — Logística de Entrega e Pagamento:** Inclusão de dados do cliente, cálculo automático da taxa de entrega por bairro em Horizonte (CE) e cálculo de troco para pagamentos em espécie.
* **RF03 — Persistência e Comanda Digital:** Gravação do pedido no banco de dados SQLite e geração de texto padronizado em um clique para envio rápido no WhatsApp e leitura limpa na cozinha.
* **RF04 — Histórico e Fechamento de Turno:** Consulta diária de atendimentos realizados e totalizadores financeiros do turno para fechamento de caixa.

---

## ♿ Acessibilidade e ODS

* **Conformidade WCAG 2.1 AA (RNF04):** Áreas de toque mínimas de 44x44px, contraste superior a 4.5:1 (e 7:1 na comanda da cozinha), rótulos `<label>` persistentes, foco visível e alertas multissensoriais (símbolo + cor + texto).
* **Alinhamento ao ODS 8 (Trabalho Decente e Crescimento Econômico):** Modernização tecnológica de microempreendimentos locais (Meta 8.2 e 8.3), reduzindo a carga cognitiva e o estresse laboral dos trabalhadores.

---

## 🛠️ Como Executar o Projeto Localmente

1. **Pré-requisitos:**
   * Python 3.12+ instalado na máquina.

2. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/romarionc/MVP_farinatto.git](https://github.com/romarionc/MVP_farinatto.git)
   cd MVP_farinatto