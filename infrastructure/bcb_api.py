import requests

BASE_URL = "https://www.bcb.gov.br/api/servico/sitebcb/historicotaxajurosdiario/atual"

def get_taxas_json(codigo_modalidade: str, data_inicio: str):
    filtro = (
        f"(codigoSegmento eq '1') and "
        f"(codigoModalidade eq '{codigo_modalidade}') and "
        f"(InicioPeriodo eq '{data_inicio}')"
    )
    params = {"filtro": filtro}
    try:
        resp = requests.get(BASE_URL, params=params)
        resp.raise_for_status()
        dados = resp.json()
        return dados.get("conteudo", []), dados.get("parametros", {}).get("InicioPeriodo", "Desconhecido")
    except:
        return [], "Desconhecido"
