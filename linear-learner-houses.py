#carregamento da base de dados
import pandas as pd
import matplotlib.pyplot as plt
#apenas no jupter lab
#%matplotlib inline
import seaborn as sns
import numpy as np

#carregando database
base_casas = pd.read_csv('house_prices.csv')
#visualização geral dos dados
base_casas
#apenas colunas
base_casas.columns
#estatisticas gerais em relação aos dados
base_casas.describe()
#tratamento de colunas nulas
base_casas.isnull().sum()

#VISUALIZAÇÃO DOS DADOS
#correlão de um atribuito com os outros, bem importante para problemas de regressão
#quanto mais próximo de 1 mais correção existe
base_casas.corr()

figura = plt.figure(figsize=(20,20))
sns.heatmap(base_casas.corr(), annot=True);

#Pré-Processamento dos dados

