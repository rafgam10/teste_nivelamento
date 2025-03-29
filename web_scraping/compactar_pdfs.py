import zipfile


def compactar():
    print("Compactando PDFs...")

    # Variavel para o arquivo Zip:
    nome_zip = "pdfs_compactados.zip"

    # Lista com o nome dos arquivos:
    arquivosPDF = ['Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf', 'Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf']


    # Criando o zip e adiciona apenas os PDF:
    with zipfile.ZipFile(nome_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for arquivo in arquivosPDF:
            if arquivo.endswith('.pdf'):
                zipf.write(arquivo)

    print(f"Arquivos PDF compactados em '{nome_zip}' com sucesso!")
