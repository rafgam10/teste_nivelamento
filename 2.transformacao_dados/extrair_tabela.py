# Importar o comando "read_pdf" do tabula
from tabula import read_pdf
import os

#Função para fazer a chamanda no main.py:
def extrair_tabelas():

    # Caminho do PDF
    arquivo_pdf = "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"

    # Variável da Pasta local
    pasta_local = "pasta_prf"

    # Fazendo uma verificação se a pasta existe, se não, cria a pasta
    if not os.path.exists(pasta_local):
        os.makedirs(pasta_local)

    # Extrai todas as tabelas do PDF para DataFrames
    tabelas = read_pdf(arquivo_pdf, pages="all", multiple_tables=True)

    # Salva cada tabela extraída em CSV
    for i, tabela in enumerate(tabelas):
        caminho_arquivo = os.path.join(pasta_local, f"tabela_extraida.csv")
        tabela.to_csv(caminho_arquivo, index=False)

    print(f"Tabelas extraídas e salvas na pasta '{pasta_local}' com sucesso!")
