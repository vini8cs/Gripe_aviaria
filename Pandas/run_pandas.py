import pandas as pd
import requests
import json
import sqlalchemy

"""url = "https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv"""""
"""dados = pd.read_csv(url, sep=";", header=0)"""

# print(dados)

# pegar informações do data frame
# print(dados.info())

# selecionar colunas específicas
"""print(dados[["Quartos", "Valor"]])"""

# calcula estatística básica dos dados
"""print(dados.describe())"""

# para ter o valor da média por Tipo apenas dos valore snuméricos
"""print(dados.groupby("Tipo").mean(numeric_only=True))"""

# Para ter o valor da média por Tipo apenas para o Valor dos imóveis. Colocar "Valor" com 2 [] retorna um dataframe e não Series:
"""print(dados.groupby("Tipo")[["Valor"]].mean())"""

# Dá também para ordernar pelos valores mais altos:
"""print(dados.groupby("Tipo")[["Valor"]].mean().sort_values("Valor"))"""

# para plot um gráfico de barras
"""dados_grafico = dados.groupby("Tipo")[["Valor"]].mean().sort_values("Valor")"""
"""dados_grafico.plot(kind='barh', figsize=(14,10), color= "purple")"""

# Método query

# Seleciona linhas a partir de parâmetros selecionados:

"""imoveis_comerciais = ['Conjunto Comercial/Sala', 
                      'Prédio Inteiro', 'Loja/Salão', 
                      'Galpão/Depósito/Armazém', 
                      'Casa Comercial', 'Terreno Padrão',
                      'Loja Shopping/ Ct Comercial',
                      'Box/Garagem', 'Chácara',
                      'Loteamento/Condomínio', 'Sítio',
                      'Pousada/Chalé', 'Hotel', 'Indústria']"""


# pode selecionar as linhas que não tem Tipo igual a itens na lista
"""print(dados.query('@imoveis_comerciais not in Tipo'))"""

# ou que tem:
"""print(dados.query('@imoveis_comerciais in Tipo'))"""

# calcular quantas vezes uma variavel aparece

"""print(dados.Tipo.value_counts())"""

# Para calcular em percentual

"""df_percentual = dados.Tipo.value_counts(normalize=True).to_frame().sort_values("Tipo")"""
"""df_percentual.plot(
    kind="bar", figsize=(14, 10), color="green", xlabel="Tipos", ylabel="Percentual"
)"""

#selecionando somente apartametos

"""print(dados.query('Tipo == "Apartamento"'))"""

#Checar onde tem dados nulos
"""print(dados.isnull())"""

#pode fazer uma soma por coluna:
"""print(dados.isnull().sum())"""

#prencher com zero os dados nulos e pode ver que a soma agora está totalmente zerada
"""dados = dados.fillna(0)"""
"""print(dados.isnull().sum())"""

#removendo linhas do data frame
"""registro_a_remover = dados.query("Valor == 0 | Condominio == 0").index #pegar os index das linhas"""
"""dados.drop(registro_a_remover, axis = 0, inplace=True) #axis = 0 indica linhas e inplace significa que as mudanças vão ser feitas diretamente ao dataframe, sem precisar especificar um novo"""

#removendo coluna
"""dados.drop("Tipo", axis = 1, inplace=True)"""

#filtrando valores em um DataFrame
"""print(dados[(dados["Valor"] < 1200) & (dados["Quartos"] == 1)])"""

"""print(dados[(dados["Valor"] > 200) & (dados["Tipo"] == "Apartamento")])"""

"""(dados[(dados["Quartos"] > 2) & (dados["Valor"] < 3000) & (dados["Area"] > 70)])"""

#juntando colunas com texto

"""dados["Descricao"] = dados["Tipo"] + " em " + dados["Bairro"] + " com " + dados["Quartos"].astype(str) + " quarto(s) e " + dados["Vagas"].astype(str) + " vaga(s) de garagem"""

