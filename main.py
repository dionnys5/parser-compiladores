import json

linguagem = {
    'palavras_reservadas': [
        'while',
        'do'
    ],
    'operadores': [
        '<',
        '=',
        '+'
    ],
    'terminadores': [
        ';'
    ],
    'identificadores': [
        'i',
        'j'
    ],
    'numeros': [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    ]
}

arquivo_tokens = open('tokens.json', 'w')
tabela_sintaxe = open('table_sintaxe.json', 'w')


def token_identificador(token):
    """
    :param tokens: Lista de tokens
    :return: Dicionário com a situacao do erro e o identificador do token (Se houver)
    """
    erro = False
    identificador = None
    if token in linguagem['palavras_reservadas']:
        identificador = 'palavras_reservadas'
    elif token in linguagem['operadores']:
        identificador = 'operadores'
    elif token in linguagem['terminadores']:
        identificador = 'terminadores'
    elif token in linguagem['identificadores']:
        identificador = 'identificadores'
    elif len(token) > 1 and token[0] in linguagem['numeros']:
        try:
            num = int(token)
            identificador = 'sequencia'
        except ValueError:
            pass
    elif token in linguagem['numeros']:
        identificador = 'numeros'
    else:
        erro = True
    return erro, identificador


with open('novo-text.txt', 'r') as file:
    entrada = file.read()
    instrucoes = entrada.split(';')
    lista_tokens = {}
    lista_lexica = {}
    erro = False
    for i, instruct in enumerate(instrucoes):
        tokens = instruct.split(' ')
        if not instruct == '':
            tokens.append(';')
            for t, token in enumerate(tokens):
                tamanho = len(token)
                identificador = token_identificador(token)
                if identificador[0]:
                    erro = True
                    lista_lexica[token + ' ' + str((i, t))] = {
                        'token': token,
                        'erro': 'Token nao encontrado',
                        'posicao': (i, t)
                    }
                    break
                ident = identificador[1]
                lista_lexica[token + ' ' + str((i, t))] = {
                    'token': token,
                    'identificacao': ident,
                    'tamanho': tamanho,
                    'posicao': (i, t)
                }
                if ident == 'sequencia' or ident == 'identificadores':
                    lista_tokens[t] = token
        if erro:
            break

    tokens_json = json.dumps(lista_tokens)
    tabela_json = json.dumps(lista_lexica)
    arquivo_tokens.write(tokens_json)
    tabela_sintaxe.write(tabela_json)

