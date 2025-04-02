# 📌 Projeto: Busca de Operadoras de Saúde

Este projeto consiste em uma aplicação web que permite buscar operadoras de saúde a partir de um CSV. O backend foi desenvolvido em **Flask**, e o frontend em **Vue.js**.

---

## 🚀 **Tecnologias Utilizadas**

- **Backend:** Python, Flask, Pandas, Flask-CORS
- **Frontend:** Vue.js, Vite, Axios
- **Banco de Dados:** CSV (Pandas para manipulação)

---

## 📂 **Estrutura do Projeto**

```
📦 operadoras-projeto
 │   ├── app.py            # Arquivo principal do servidor Flask
 │   ├── models.py         # Modelo para carregar e filtrar dados do CSV
 │   ├── routes.py         # Rotas da API
 │   ├── Relatorio_cadop.csv # Base de dados CSV
 │   ├── requirements.txt  # Dependências do backend
 ├── 📂 frontend
 │   ├── 📂 src
 │   │   ├── App.vue       # Componente principal
 │   │   ├── main.js       # Arquivo de inicialização do Vue.js
 │   │   ├── 📂 components
 │   │   │   ├── SearchBar.vue   # Componente da barra de busca
 │   │   │   ├── ResultsList.vue # Componente para exibir os resultados
 │   ├── index.html        # Estrutura HTML
 │   ├── package.json      # Dependências do frontend
 ├── README.md             # Documentação
```

---

## 🖥️ **Executando o Backend**

### 1️⃣ **Instalar as dependências**

Acesse a pasta `backend` e instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

### 2️⃣ **Rodar o servidor Flask**

```bash
python app.py
```

O backend estará rodando em **http://127.0.0.1:5000**.

---

## 🌐 **Executando o Frontend**

### 1️⃣ **Instalar as dependências**

Acesse a pasta `frontend` e instale os pacotes do Vue.js:

```bash
npm install
```

### 2️⃣ **Rodar o servidor do Vue.js**

```bash
npm run dev
```

O frontend estará acessível em **http://localhost:5173**.

---

## 🔥 **Testando a API**

Para testar a API sem o frontend, você pode usar o Postman ou acessar a seguinte URL no navegador:

```
http://127.0.0.1:5000/buscar?q=419761
```

Isso retornará um JSON com os dados da operadora filtrada.

---

## 🤝 **Agradecimentos**

Muito obrigado pelos testes. :)

