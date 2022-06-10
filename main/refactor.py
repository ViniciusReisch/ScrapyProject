import pandas as pd
import datetime


# Recebendo os valores do .json
df = pd.read_json (r'C:\Users\vinicius.reisch\PycharmProjects\pythonProject\main\main\dados.json')
precos = []
lojas = []
dic = {}
lista1 = [df]
lista = []

# Transformando os preços em float
for i in range(len(lista1[0]['Preco'])):
    x = lista1[0]['Preco'][i].replace("R$", '')
    x = x.replace(".", '')
    x = x.replace(",", ".")
    precos.append(float(x))
print(precos)
# Ordenando os nomes de loja na posição dos preços
for i in range(len(lista1[0]['Loja'])):
    lojas.append(lista1[0]['Loja'][i])

# Obtendo o menor valor
index = precos.index(min(precos))
print(f"Informação do dia {datetime.datetime.now()}"
      f"\nA loja com o produto mais barato é a {lojas[index]} com valor de {precos[index]}")

# Armazenando dados
arquivoList = (f"\nInformação do dia {datetime.datetime.now()}"
            f"\nA loja com o produto mais barato é a {lojas[index]} com valor de {precos[index]}")
arquivo = open('Data.txt', 'a', encoding="utf-8").writelines(arquivoList)

