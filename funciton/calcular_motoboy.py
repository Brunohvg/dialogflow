def calculate_order(dados):
    import os
    import requests

    # Pega o cep da entrega
    cep = dados['queryResult']['parameters']['motoboy']

    # Pega a chave secreta da API
    my_secret = os.environ['secret_key']
    headers = {'X-DV-Auth-Token': my_secret}

    # Url 
    url = 'https://robotapitest-br.borzodelivery.com/api/business/1.2/calculate-order'
    
    # Monta o objeto com os dados da entrega
    data = {
        'matter': 'Documents', 
        'points': [
            {'address':'30170-130'}, 
            {'address': cep}
        ]
    }
    
    # Faz a requisição para calcular o valor da entrega
    r = requests.post(url, json=data, headers=headers)
    response_dict = r.json()

    # Pega o valor da entrega
    valor = response_dict['order']['delivery_fee_amount']
    valor_float = float(valor)
    valor_total = valor_float * 1.36    
    print(valor_total)
    # Montar resposta 
    fulfillment_text = f"Valor da corrida fica em R$ {valor_total:.2f}, este valor é pago diretamente para o motoboy no ato da entrega em dinheiro ou pix "
    
    # Retornar responsta para o cliente 
    return {"fulfillmentText": fulfillment_text}
