import os
import json
import requests as re
from unidecode import unidecode

my_secret = os.environ['key_correios']
url = f"https://www.sgpweb.com.br/novo/api/consulta-postagens?chave_integracao={my_secret}&data_inicial=2023-01-01&data_final=2023-01-31"


def obert_rastreio(dados):
    nome = dados['queryResult']['parameters']['nome']
    nome = nome.upper()
    nome = unidecode(nome)

   # telefone = dados['queryResult']['parameters']['telefone']

    
    try:
        response = re.get(url)
        if response.status_code != 200:
            raise ValueError(
                f"Ocorreu um erro ao acessar a API: {response.text}")
        resultado = response.json()
        
        codigo_rastreio = None
        status = None
        for objeto in resultado['retorno']['objetos']:
            if objeto['destinatario'] == nome:
                codigo_rastreio = objeto['objeto']
                status = objeto['status']
                break
        
        if codigo_rastreio:
            fulfillment_text = f"O código de rastreio para {nome}\n*{codigo_rastreio}*\n{status}"
        else:
            fulfillment_text = f"Não encontramos nenhuma postagem para o cliente\n{nome}"
            
    except re.exceptions.RequestException as e:
        print(f"Ocorreu um erro ao acessar a API: {e}")
        return None
    except ValueError as e:
        print(e)
        return None
    
    return {"fulfillmentText": fulfillment_text}
