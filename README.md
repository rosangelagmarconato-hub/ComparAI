# COMPARAI - Comparador Inteligente de Crédito

## Descrição do Projeto

O **COMPARAI** é uma ferramenta em Python que permite ao usuário simular financiamentos de veículos e imóveis, considerando restrições de financiamento e renda, e oferecendo um resumo detalhado das melhores opções de crédito disponíveis em bancos selecionados. O sistema apresenta:

* Limite de financiamento: máximo 80% do valor do bem.
* Limite da parcela: máximo 30% do rendimento mensal.
* Cálculo detalhado de parcelas, juros, seguro, IOF, TAC e CET.
* Exibição de tabela organizada por prazos (12, 24 e 36 meses).
* Gráfico comparativo de parcelas e juros com valores destacados.
* Interação com o usuário para encaminhar contato ao gerente da instituição.

---

## Funcionalidades Principais

1. **Entrada de dados do usuário**:

   * Nome e telefone.
   * Modalidade de financiamento: Veículo, Imóvel (mercado), Imóvel (regulado).
   * Mês e ano de referência.
   * Valor do bem, valor solicitado para financiamento e rendimento mensal.

2. **Validação de limites**:

   * Se o valor financiado ultrapassar 80% do bem, ajusta automaticamente para o máximo permitido.
   * Calcula o limite de parcela com base em 30% do rendimento mensal e filtra opções que ultrapassem esse valor.

3. **Simulação de financiamentos**:

   * Busca taxas de juros do Banco Central para os bancos selecionados.
   * Calcula parcela mensal, total pago, juros, seguro, IOF, TAC e CET.
   * Agrupa os resultados por prazo (12, 24 e 36 meses).

4. **Apresentação dos resultados**:

   * Exibe tabela detalhada com as opções válidas.
   * Mostra gráfico comparativo de parcelas e juros, com valores destacados sobre as barras.
   * Pergunta ao usuário se deseja entrar em contato com o gerente da instituição escolhida.

---

## Tecnologias Utilizadas

* **Python 3.x**
* Bibliotecas:

  * `requests` → para consumir API do Banco Central.
  * `pandas` → para manipulação de dados e criação de tabelas.
  * `numpy` → para cálculos financeiros.
  * `matplotlib` → para gerar gráficos comparativos.
  * `dateutil` → para manipulação de datas.

---

## Estrutura do Projeto

```text
comparai/
│
├── comparai.py          # Script principal do comparador
└── README.md            # Documentação em Markdown
```

---

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seuusuario/comparai.git
cd comparai
```

2. Instale as dependências:

```bash
pip install pandas numpy matplotlib requests python-dateutil
```

---

## Como Executar

```bash
python comparai.py
```

O script solicitará:

1. Nome e telefone.
2. Modalidade de financiamento (1, 2 ou 3).
3. Mês e ano de referência.
4. Valor do bem, valor a ser financiado e rendimento mensal.

Após a entrada dos dados, o programa exibirá:

* Mensagem de alerta se o valor solicitado ultrapassar 80% do bem.
* Resumo do solicitante.
* Tabela de opções de financiamento agrupada por prazo.
* Pergunta se deseja entrar em contato com a instituição.
* Gráfico comparativo de parcelas e juros com valores em destaque.

---

## Exemplo de Entrada

```
Informe seu nome: Rosangela
Informe seu telefone (DDD + celular): (14) 12345-6789
Escolha a modalidade de financiamento: 1
Digite o mês (2 dígitos, ex: 09): 09
Digite o ano (4 dígitos, ex: 2025): 2025

Valor do bem (ex: 10.000,00): R$ 10000
Valor a ser financiado (ex: 8,000.00): R$ 9000
⚠️ O valor solicitado excede 80% do bem. Ajustando para o máximo permitido: R$ 8,000.00
Rendimento mensal (ex: 5.000,00): R$ 3000
```

---

## Exemplo de Saída

### Resumo do Solicitante

```
Nome: Rosangela
Telefone: (14) 12345-6789
Modalidade: Financiamento de Veículo
Valor do bem: R$ 10.000,00
Valor financiado: R$ 8.000,00
Rendimento mensal: R$ 3.000,00
Limite de parcela (30% do rendimento): R$ 900,00
```

### Tabela de Opções

| Nº | Prazo (meses) | Banco              | Juros ao mês (%) | CET a.a. (%) | Parcela (R\$) | Total Pago (R\$) | Juros (R\$) | Seguro (R\$) | IOF (R\$) | TAC (R\$) |
| -- | ------------- | ------------------ | ---------------- | ------------ | ------------- | ---------------- | ----------- | ------------ | --------- | --------- |
| 1  | 12            | BCO BRADESCO S.A.  | 1.45             | 19.00        | 745.00        | 8.940,00         | 940.00      | 160.00       | 30.40     | 300.00    |
| 2  | 12            | BCO DO BRASIL S.A. | 1.50             | 19.50        | 750.00        | 9.000,00         | 1.000,00    | 160.00       | 30.40     | 300.00    |
|    |               |                    |                  |              |               |                  |             |              |           |           |
| 3  | 24            | BCO BRADESCO S.A.  | 1.45             | 19.00        | 385.00        | 9.240,00         | 1.240,00    | 320.00       | 30.40     | 600.00    |
| 4  | 24            | BCO DO BRASIL S.A. | 1.50             | 19.50        | 390.00        | 9.360,00         | 1.360,00    | 320.00       | 30.40     | 600.00    |
|    |               |                    |                  |              |               |                  |             |              |           |           |
| 5  | 36            | BCO BRADESCO S.A.  | 1.45             | 19.00        | 260.00        | 9.360,00         | 1.360,00    | 480.00       | 30.40     | 800.00    |
| 6  | 36            | BCO DO BRASIL S.A. | 1.50             | 19.50        | 265.00        | 9.540,00         | 1.540,00    | 480.00       | 30.40     | 800.00    |

---

### Gráfico

* Barras azuis → Parcelas
* Barras laranja → Juros
* Valores em cima das barras para fácil leitura.

---

## Observações

* Apenas opções de financiamento que respeitam o limite de parcela (30% do rendimento) são exibidas.
* Se nenhuma opção atender às restrições, será exibida uma mensagem de alerta.
* A API do Banco Central pode não retornar dados em tempo real, então algumas tabelas podem aparecer como "Desconhecido".

## Como rodar

``` bash
pip install -r requirements.txt
```
