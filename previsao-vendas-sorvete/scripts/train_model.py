import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
import os

# Caminhos
input_path = os.path.join(os.path.dirname(__file__), '../inputs/dados_temperatura_vendas.csv')
model_path = os.path.join(os.path.dirname(__file__), '../models/model.pkl')

# Carregar dados
dados = pd.read_csv(input_path)

# Dividir variáveis independentes e dependentes
X = dados[['temperatura']]
y = dados['vendas']

# Dividir conjunto de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Salvar o modelo treinado
joblib.dump(modelo, model_path)

print("Modelo treinado e salvo em:", model_path)
