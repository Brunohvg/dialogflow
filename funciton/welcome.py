def welcome(dados):
    # Montar resposta
    fulfillment_text = "Bem-vindo! Como posso te ajudar hoje?"

    # Adicionar botões de quick replies
    quick_replies = [
        {
            "content_type": "text",
            "title": "Motoboy",
            "payload": "motoboy"
        },
        {
            "content_type": "text",
            "title": "Correio",
            "payload": "correio"
        }
    ]

    # Retornar responsta para o cliente
    return {
        "fulfillmentText": fulfillment_text,
        "fulfillmentMessages": [
            {
                "platform": "FACEBOOK",
                "quickReplies": {
                    "title": "Opções",
                    "quickReplies": quick_replies
                }
            },
            {
                "text": {
                    "text": [
                        fulfillment_text
                    ]
                }
            }
        ],
        "payload": {
          "facebook": {
            "text": fulfillment_text,
            "quick_replies": quick_replies
          }
        }
    }
