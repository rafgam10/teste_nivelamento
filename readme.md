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
- [ ] Extrair a tabela "Rol de Procedimentos e Eventos em Saúde" do Anexo I.
- [ ] Salvar os dados extraídos em `.csv`.
- [ ] Substituir abreviações conforme legenda do PDF.
- [ ] Compactar o `.csv` gerado.

📌 **Tecnologias sugeridas**: `pdfplumber`, `pandas`, `zipfile`.

---

### **3️⃣ Banco de Dados**
- [ ] Baixar arquivos de demonstrações contábeis e dados cadastrais das operadoras.
- [ ] Criar estrutura de tabelas no MySQL/PostgreSQL.
- [ ] Importar os dados para o banco de dados.
- [ ] Criar queries para análise de despesas das operadoras.

📌 **Tecnologias sugeridas**: `MySQL/PostgreSQL`, `pymysql`, `psycopg2`.

---

### **4️⃣ API - Desenvolvimento Web**
- [ ] Criar uma API em Flask.
- [ ] Criar rota para busca textual de operadoras.
- [ ] Criar interface web usando Vue.js.
- [ ] Criar coleção no Postman para testes.

📌 **Tecnologias sugeridas**: `Flask`, `Flask-RESTful`, `SQLAlchemy`, `Vue.js`, `Postman`.

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
│
│── 📂 2.transformacao_dados/  # Código de extração e tratamento de dados
│   ├── extrair_tabela.py    # Script para extrair tabela do PDF
│   ├── gerar_csv.py         # Script para salvar os dados em CSV
│   ├── compactar_csv.py     # Script para compactar o CSV gerado
│   ├── requirements.txt     # Dependências (ex: pdfplumber, pandas)
│
│── 📂 3.banco_dados/          # Scripts SQL e inserção de dados no banco
│   ├── criar_tabelas.sql    # Scripts para criação de tabelas
│   ├── importar_dados.py    # Código para importar CSV para o banco
│   ├── consultas.sql        # Queries analíticas para análise de despesas
│   ├── requirements.txt     # Dependências (ex: pymysql, psycopg2)
│
│── 📂 4.api/                  # Código do servidor Flask e interface Vue.js
│   ├── app.py               # Servidor Flask
│   ├── models.py            # Modelos de banco de dados
│   ├── routes.py            # Definição de rotas da API
│   ├── frontend/            # Interface em Vue.js
│   │   ├── components/      # Componentes Vue.js
│   │   ├── App.vue          # Arquivo principal Vue.js
│   ├── requirements.txt     # Dependências (ex: Flask, Flask-RESTful)
│
│── 📂 tests/                # Testes unitários e de integração
│   ├── test_scraping.py     # Testes para web scraping
│   ├── test_transformacao.py# Testes para extração e conversão de dados
│   ├── test_api.py          # Testes da API Flask
│
│── README.md                # Instruções para instalação e execução
│── .gitignore               # Arquivos e pastas a serem ignorados no Git
│── docker-compose.yml        # (Opcional) Arquivo para subir banco e API com Docker
```

## 📝 Docs Utilizados

- [Ambiente_Virtual](https://docs.python.org/pt-br/3.13/tutorial/venv.html)
- [Introdução ao BeautifulSoup – Raspagem de Dados com Python](https://www.hashtagtreinamentos.com/introducao-ao-beautifulsoup-python)
- [zipfile — Trabalha com arquivos ZIP](https://docs.python.org/pt-br/3.13/library/zipfile.html)