"""dados["Possui suite"] = dados["Suites"].apply(lambda x: "Sim" if x > 0 else "Não")"""

##############################
#lendo os arquivos CSV
##############################

#é possível indicar quantas linhas ler no dataframe original

"""dados = pd.read_csv(url, sep=";", nrows=5)"""

#ou selecionar as colunas antes de abrir

"""dados = pd.read_csv(url, sep=";", usecols=['Tipo', 'Vagas', 'IPTU'])"""

#inclusive pelo index

"""dados = pd.read_csv(url, sep=";", usecols=[0, 3, 8])"""

#skiprows=3: indica que as três primeiras linhas do arquivo devem ser ignoradas, pois não contêm dados relevantes.
#skipfooter = 9: indica que as nove últimas linhas do arquivo devem ser ignoradas, pois não contêm dados relevantes.
#engine='python': o motor usado para ler o arquivo é o Python. Isso é necessário quando se usa o parâmetro skipfooter, pois o motor padrão não suporta essa opção.

"""dados = pd.read_csv(url, sep=";", skiprows=3, skipfooter=9, engine="python")"""

###############################
#lendo arquivos excel
###############################

# pegando o url do github com a opção ?raw=True para carregar o arquivo bruto
"""url = 'https://github.com/alura-cursos/Pandas/blob/main/emissoes_CO2.xlsx?raw=True'"""

"""dados = pd.read_excel(url)"""

#checar se tem abas dentro do excel
"""pd.ExcelFile(url).sheet_names"""

#selecionando uma planilha especifica
"""percapita = pd.read_excel(url, sheet_name="emissoes_percapita")"""

#selecionando colunas e linhas
"""emissoes = pd.read_excel(url, sheet_name="emissoes_CO2", usecols="A:D", nrows=10)"""

#####################################
###lendo dados da planilha do google
#####################################

"https://docs.google.com/spreadsheets/d/12plfm8LjAxJmyBfkIIcRZCMLwkyaSs0T/edit?usp=sharing&ouid=104831619709624827618&rtpof=true&sd=true"

#pega o id no link

"""sheet_id = '12plfm8LjAxJmyBfkIIcRZCMLwkyaSs0T'"""

#vamos acessar a API de visualização de planilhas do Google com "/gviz/tq" e retornar em formato csv com "?tqx=out:csv&sheet"

"""url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet"""""

"""dados = pd.read_csv(url, sep=",")"""

#para acessar uma planilha específica:

"""sheet_name = "emissoes_percapita"""""
"""url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"""""
"""dados = pd.read_csv(url, sep=",")"""

#####################################
###lendo arquivos em formato JSON
#####################################

""""dados =pd.read_json("pacientes.json")"""


#pode haver também dados não normalizados. Para normalizá-los, usa-se a função pd.jason_normalize() para a coluna que está aninhada,
#que no caso é a Pacientes. Para poder compará-los e manipulá-los, é preciso fazer a normalização.

#extistem várias formas de normalizar. As chaves tambpem podem estar dentro de uma lista:
"""
json_lista = [
    { 'ID': '01', 'Faixa_etaria': '55-59', 'Sexo_biologico': 'feminino'},
    { 'ID': '02', 'Faixa_etaria': '80 ou +', 'Sexo_biologico': 'feminino'}
]

dados = pd.json_normalize(json_lista)
"""

#ou dentro de um diciońario

"""
json_obj = {
    'ID': '01',
    'Faixa_etaria': '55-59',
    'Sexo_biologico': 'Feminino',
    'Saude': {'Dificuldade_caminhar': 'Nao',
              'Atividade_fisica': 'Sim',
              'IMC': 16.6,
              'Doenca_cardiaca': 'Nao',
          }
      }

dados = pd.json_normalize(json_obj)
"""

#Quando nós temos dados que estão dentro de dicionários e listas, ai já fica mais complicado,
#precisando indicar exatmente a chave que tem a lista:

