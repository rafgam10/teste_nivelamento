from flask import Flask
from routes import operadora_bp
from flask_cors import CORS  # Importação do CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

# Registrar as rotas
app.register_blueprint(operadora_bp)

if __name__ == '__main__':
    app.run(debug=True)
