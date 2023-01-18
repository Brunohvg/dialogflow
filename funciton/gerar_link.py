def gerar_link(dados):
    import os 
    import requests
    
    # Variables 

    my_secret = os.environ['chave_Producao']
    nome = dados['queryResult']['parameters']['nomelink']
    valor = dados['queryResult']['parameters']['valorlink']
    
    # Converter valor em centavos 
    valor_centavos = valor * 100
    
    dividir = dados['queryResult']['parameters']['dividir']
    # Tratar o variavel dividir
    dividir = dividir.upper()
    if dividir == "SIM":
        qtd_min = 3
        qtd_max = 3
    else:
        qtd_min = 1
        qtd_max = 1

    # Url da chamada
    url = "https://api.pagar.me/1/payment_links"

    payload = {
        
    "api_key": my_secret,
    "amount": valor_centavos,
    "name": nome,
    "items": [
    {
    "id": "1",
    "title": nome,
    "unit_price": valor_centavos,
    "quantity": 1,
    "tangible": True
    }
    ],
    "postback_config": {
    "orders": "http://postback.url/orders",
    "transactions": "http://postback.url/transactions"
    },
    "payment_config": {
    "boleto": {
    "enabled": False,
    "expires_in": 20
    },
    "credit_card": {
    "enabled": True,
    "free_installments": qtd_min,
    "interest_rate": 25,
    "max_installments": qtd_max
    },
    "default_payment_method": "boleto"
    },
    "max_orders": 3,
    "expires_in": 120
    }
    
    headers = { "content-type": "application/json" }
    
    response = requests.post(url, json=payload, headers=headers)
    
    response_data = response.json()

    link_url = response_data.get('url')
    if link_url == None:
        fulfillment_text = "Ops algo aconteceu que não pude gerar seu link favor entrar em contato com o setor responsavel"

    if 'errors' in response_data:
        fulfillment_text = (response_data['errors'])
    else:
        fulfillment_text = f"Aqui está, {nome}\nLink no valor de R$ {valor:.2f}\n{link_url}"
        
    return {"fulfillmentText": fulfillment_text}