"""dados_2 = pd.read_json("pacientes_2.json")"""

#ou
"""
dados_2 = {
  "Pesquisa": "Principais Indicadores de Doenca Cardiaca",
  "Ano": 2020,
  "Pacientes": [
    {
      "ID": "01",
      "Faixa_etaria": "55-59",
      "Sexo_biologico": "Feminino",
      "Raça": "Branca",
      "IMC": 16.6,
      "Fumante": "Sim",
      "Consumo_alcool": "Nao",
      "Saude_fisica": 3,
      "Saude_mental": 30,
      "Dificuldade_caminhar": "Nao",
      "Atividade_fisica": "Sim",
      "Saude_geral": "Muito boa",
      "Horas_sono": 5,
      "Problemas_saude": [
        "Diabetes",
        "Asma",
        "Cancer_pele"
      ]
    },
    {
      "ID": "02",
      "Faixa_etaria": "80 ou +",
      "Sexo_biologico": "Feminino",
      "Raça": "Branca",
      "IMC": 20.34,
      "Fumante": "Nao",
      "Consumo_alcool": "Nao",
      "Saude_fisica": 0,
      "Saude_mental": 0,
      "Dificuldade_caminhar": "Nao",
      "Atividade_fisica": "Sim",
      "Saude_geral": "Muito boa",
      "Horas_sono": 7,
      "Problemas_saude": [
        "AVC"
      ]
    },
    {
      "ID": "03",
      "Faixa_etaria": "65-69",
      "Sexo_biologico": "Masculino",
      "Raça": "Branca",
      "IMC": 26.58,
      "Fumante": "Sim",
      "Consumo_alcool": "Nao",
      "Saude_fisica": 20,
      "Saude_mental": 30,
      "Dificuldade_caminhar": "Nao",
      "Atividade_fisica": "Sim",
      "Saude_geral": "Muito boa",
      "Horas_sono": 8,
      "Problemas_saude": [
        "diabetes",
        "Asma"
      ]
    }
  ]
}

"""

"""dados_2_normalizados = pd.json_normalize(dados_2["Pacientes"])"""

#ou

"""dados_2_normalizados = pd.json_normalize(dados_2, record_path=['Pacientes'])"""


#Mas agora percebe-se que os valores fora de Paciente (Ano, Pesquisa) sumiram. Para mantê-los,
#usa-se o argumento "meta"

"""dados_2_normalizados = pd.json_normalize(dados_2, record_path=['Pacientes'], meta=['Pesquisa', 'Ano'])"""

#para salvar:

"""dados_2_normalizados.to_json("pacientes2_normalizado.json")"""
#pode salvar também em excel, csv ou qualquer outr formato que vc quiser também

"""
API

APIs web são os mais comuns. Faz a interface entre o usuário e sofwtare. O usuário faz uma
requisição à API e obtém um resultado. A API é responsável por processar essa requisição e retornar um
resultado ao usuário.

Padrões de API Web:

RPC -> chama uma função no destino. 
Soap -> fornececia um protocolo para trabalhar com RPC. Definia o formato de uma requisição utilizando XLM definindo as funções, parâmtros, etc. Mas o formato é muito grande
REST (mais utilizado) -> vai usar o HTTP como foi pensando usando GET, POST, etc
"""


#É possível também ler os arquivos json com o json.loads:

"""
dados_frutas = requests.get('https://fruityvice.com/api/fruit/all')

with open("file_frutas.json", "wb") as f:
    f.write(dados_frutas.content)

with open("file_frutas.json",'r') as f:
    resultado = json.loads(f.read())    
"""

#ou

"""resultado = json.loads(dados_frutas.text)"""

#normalize

"""dados_normalizados = pd.json_normalize(resultado)"""

#####################################
###lendo arquivos em formato HTML
#####################################

"""data = pd.read_html("filmes_wikipedia.html")"""

