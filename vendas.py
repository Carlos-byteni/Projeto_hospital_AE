# Importar as bibliotecas
import pandas as pd

"""
Neste código se lê um arquivo csv com dados de vendas de produtos, esses produtos são: Mesa, Sofa, Cadeira,
TV e Cama, cada um deles está associado um preço unitário e uma quantidade específica. O loop for no
código faz um percorrido por todos os items dos produtos, bem como na quantidade e no preço unitário, para
depois calcular a fatura total baseado no produto quantidad e preço unitário de cada um desses items. Finalmente
o nome do produto com a faturação total é acrescentada em um lista visualizando os valores. Depois se visualiza
os valores mais altos e mais baixos da fatura desses items.
"""

# Importar os dados do arquivo csv
dataset = pd.read_csv('Data.csv')

# Armazenar as faturas totales
valores_totais = []

# Calcular o faturamento total por produto, faz um For loop percorrendo os items de cada coluna.
for i in range(len(dataset)):
  Produto = dataset.loc[i, 'Produto']
  Quantidade = dataset.loc[i, 'Quantidade']
  Preco_Unitario = dataset.loc[i, 'Preco_Unitario']
  Fatura_Total = Quantidade * Preco_Unitario

  valores_totais.append(Fatura_Total)
  print(f'{Produto}, Fatura_Total: {Fatura_Total}')

maior_faturamento = max(valores_totais)
menor_faturamento = min(valores_totais)
print(f'\nMaior Faturamento: {maior_faturamento}')
print(f'Menor Faturamento: {menor_faturamento}')
