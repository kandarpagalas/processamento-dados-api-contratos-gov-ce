import requests
import pandas as pd

endpoint = "https://api-dados-abertos.cearatransparente.ce.gov.br/transparencia/contratos/contratos"


for ano in range(2024, 2013, -1):
    max_pages = 5
    last_page = 0

    all_contratos = []
    while last_page < max_pages:
        params = {
            "page": last_page + 1,
            "data_assinatura_inicio": f"01/01/{ano}",
            "data_assinatura_fim": f"31/12/{ano}",
        }

        res = requests.get(endpoint, params=params)


        if res.status_code == 200:
            data = res.json()

            total_pages = data["sumary"]["total_pages"]
            last_page = int(data["sumary"]["current_page"])

            if max_pages != int(total_pages):
                max_pages = int(total_pages)

            print(f"{ano} - {last_page}/{total_pages}")

            contratos = data["data"]
            all_contratos.extend(contratos)

        df = pd.DataFrame(all_contratos)
        df.to_csv(f"data/contratos_{ano}.csv")