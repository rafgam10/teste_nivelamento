import pandas as pd
import zipfile
import os

def compactar_csv():
    pasta_local = "pasta_prf"  # Pasta onde os arquivos CSV foram salvos
    arquivos_csv = [f for f in os.listdir(pasta_local) if f.endswith('.csv')]  # Lista de arquivos CSV

    # Caminho do arquivo compactado
    arquivo_zip = f"Teste_Rafael.zip"


    # Cria o arquivo zip
    with zipfile.ZipFile(arquivo_zip, 'w') as zipf:
        for arquivo_csv in arquivos_csv:
            caminho_arquivo = os.path.join(pasta_local, arquivo_csv)
            
            # Lê o arquivo CSV, ignorando linhas problemáticas
            try:
                df = pd.read_csv(caminho_arquivo, on_bad_lines='skip')  # Ignora as linhas com problemas
                # Salva o CSV compactado
                with zipf.open(arquivo_csv, 'w') as arquivo_zipado:
                    df.to_csv(arquivo_zipado, index=False)  # Salva o CSV dentro do zip

            except Exception as e:
                print(f"Erro ao processar {arquivo_csv}: {e}")

    print(f"Arquivos CSV compactados em '{arquivo_zip}' com sucesso!")
