import os
import json
import requests as re


def calculate_order(dados):

    # Pega o cep da entrega
    cep = dados['queryResult']['parameters']['motoboy']


    # Pega a chave secreta da API
    my_secret = os.environ['secret_key']
    headers = {'X-DV-Auth-Token': my_secret}


    url = 'https://robotapitest-br.borzodelivery.com/api/business/1.2/calculate-order'

    # Monta o objeto com os dados da entrega
    data = {
        'matter': 'Documents',
        'points': [{
            'address': '30170-130'
        }, {
            'address': cep
        }]
    }

    # Faz a requisição para calcular o valor da entrega
    try:
        response = re.post(url, json=data, headers=headers)
        if response.status_code != 200:
            raise ValueError(
                f"Ocorreu um erro ao acessar a API: {response.text}")
        response_dict = response.json()

    except re.exceptions.RequestException as e:
        print(f"Ocorreu um erro ao acessar a API: {e}")
        return None

    except ValueError as e:
        print(e)
        return None
    #return response_dict

    # Pega o valor da entrega
    valor = response_dict['order']['delivery_fee_amount']
    endereço = response_dict
    valor_float = float(valor)
    valor_total = valor_float * 1.36
    print(valor_total)
    # Montar resposta
   # fulfillment_text = f"Valor da corrida fica em R$ {valor_total:.2f}\nEste valor é pago diretamente para o motoboy no ato da entrega em dinheiro ou pix"

    # Retornar responsta para o cliente
    #return {"fulfillmentText": fulfillment_text}

    fulfillment_text2 = f"Valor da corrida fica em R$ {valor_total:.2f}\nEste valor é pago diretamente para o motoboy no ato da entrega em dinheiro ou pix"
    fulfillment_text = f"O endereço de entrega é {endereço['order']['points'][1]['address']}"
    return {"fulfillmentMessages": [{"text": {"text": [fulfillment_text]}}, {"text": {"text": [fulfillment_text2]}}]}

 