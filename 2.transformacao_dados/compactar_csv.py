import pandas as pd
import os
import zipfile

# Função usando para ser chamando no main.py
def compactar_csv_modulo():

    # Nome do arquivo CSV extraído anteriormente
    csv_path = "saida/Rol_de_Procedimentos.csv"  # Caminho do arquivo CSV
    test_zip_path = "saida/Teste_seu_nome.zip"  # Nome do arquivo ZIP de saída

    # Dicionário contendo as substituições necessárias para as abreviações
    substituicoes = {"OD": "Odontológica", "AMB": "Ambulatorial"}

    def processar_csv(csv_path):
        """
        Função para abrir o arquivo CSV, substituir as abreviações e salvar novamente.
        """
        df = pd.read_csv(csv_path)  # Carregar os dados do CSV em um DataFrame
        
        # Percorrer todas as colunas e substituir os valores conforme o dicionário
        for coluna in df.columns:
            df[coluna] = df[coluna].replace(substituicoes)
        
        # Salvar o arquivo atualizado, mantendo o formato CSV
        df.to_csv(csv_path, index=False, encoding='utf-8')  # Salvar sem incluir os índices
        print("Substituições concluídas e arquivo atualizado!")

    def compactar_csv(csv_path, zip_path):
        """
        Função para compactar o arquivo CSV em um arquivo ZIP.
        """
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:  # Criar arquivo ZIP
            zipf.write(csv_path, os.path.basename(csv_path))  # Adicionar o CSV ao ZIP
        print(f"Arquivo compactado e salvo em '{zip_path}'")

    # Executar as funções para processar e compactar o arquivo
    processar_csv(csv_path)  # Chamar a função para substituir as abreviações
    compactar_csv(csv_path, test_zip_path)  # Chamar a função para compactar o CSV




