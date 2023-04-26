##4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
##
##SP – R$67.836,43
##RJ – R$36.678,66
##MG – R$29.229,88
##ES – R$27.165,48
##Outros – R$19.849,53

##Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado 
##teve dentro do valor total mensal da distribuidora.
import json

dados_faturamento = []

with open("dados.json") as file:
    dados_faturamento = json.load(file)

total_mensal = 0
array_percentuais = []

for dados_estado in dados_faturamento:
    total_mensal += float(dados_estado["Faturamento"])

array_faturamentos = []

for i in range(len(dados_faturamento)):
    estado_atual = dados_faturamento[i]["Estado"]
    faturamento_atual = dados_faturamento[i]["Faturamento"]
    percentual_atual = (float(faturamento_atual) / total_mensal) * 100
    print(f"{estado_atual} - {percentual_atual:.2f} %")

