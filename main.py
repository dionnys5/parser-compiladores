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
# tabela_sintaxe = open('table_sintaxe.json','w')

with open('novo-text.json', 'r') as file:
    entrada = file.read()
    tokens_saida = {}
    tabela_sintaxe = {}
    instrucoes = entrada.split(';')
    for i, instruct in enumerate(instrucoes):
        tokens = instruct.split(' ')
        if not instruct == '':
            tokens_saida['Instrucao ' + str(i)] = {}
            tabela_sintaxe['Instrucao ' + str(i)] = {}
            for t, token in enumerate(tokens):
                tokens_saida['Instrucao ' + str(i)][t] = token






    formatacao_json = json.dumps(tokens_saida)
    arquivo_tokens.write(formatacao_json)
    arquivo_tokens.close()

