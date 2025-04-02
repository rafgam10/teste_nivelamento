from flask import Blueprint, request, jsonify
from models import OperadoraModel

operadora_bp = Blueprint('operadora', __name__)
model = OperadoraModel("Relatorio_cadop.csv")

@operadora_bp.route('/buscar', methods=['GET'])
def buscar_operadora():
    termo = request.args.get('q', '')
    if not termo:
        return jsonify({"erro": "Informe um termo de busca"}), 400

    resultados = model.buscar(termo)
    return jsonify(resultados)
