class Financiamento:
    def __init__(self, valor_bem: float, valor_financiado: float, rendimento: float):
        self.valor_bem = valor_bem
        self.valor_financiado = valor_financiado
        self.rendimento = rendimento
        self.limite_parcela = rendimento * 0.3
        self.max_financiamento = valor_bem * 0.8
