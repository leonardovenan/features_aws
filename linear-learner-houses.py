#carregamento da base de dados
import pandas as pd
import matplotlib.pyplot as plt
#apenas no jupter lab
#%matplotlib inline
import seaborn as sns
import numpy as np
import sagemaker
import boto3
from sagemaker import Session
import io
import sagemaker.amazon.common as smac #sagemaker common library
import os

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
#atributos previsores
X_treinamento.shape, X_teste.shape
#alvo -> previsão
y_treinamento.shape, y_teste.shape

#normalização de dados é importante.

#Configurações do SageMaker:
session = sagemaker.Session()
bucket = "nome-do-bucket"
subpasta_modelo = 'modelos/house-prices/linear-learner'
subpasta_dataset = 'datasets/houses-prices'

#buscar quais são as permissões do sagemaker
role = sagemaker.get_execution_role()
print(role)
#conversão da base de dados
buffer = io.BytesIO()
smac.write_numpy_to_dense_tensor(buffer, X_treinamento, y_treinamento) #transformação de numpy para dense que é utilizado no AWS
buffer.seek(0) #colocar a base de dados na posição inicial considerando o primeiro registro

#enviar dados de forma binária para o AWS S3
key = 'houses-train-data'
boto3.resource('s3').Bucket(bucket).Object(os.path.join(subpasta_dataset, 'train', key)).upload_fileobj(buffer)
# os.path.join(subpasta_dataset, 'train', key) -> concatenação do caminho

#caminho específico para a base de treino
s3_train_data = 's3://{}/{}/train'.format(bucket, subpasta_dataset, key)
print('Localização da base de treinamento: {}'.format(s3_train_data))

#local onde vamos salvar o modelo treinado
output_location = 's3://{}/{}/output'.format(bucket, subpasta_modelo)
print('Modelo final será salvo em: {}'.format(output_location))