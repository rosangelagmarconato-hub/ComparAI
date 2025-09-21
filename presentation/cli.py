from domain.entities.cliente import Cliente
from domain.entities.banco import Banco
from domain.entities.modalidade import Modalidade
from domain.entities.financiamento import Financiamento
from domain.regras import limpar_valor, calcular_data_mes_anterior
from infrastructure.bcb_api import get_taxas_json
from application.services.simulacao_financiamento import gerar_opcoes_financiamento
from application.services.apresentacao_tabela import mostrar_tabela, gerar_grafico

BANCOS = [
    "BCO COOPERATIVO SICREDI S.A.",
    "BCO BRADESCO S.A.",
    "BCO DO BRASIL S.A.",
    "ITAÚ UNIBANCO S.A.",
    "BANCO SICOOB S.A.",
    "CAIXA ECONOMICA FEDERAL"
]

MODALIDADES = {
    "1": Modalidade("Veículo", "401101"),
    "2": Modalidade("Imóvel (taxa de mercado)", "903101"),
    "3": Modalidade("Imóvel (taxa regulada - CEF)", "905101")
}

def main():
    print("\n" + "="*60)
    print("📢 COMPARAI: Seu comparador inteligente de crédito".upper())
    print("="*60 + "\n")

    nome = input("Informe seu nome: ")
    telefone = input("Informe seu telefone (DDD + celular): ")
    cliente = Cliente(nome, telefone)

    print("\nEscolha a modalidade de financiamento:")
    for key, mod in MODALIDADES.items():
        print(f"{key} - {mod.nome}")
    escolha = input("Digite 1, 2 ou 3: ").strip()
    if escolha not in MODALIDADES:
        print("Modalidade inválida.")
        return
    modalidade = MODALIDADES[escolha]

    print("\nInforme o mês e ano de referência:\n")
    mes = input("Digite o mês (2 dígitos, ex: 09): ").zfill(2)
    ano = input("Digite o ano (4 dígitos, ex: 2025): ")

    print("\n")
    try:
        valor_bem = limpar_valor(input("Valor do bem (ex: 10.000,00): R$ "))
        valor_financiado = limpar_valor(input(f"Valor a ser financiado (ex: {valor_bem*0.8:,.2f}): R$ "))
        if valor_financiado > valor_bem*0.8:
            print(f"\n⚠️ O valor solicitado excede 80% do bem. Ajustando para o máximo permitido: R$ {valor_bem*0.8:,.2f}\n")
            valor_financiado = valor_bem*0.8
        rendimento = limpar_valor(input("Rendimento mensal (ex: 5.000,00): R$ "))
    except ValueError:
        print("Digite os valores corretamente.")
        return

    financiamento = Financiamento(valor_bem, valor_financiado, rendimento)

    print(f"\nResumo do solicitante:\nNome: {cliente.nome}\nTelefone: {cliente.telefone}\nModalidade: {modalidade.nome}")
    print(f"Valor do bem: R$ {financiamento.valor_bem:,.2f}\nValor financiado: R$ {financiamento.valor_financiado:,.2f}")
    print(f"Rendimento mensal: R$ {financiamento.rendimento:,.2f}\nLimite de parcela (30% do rendimento): R$ {financiamento.limite_parcela:,.2f}\n")

    data_inicio = calcular_data_mes_anterior(mes, ano)
    taxas_json, data_tabela = get_taxas_json(modalidade.codigo, data_inicio)

    bancos = []
    taxas_mensais = []
    for t in taxas_json:
        banco_nome = t.get("InstituicaoFinanceira")
        taxa_str = t.get("TaxaJurosAoMes")
        if banco_nome in BANCOS and taxa_str:
            bancos.append(Banco(banco_nome))
            taxas_mensais.append(float(taxa_str.replace(",", "."))/100)

    resultados = gerar_opcoes_financiamento(financiamento.valor_financiado, [12, 24, 36], bancos, taxas_mensais, financiamento.limite_parcela)
    df = mostrar_tabela(resultados)
    if df is not None:
        gerar_grafico(df)

    resposta = input("\nDeseja entrar em contato com a instituição escolhida? (sim/não): ").strip().lower()
    if resposta == "sim":
        opcao = input("Informe o número da condição desejada: ")
        print(f"\n✅ Obrigado, {cliente.nome}. Enviaremos seu contato ao gerente da instituição nº {opcao}. Ele entrará em contato pelo telefone informado ({cliente.telefone}).\n")
    else:
        print(f"\nObrigado por utilizar o COMPARAI, {cliente.nome}. Estamos sempre à disposição.\n")

if __name__ == "__main__":
    main()
