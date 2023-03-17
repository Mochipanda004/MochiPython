"""API"""

import pandas as pd
from sodapy import Socrata


def consulta_base(departamento, limite):
    """Se recolectará y filtrará la informaión requerida por el usuario..."""

    client = Socrata("www.datos.gov.co", None)

    results = client.get("gt2j-8ykr", where=f"departamento_nom = '{departamento}'",
                         select = "ciudad_municipio_nom, departamento_nom, edad, fuente_tipo_contagio, tipo_recuperacion, estado, pais_viajo_1_nom",
                         limit = limite)

    # Convert to pandas DataFrame
    results_df = pd.DataFrame.from_records(results)
    if 'pais_viajo_1_nom' not in results_df.columns:
        results_df['pais_viajo_1_nom'] = ""

    results_df.columns = ["Ciudad de Ubicación", "Departamento", "Edad", "Tipo de Contagio", "Tipo de Recuperación", "Estado", "País de Procedencia"]
    
    return results_df
