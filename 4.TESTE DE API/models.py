import pandas as pd

class OperadoraModel:
    def __init__(self, csv_path):
        # Carrega o CSV e substitui NaN por string vazia
        self.df = pd.read_csv(csv_path, delimiter=";", encoding="utf-8", on_bad_lines="skip").fillna("")

    def buscar(self, termo):
        # Melhorando a filtragem para evitar erros
        termo = termo.lower()
        resultados = self.df[self.df.apply(lambda row: any(termo in str(valor).lower() for valor in row), axis=1)]
        return resultados.to_dict(orient="records")
