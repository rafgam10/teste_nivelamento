# Teste de Nivelamento

## 📌 Sobre o Teste
Este teste foi desenvolvido para avaliar suas habilidades em programação, organização e estruturação do código. As tarefas propostas refletem cenários comuns enfrentados no dia a dia da empresa, permitindo uma análise prática das suas competências.

## 🎯 Critérios de Avaliação
Os seguintes critérios serão considerados durante a avaliação do seu teste:

- ✅ **Conhecimentos fundamentais de programação**
- ✅ **Organização e estruturação do código**
- ✅ **Boas práticas de desenvolvimento**

## 💡 Diferenciais Considerados
Além dos critérios básicos, também são valorizados os seguintes diferenciais:

- 🔹 **Realização de testes adicionais** (unitários, integração, etc.).
- 🔹 **Preocupação com performance** e eficiência do código.
- 🔹 **Arquitetura bem planejada**, modular e escalável.
- 🔹 **Uso eficiente de ferramentas de controle de versão** (Git).
- 🔹 **Aplicação de infraestrutura em nuvem** para facilitar o deploy e escalabilidade.

📢 *Atenção:* Os diferenciais não são obrigatórios, mas demonstram competências valorizadas pela empresa. Caso não tenha experiência em algum desses tópicos, concentre-se na qualidade e clareza do seu código.

---

## 📝 Estrutura do Teste

### **1️⃣ Web Scraping**
- [X] Acessar o site da ANS.
- [X] Baixar os arquivos PDF (Anexos I e II).
- [X] Compactar os arquivos em um único `.zip`.

📌 **Tecnologias sugeridas**: `requests`, `BeautifulSoup`, `zipfile`.

---

### **2️⃣ Transformação de Dados**
- [X] Extrair a tabela "Rol de Procedimentos e Eventos em Saúde" do Anexo I.
- [X] Salvar os dados extraídos em `.csv`.
- [X] Substituir abreviações conforme legenda do PDF.
- [X] Compactar o `.csv` gerado.

📌 **Tecnologias sugeridas**: `pdfplumber`, `pandas`, `os`, `zipfile`.

---

### **3️⃣ Banco de Dados**
- [X] Baixar arquivos de demonstrações contábeis e dados cadastrais das operadoras.
- [X] Criar estrutura de tabelas no MySQL/PostgreSQL.
- [X] Importar os dados para o banco de dados.
- [X] Criar queries para análise de despesas das operadoras.

📌 **Tecnologias sugeridas**: `MySQL/PostgreSQL`.

---

### **4️⃣ API - Desenvolvimento Web**
- [X] Criar uma API em Flask.
- [X] Criar rota para busca textual de operadoras.
- [X] Criar interface web usando Vue.js.
- [X] Criar coleção no Postman para testes.

📌 **Tecnologias sugeridas**: `Flask(flask_cors)`, `Pandas`, `Axios`, `Vue.js`, `Postman`.

---

## 🚀 Como Submeter o Teste
1. Suba seu código para um repositório no **GitHub/GitLab/Bitbucket**.
2. Inclua um arquivo `README.md` com instruções de instalação e execução.
3. Envie o link do repositório conforme solicitado.

Boa sorte! 🚀

## 📂 Estrutura do Projeto

```graphql
📂 teste_nivelamento/
│── 📂 1.web_scraping/         # Código relacionado ao download de PDFs
│   ├── baixar_pdfs.py       # Script para baixar os PDFs
│   ├── compactar_pdfs.py    # Script para compactar os arquivos baixados
│   ├── requirements.txt     # Dependências necessárias (ex: requests, BeautifulSoup)
|   ├── readme.md     
│
│── 📂 2.transformacao_dados/  # Código de extração e tratamento de dados
│   ├── extrair_tabela.py    # Script para extrair tabela do PDF
│   ├── compactar_csv.py     # Script para compactar o CSV gerado
│   ├── requirements.txt     # Dependências (ex: pdfplumber, pandas)
|   ├── readme.md     
│
│── 📂 3.banco_dados/          # Scripts SQL e inserção de dados no banco
│   ├── demonstracoes_contabeis_2023.sql   # Código SQL para csv 2023 todo
│   ├── demonstracoes_contabeis_2024.sql   # Código SQL para csv 2024 todo
│   ├── pesquisa_operadoras_trimestre.sql   # Código com resultado trimestre
│   ├── pesquisa_operadoras_ano.sql   # Código com resultado ano
│   ├── download     # Arquivos de uso
|   ├── Resultados_consultas     # pngs de Resultados
│
│── 📂 4.TESTE DE API/                  # Código do servidor Flask e interface Vue.js
│   ├── app.py               # Servidor Flask
│   ├── models.py            # Modelos de banco de dados
│   ├── routes.py            # Definição de rotas da API
│   ├── frontend/            # Interface em Vue.js
│   │   ├── components/      # Componentes Vue.js
│   │   ├── App.vue          # Arquivo principal Vue.js
│   ├── requirements.txt     # Dependências (ex: Flask, Flask-RESTful)
|   ├── readme.md     
│── README.md                # Instruções para instalação e execução
│── .gitignore               # Arquivos e pastas a serem ignorados no Git
```

## 📝 Docs Utilizados

- [Ambiente_Virtual](https://docs.python.org/pt-br/3.13/tutorial/venv.html)
- [Introdução ao BeautifulSoup – Raspagem de Dados com Python](https://www.hashtagtreinamentos.com/introducao-ao-beautifulsoup-python)
- [zipfile — Trabalha com arquivos ZIP](https://docs.python.org/pt-br/3.13/library/zipfile.html)
- [Docs Pandas](https://pandas.pydata.org/docs/)
- [Docs Tabula-py](https://tabula-py.readthedocs.io/en/latest/tabula.html)