#gera uma lista. Para poder então pegar o data frame, precisar usar o index [1]

"""top_filmes = data[1]"""

#criar um html

"""top_filmes.to_html("top_files.html")"""
"""top_filmes.to_csv("top_files.csv")"""

#####################################
###lendo arquivos em formato XML
#####################################

"""dados_imdb = pd.read_xml("imdb_top_1000.xml")"""




#####################################
###ANalisando banco de dados com sqlalchemy
#####################################
import sqlalchemy

from sqlalchemy import create_engine, MetaData, Table, inspect
#create_engine -> vai fazer o banco de dados funcioncar;
#MetaData: representa a classe dos nossos metadatos, incluindo informações sobre tabelas e outros obrjetos
#Table: manipular dados em tabelas;
#inspect: inspecionar a estrutura do banco de dados, incluindo tabela e outros objetivos

"""engine = create_engine("sqlite:///:memory:")""" #banco de dados sqlite sendo instalado na memória


#Existem bancos de dados relacionais e não-relacionais. Os bancos de dados relacionais representam e armazenam dados em tabelas. Já os não-relacionais, também conhecidos como bancos de dados NoSQL (Not Only SQL - Não SQL), usam uma variedade de estruturas de dados, como documentos, grafos ou pares de chave-valor.

#Python oferece vários pacotes e bibliotecas para trabalhar com bancos de dados, incluindo SQLite, MySQL, PostgreSQL, Oracle, MongoDB, entre outros. Um dos pacotes mais comuns usados para trabalhar com bancos de dados relacionais em Python é o pacote sqlite3 que oferece suporte a bancos de dados SQLite. Este banco de dados é leve e incorporado que não exige um servidor separado para ser executado que já vem nativamente instalado no Google Colab.

#Para trabalhar com esse banco podemos utilizar a SQLAlchemy, uma biblioteca de mapeamento objeto-relacional (ORM), que possibilita interagir com bancos de dados relacionais usando código Python. Ela fornece uma camada de abstração que permite aos desenvolvedores trabalhar com objetos Python em vez de lidar diretamente com as complexidades da linguagem SQL (Structured Query Language - Linguagem de consulta estruturada).

#Uma das principais vantagens do uso de SQLAchemy é a capacidade de criar código mais legível e fácil de manter. Com SQLAlchemy, as operações do banco de dados são executadas usando métodos em objetos Python, tornando o código mais claro e menos propenso a erros.

#Além disso, a SQLAlchemy oferece suporte a consultas complexas em bancos de dados, permitindo que pessoas desenvolvedoras extraiam facilmente informações relevantes de grandes conjuntos de dados. Isso é especialmente útil em aplicações que precisam lidar com grandes quantidades de dados.


'''url = "https://raw.githubusercontent.com/alura-cursos/Pandas/main/clientes_banco.csv"'''
'''dados = pd.read_csv(url)'''


#criando um arquivo sql
'''dados.to_sql("clientes", engine, index = False)'''

#pra checar que nosso banco foi criado, a gente usa o inspect para checar nosso engine

'''inspector = inspect(engine)'''
'''inspector.get_table_names()''' #devolve os nomes das tableas dentro do banco de dados

#As instruções SQL podem ser compostas por uma ou mais cláusulas que fornecem 
#informações adicionais sobre o que a consulta deve fazer. As cláusulas mais comuns são:

#SELECT: especifica quais colunas devem ser selecionadas na consulta.
#FROM: especifica as tabelas do banco de dados que devem ser consultadas.
#WHERE: filtra os resultados da consulta com base em uma ou mais condições especificadas.
#ORDER BY: classifica os resultados da consulta em ordem crescente ou decrescente com base em uma ou mais colunas.
#GROUP BY: agrupa os resultados da consulta com base em uma ou mais colunas.
#LIMIT: limita o número de linhas retornadas pelos resultados da consulta.

