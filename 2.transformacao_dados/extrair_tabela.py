import pdfplumber
import pandas as pd
import os

def extrair_tabelas_modulo():
    # Criar diretório para salvar os arquivos
    output_dir = "saida"
    os.makedirs(output_dir, exist_ok=True)

    # Caminho do PDF (substitua pelo caminho correto)
    pdf_path = "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"

    def extrair_tabela(pdf_path):
        dados = []
        cabecalho = None  # Armazena o cabeçalho para garantir que apareça apenas uma vez
        
        with pdfplumber.open(pdf_path) as pdf:
            for pagina in pdf.pages:
                tabelas = pagina.extract_tables()
                for tabela in tabelas:
                    for i, linha in enumerate(tabela):
                        if i == 0:  # Primeira linha pode ser cabeçalho
                            if cabecalho is None:
                                cabecalho = linha  # Define o cabeçalho apenas uma vez
                            continue  # Evita adicionar o cabeçalho repetidamente
                        dados.append(linha)
        
        # Criar DataFrame
        df = pd.DataFrame(dados, columns=cabecalho)
        return df

    # Extrair a tabela e salvar em CSV
    df_tabela = extrair_tabela(pdf_path)
    csv_path = os.path.join(output_dir, "Rol_de_Procedimentos.csv")
    df_tabela.to_csv(csv_path, index=False, encoding='utf-8')
    print(f"Extração concluída! Dados salvos em '{csv_path}'")
