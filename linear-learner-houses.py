#carregamento da base de dados
import pandas as pd
import matplotlib.pyplot as plt
#apenas no jupter lab
#%matplotlib inline
import seaborn as sns
import numpy as np

#carregando database
base_casas = pd.read_csv('house_prices.csv')
base_casas