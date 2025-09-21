from typing import List
from domain.entities.banco import Banco
from domain.regras import calcular_parcela, calcular_cet

def gerar_opcoes_financiamento(valor_financiado: float, prazo_list: List[int], bancos: List[Banco], taxas_mensais: List[float], limite_parcela: float):
    resultados = []
    seq = 1
    for prazo in prazo_list:
        melhores = sorted(zip(bancos, taxas_mensais), key=lambda x: x[1])[:2]  # 2 melhores por prazo
        for banco, taxa_mensal in melhores:
            parcela = calcular_parcela(valor_financiado, taxa_mensal, prazo)
            if parcela > limite_parcela:
                continue
            total = parcela * prazo
            juros_total = total - valor_financiado
            cet, seguro, iof, tac = calcular_cet(valor_financiado, prazo, taxa_mensal)
            resultados.append({
                "Nº": seq,
                "Prazo (meses)": prazo,
                "Banco": banco.nome,
                "Juros ao mês (%)": round(taxa_mensal*100, 4),
                "CET a.a. (%)": round(cet*100, 2),
                "Parcela (R$)": round(parcela, 2),
                "Total Pago (R$)": round(total, 2),
                "Juros (R$)": round(juros_total, 2),
                "Seguro (R$)": round(seguro, 2),
                "IOF (R$)": round(iof, 2),
                "TAC (R$)": round(tac, 2)
            })
            seq += 1
        # Linha em branco entre grupos
        resultados.append({k: "" for k in resultados[-1].keys()})
    return resultados
