# Extração e Processamento de Dados do PDF

## Descrição do Projeto
Este projeto tem como objetivo extrair tabelas de um arquivo PDF, processar os dados extraídos e compactá-los em um arquivo ZIP.
Ele está dividido em três módulos principais:

1. **extração de tabelas do PDF**: O arquivo `extrair_tabelas.py` usa a biblioteca `pdfplumber` para extrair tabelas do PDF e salvar os dados em um arquivo CSV.
2. **processamento do CSV**: O arquivo `compactar_csv.py` substitui abreviações nas colunas do CSV e compacta o arquivo.
3. **execução principal**: O `main.py` executa os módulos em ordem e informa ao usuário sobre o tempo de execução.

## Estrutura do Projeto
```
/
|-- main.py
|-- extrair_tabelas.py
|-- compactar_csv.py
|-- saida/
    |-- Rol_de_Procedimentos.csv  (Gerado após a extração)
    |-- Teste_seu_nome.zip        (Gerado após a compactação)
```

## Instalação e Dependências
Antes de executar o projeto, instale as dependências necessárias com:
```bash
pip install pdfplumber pandas
```

## Como Usar

### 1. Executar o programa principal
No terminal, execute:
```bash
python main.py
```
> **Atenção:** O processo pode demorar alguns minutos dependendo do tamanho do PDF.

## Explicação dos Arquivos

### `extrair_tabelas.py`
Este script extrai tabelas do PDF e as salva em um arquivo CSV dentro da pasta `saida/`.
- **Abre o PDF e percorre todas as páginas**
- **Extrai tabelas e armazena os dados**
- **Garante que o cabeçalho apareça apenas uma vez**
- **Salva os dados extraídos em `Rol_de_Procedimentos.csv`**

### `compactar_csv.py`
Este script processa o CSV e o compacta em um arquivo ZIP.
- **Substitui abreviações:**
  - "OD" → "Odontológica"
  - "AMB" → "Ambulatorial"
- **Salva o CSV atualizado**
- **Compacta o arquivo em `Teste_seu_nome.zip`** -> `Teste_Rafael.zip`

### `main.py`
O arquivo principal que chama os outros módulos e executa o processo completo.

