from math import pow

def limpar_valor(valor_str: str) -> float:
    return float(valor_str.replace(".", "").replace(",", "."))

def calcular_data_mes_anterior(mes: str, ano: str) -> str:
    from datetime import datetime
    from dateutil.relativedelta import relativedelta
    data = datetime.strptime(f"01/{mes}/{ano}", "%d/%m/%Y")
    data_anterior = data - relativedelta(months=1)
    return data_anterior.strftime("%Y-%m-%d")

def calcular_parcela(valor: float, taxa: float, prazo: int) -> float:
    if taxa == 0:
        return valor / prazo
    return (taxa * valor) / (1 - pow(1 + taxa, -prazo))

def taxa_efetiva_anual(taxa_mensal: float) -> float:
    return pow(1 + taxa_mensal, 12) - 1

def calcular_cet(valor: float, prazo: int, taxa_mensal: float):
    seguro_anual = 0.02
    iof_aliquota = 0.0038
    tac_por_prazo = {12: 300, 24: 600, 36: 800}
    juros_aa = taxa_efetiva_anual(taxa_mensal)
    seguro_total = valor * seguro_anual * (prazo / 12)
    iof_total = valor * iof_aliquota
    tac_total = tac_por_prazo.get(prazo, 0)
    cet_total = juros_aa + (seguro_total + iof_total + tac_total) / valor
    return cet_total, seguro_total, iof_total, tac_total
