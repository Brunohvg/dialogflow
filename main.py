import requests
from flask import Flask, request
from funciton.horario import horarios
from funciton.calcular_motoboy import calculate_order
from funciton.gerar_link import gerar_link
from funciton.calcular_correios import calcular_correio

app = Flask(__name__)


HANDLERS = {
    'horario': horarios,
    'MotoBoy': calculate_order,
    'GerarLink': gerar_link,
    'PrecoCorreio': calcular_correio
}

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8080

@app.route('/', methods=['GET'])
def index():
    return "HANDLERS"

@app.route('/webhook', methods=['POST'])
def handle_request():
    dados = request.get_json(silent=True)
    intent = dados['queryResult']['intent']['displayName']
    
    handler = HANDLERS.get(intent)
    if handler:
        return handler(dados)
    else:
        return {"fulfillmentText": "Intenção não reconhecida"}

if __name__ == '__main__':
    
    app.run(host=SERVER_HOST, port=SERVER_PORT, debug=True)