#uma consulta em sql sempre é chamada de query:

#SELECT é comando para relecionar quais colunas enquanto que * indica que retorne
# todas as colunas da tabela;

#FROM indica qual tabela estamos analisando

#WHERE seria o obejto para filtrar, que nesse caso, seria todas as linhas da Cateforia_de_renda
#que tem valor igual à Empregado. A função read_sql da biblioteca Pandas do Python é utilizada para executar uma consulta SQL em um banco de dados e 
#retornar os resultados em um objeto DataFrame.

'''query = "SELECT * FROM clientes WHERE Categoria_de_renda='Empregado'"'''
'''empregados = pd.read_sql(query, engine)'''

#para adicionar essa nova tabela no nosso engine:

'''empregados.to_sql("empregados", engine, index=False)'''

"""inspector = inspect(engine)"""
"""print(inspector.get_table_names())"""

#você também pode ler uma tabela específica. A função read_sql_table é usada para carregar dados diretamente de uma tabela existente no banco de dados

'''empregados = pd.read_sql_table("empregados", engine)'''

#Atulizando banco de dados. Digamos que queremos remover o cliente ID 5008804. Para fazer isso:

'''query = "DELETE FROM clientes WHERE ID_Cliente='5008804'"'''
#para garantir que vamos fechar direitinho nosso banco de dados deppis de usar. Ele vai executar
#nossa query diretamente no banco de dados:
'''
with engine.connect() as conn:
  conn.execute(query)
'''
#e o primeiro cliente se foi
'''pd.read_sql_table("clientes", engine)'''

#para atualizar agora utiliamos UPDATE tabela SET coluna='novo valor' WHERE coluna_lead='nome_da_coluna'  :
'''
query = "UPDATE clientes SET Grau_escolaridade='Ensino superior' WHERE ID_Cliente='5008808'"
with engine.connect() as conn:
    conn.execute(query)

print(pd.read_sql_table("clientes", engine))
'''


###Fazendo teste####

engine = create_engine("sqlite:///:memory:")

url = "https://raw.githubusercontent.com/alura-cursos/Pandas/main/clientes_banco.csv"
dados = pd.read_csv(url)

dados.to_sql("data", engine, index=False)
inpection = inspect(engine)
print(inpection.get_table_names())


dados = pd.read_sql("data", engine)

query = "UPDATE data SET Rendimento_anual='300000' WHERE ID_Cliente='6840104'"
with engine.connect() as conn:
    conn.execute(query)

dados = pd.read_sql("data", engine)
#print(dados.query('ID_Cliente==6840104'))

#print(dados[(dados["Rendimento_anual"] >= 300000) & (dados["Tem_carro"] == 0)])

#print(dados[(dados["Grau_escolaridade"] == "Ensino superior") & (dados["Idade"] >= 25) & (dados["Rendimento_anual"] > 4000)])

print(dados.query("ID_Cliente == 5008809"))

query = "DELETE FROM data WHERE ID_Cliente='5008809'"
with engine.connect() as conn:
    conn.execute(query)

dados = pd.read_sql_table("data", engine)
print(dados.query("ID_Cliente == 5008809"))

#Para adicionar um novo cliente, utiliza-se a opção INSERT INTO tabela (nome das colunas) VALUES (novos valores)

query = 'INSERT INTO data (ID_Cliente, Idade, Grau_escolaridade, Estado_civil, ' \
        'Tamanho_familia, Categoria_de_renda, Ocupacao, Anos_empregado, ' \
        'Rendimento_anual, Tem_carro, Moradia) ' \
        'VALUES (6850985, 33, "Doutorado", "Solteiro", 1, "Empregado", "TI", ' \
        '2, 290000, 0, "Casa/apartamento próprio")'

with engine.connect() as conn:
    conn.execute(query)

dados = pd.read_sql_table("data", engine)
print(dados.query("ID_Cliente==6850985"))
