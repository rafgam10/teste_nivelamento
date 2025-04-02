from flask import Flask
from routes import operadora_bp

app = Flask(__name__)

# Registrar as rotas
app.register_blueprint(operadora_bp)

if __name__ == '__main__':
    app.run(debug=True)
