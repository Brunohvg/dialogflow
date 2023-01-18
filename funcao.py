def buscarCep(cep, api='viacep', formato='json'):
    import requests as re
    # Remover o hífen do CEP caso for passado
    cep = cep.replace('-', '')
    
    # Verificar se o CEP possui 8 dígitos e é composto apenas por números
    if len(cep) == 8 and cep.isnumeric():
        # Montar a URL da API de CEP
        if api == 'viacep':
            url = f'https://viacep.com.br/ws/{cep}/{formato}/'
        elif api == 'cepaberto':
            url = f'https://www.cepaberto.com/api/v3/cep?cep={cep}'
        else:
            return 'API de CEP inválida'
        
        # Fazer a requisição à API de CEP
        try:
            date = re.get(url, timeout=5)
            # Verificar se a requisição foi bem-sucedida
            if date.status_code == 200:
                date = date.json() if formato == 'json' else date.xml()
                # Verificar se o CEP foi encontrado na base de dados da API
                if 'erro' in date:
                    return 'CEP não encontrado'
                else:
                    return datedef buscarCep(cep, api='viacep', formato='json'):
    import requests as re
    # Remover o hífen do CEP caso for passadodef buscarCep(cep, api='viacep', formato='json'):
    import requests as re
    # Remover o hífen do CEP caso for passado
    cep = cep.replace('-', '')
    
    # Verificar se o CEP possui 8 dígitos e é composto apenas por números
    if len(cep) == 8 and cep.isnumeric():
        # Montar a URL da API de CEP
        if api == 'viacep':
            url = f'https://viacep.com.br/ws/{cep}/{formato}/'
        elif api == 'cepaberto':
            url = f'https://www.cepaberto.com/api/v3/cep?cep={cep}'
        else:
            return 'API de CEP inválida'
        
        # Fazer a requisição à API de CEP
        try:
            date = re.get(url, timeout=5)
            # Verificar se a requisição foi bem-sucedida
            if date.status_code == 200:
                date = date.json() if formato == 'json' else date.xml()
                # Verificar se o CEP foi encontrado na base de dados da API
                if 'erro' in date:
                    return 'CEP não encontrado'
                else:
                    return datedef buscarCep(cep, api='viacep', formato='json'):
    import requests as re
    # Remover o hífen do CEP caso for passado
    cep = cep.replace('-', '')
    
    # Verificar se o CEP possui 8 dígitos e é composto apenas por números
    if len(cep) == 8 and cep.isnumeric():
        # Montar a URL da API de CEP
        if api == 'viacep':
            url = f'https://viacep.com.br/ws/{cep}/{formato}/'
        elif api == 'cepaberto':
            url = f'https://www.cepaberto.com/api/v3/cep?cep={cep}'
        else:
            return 'API de CEP inválida'
        
        # Fazer a requisição à API de CEP
        try:
            date = re.get(url, timeout=5)
            # Verificar se a requisição foi bem-sucedida
            if date.status_code == 200:
                date = date.json() if formato == 'json' else date.xml()
                # Verificar se o CEP foi encontrado na base de dados da API
                if 'erro' in date:
                    return 'CEP não encontrado'
                else:
                    return date
            else:
                return 'Erro ao buscar o CEP'
        except Exception as e:
            return f'Erro: {e}'
    else:
        return 'CEP inválido'

            else:
                return 'Erro ao buscar o CEP'
        except Exception as e:
            return f'Erro: {e}'
    else:
        return 'CEP inválido'

    cep = cep.replace('-', '')
    
    # Verificar se o CEP possui 8 dígitos e é composto apenas por números
    if len(cep) == 8 and cep.isnumeric():
        # Montar a URL da API de CEP
        if api == 'viacep':
            url = f'https://viacep.com.br/ws/{cep}/{formato}/'
        elif api == 'cepaberto':
            url = f'https://www.cepaberto.com/api/v3/cep?cep={cep}'
        else:
            return 'API de CEP inválida'
        
        # Fazer a requisição à API de CEP
        try:
            date = re.get(url, timeout=5)
            # Verificar se a requisição foi bem-sucedida
            if date.status_code == 200:
                date = date.json() if formato == 'json' else date.xml()
                # Verificar se o CEP foi encontrado na base de dados da API
                if 'erro' in date:
                    return 'CEP não encontrado'
                else:
                    return date
            else:
                return 'Erro ao buscar o CEP'
        except Exception as e:
            return f'Erro: {e}'
    else:
        return 'CEP inválido'

            else:
                return 'Erro ao buscar o CEP'
        except Exception as e:
            return f'Erro: {e}'
    else:
        return 'CEP inválido'
