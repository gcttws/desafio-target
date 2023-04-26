import json

dados = []
with open("dados.json") as file:
    dados = json.load(file)

print(dados)

print(file)
print(type(dados))

valores_ordenados = []


##print('O menor valor de faturamento: ', dia, valor)
###print('O maior valor de faturamento: ', dia, valor)
####print('Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: ')