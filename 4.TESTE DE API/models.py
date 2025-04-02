import pandas as pd

class OperadoraModel:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path, delimiter=";", encoding="utf-8", on_bad_lines="skip")
        # self.df = pd.read_csv(csv_path)  # Carrega o CSV em um DataFrame

    def buscar(self, termo):
        # Filtra as operadoras pelo nome ou código
        resultados = self.df[self.df.apply(lambda row: termo.lower() in str(row).lower(), axis=1)]
        return resultados.to_dict(orient="records")
