#https://github.com/alura-cursos/pandas-conhecendo-a-biblioteca/blob/main/base-de-dados/aluguel.csv

import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep=";", header=0)
print(dados)

