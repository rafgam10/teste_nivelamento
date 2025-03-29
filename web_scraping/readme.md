
# Projeto: **TESTE DE WEB SCRAPING**

Este projeto consiste em baixar arquivos PDF de um site e compactá-los em um único arquivo ZIP.

## Requisitos

1. **Python 3.x** instalado. Se não tiver, baixe [aqui](https://www.python.org/downloads/).
2. Bibliotecas adicionais que podem ser necessárias:
   - `requests`
   - `beautifulsoup4`
   - `zipfile` (inclusa no Python)

Use o comando abaixo para instalar as dependências:

```bash
pip install requests beautifulsoup4
```

## Estrutura do Projeto

O projeto contém os seguintes scripts:

- `baixar_pdfs.py` - Realiza o download dos arquivos PDF.
- `compactar_pdfs.py` - Compacta os PDFs baixados em um único arquivo ZIP.
- `main.py` - Executa os scripts acima em sequência.

## Passo a Passo para Execução

### 1. Clone ou baixe o repositório

Clone o repositório ou baixe os arquivos para sua máquina.

```bash
git clone https://seu-repositorio.com
cd seu-repositorio
```

### 2. Verifique se as dependências estão instaladas

Execute o seguinte comando para instalar as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

Se você não tem um arquivo `requirements.txt`, basta instalar manualmente:

```bash
pip install requests beautifulsoup4
```

### 3. Edite os scripts se necessário

Verifique os scripts para garantir que os caminhos dos arquivos e URLs estão corretos.  
- **`baixar_pdfs.py`**: Onde você define os links dos PDFs que deseja baixar.
- **`compactar_pdfs.py`**: Onde você define o local onde os PDFs serão compactados.

### 4. Execute o `main.py`

Após garantir que tudo está configurado, execute o script principal `main.py`, que irá:
1. Baixar os PDFs.
2. Compactá-los em um arquivo ZIP.

Execute o código com o comando abaixo:

```bash
python main.py
```

### 5. Verifique a saída

Após a execução, você verá os seguintes resultados:

- Os arquivos PDF serão baixados com sucesso.
- O arquivo `pdfs_compactados.zip` será criado, contendo todos os PDFs.

## Estrutura de Diretórios Esperada

A estrutura de arquivos esperada para execução do código é a seguinte:

```graphql
meu-projeto/
│
├── baixar_pdfs.py        # Script para baixar PDFs
├── compactar_pdfs.py     # Script para compactar os PDFs baixados
├── main.py               # Script principal que chama os outros dois
├── requirements.txt      # Arquivo com dependências
```

## Como Funciona?

- **`baixar_pdfs.py`**: Faz a requisição ao site e baixa os arquivos PDF para uma pasta local.
- **`compactar_pdfs.py`**: Após os PDFs serem baixados, esse script os compacta em um único arquivo ZIP.
- **`main.py`**: Controla a execução, chamando o script de download e depois o de compactação, em sequência.

