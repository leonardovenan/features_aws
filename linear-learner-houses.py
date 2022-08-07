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
base_casas.columns
#o objetivo desse algoritmo é prever o preço das casas, sendo assim:
#tirando as colunas de id, data e price
X = base_casas.iloc[:, 3:19].values
y = base_casas.iloc[:, 2].values

X = np.array(X).astype('float32')
y = np.array(y).astype('float32')

#divindo base de dados para aprendizado e testes:
from sklearn.model_selection import train_test_split
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(X, y, test_size = 0.3, random_state=0)
