from bs4 import BeautifulSoup
import requests


def baixar():

    # Variavel do site para requisição:
    link = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

    # Cabeçalhos para evitar bloqueio por alguns sites:
    headers = {"User-Agent": "Mozilla/5.0"}

    # Variavel para da um GET no link:
    resposta = requests.get(link)


    # Verificação para acessa o site(200):
    if(resposta.status_code == 200):
        # Variavel para deixar a Estrutura HTMl mais padrão
        site = BeautifulSoup(resposta.text, "html.parser")

        # Loop para acha os todos os links do html que estão em tag "a"
        for linkIndex in site.find_all('a', href=True):
            file_url = linkIndex['href']

            # Filtrado apenas aqueles que tem arquivos PDF:
            if file_url.endswith('.pdf'):
                file_nome = file_url.split('/')[-1] # Pegando o nome do arquivo

                # Verificação para pegar os arquivos com o nome incial 'Anexo':
                if file_nome.startswith('Anexo'):


                    # Se o link for relativo, transformar em absoluto:
                    if not file_url.startswith('http'):
                        file_url = link + file_url
                    
                    #Exibir uma messagem:
                    print(f"Baixando PDF: {file_nome}")

                    #Baixando o arquivo:
                    file_resposta = requests.get(file_url, headers=headers)

                    #Salvado o arquivo local:
                    with open(file_nome, 'wb') as f:
                        f.write(file_resposta.content)

        print("Download Finalizando!")

    else:
        print("Erro ao acessar a paǵina:", resposta.status_code)




