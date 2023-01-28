import requests
import json
import os


def calcular_correio(dados):
    my_secret = os.environ['key_correios']
    url = f"https://www.sgpweb.com.br/novo/api/consulta-precos-prazos?chave_integracao={my_secret}"
    headers = {"Content-Type": "application/json"}

    cep = dados['queryResult']['parameters']['cepcorreios']
    peso = dados['queryResult']['parameters']['pesocorreios']
    dados = {
        "identificador": 1,
        "cep_origem": "30170-130",
        "cep_destino": cep,
        "formato": "1",
        "peso": peso,
        "comprimento": "40",
        "altura": "11",
        "largura": "25",
        "mao_propria": "N",
        "aviso_recebimento": "N",
        "valor_declarado": "100,80",
        "servicos": ["04162", "04669"]
    }

    response = requests.post(url, headers=headers, json=dados)
    response_dic = response.json()

    sedex = [
        response_dic['servicos']['04162']['Valor'],
        int(response_dic['servicos']['04162']['PrazoEntrega'])
    ]
    pac = [
        response_dic['servicos']['04669']['Valor'],
        int(response_dic['servicos']['04162']['PrazoEntrega'])
    ]

    if sedex[0] > pac[0]:
        fulfillment_text = f"Olá, o valor estimado do SEDEX é R$ {sedex[0]}\nCom tempo médio de {sedex[1]} dias.\nO valor estimado do PAC é R$ {pac[0]}\nCom tempo médio de {pac[1]} dias.\nLembre-se o tempo de entrega pode variar diacordo com o dia em que foi postado"
    else:
        fulfillment_text = f"Olá, o valor estimado do SEDEX é R$ {sedex[0]}\nCom tempo médio de {sedex[1]} dias.\nNão fazemos PAC para sua Região.\nLembre-se o tempo de entrega pode variar diacordo com o dia em que foi postado"

    return {"fulfillmentText": fulfillment_text}
