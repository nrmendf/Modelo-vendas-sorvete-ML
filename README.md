Previsão de Vendas de Sorvete com Machine Learning 🍦

📁 Projeto: Gelato Mágico

Este projeto tem como objetivo prever a quantidade de vendas de sorvete com base na temperatura ambiente de uma cidade litorânea. A previsão precisa auxilia na tomada de decisões para otimizar a produção, reduzir desperdícios e maximizar os lucros da sorveteria Gelato Mágico.

🔥 Motivação

A correlação entre a temperatura e as vendas de sorvete é evidente. Em dias mais quentes, a demanda aumenta, enquanto em dias frios há uma queda nas vendas. Usando técnicas de Machine Learning, é possível criar um modelo de regressão para antecipar a demanda e planejar a produção de forma mais precisa.

🛠️ Tecnologias Utilizadas

Python

Pandas

Scikit-Learn

Joblib

📂 Estrutura do Projeto

📦 Gelato Magico
├── inputs
│   └── dados_temperatura_vendas.csv
├── models
│   └── modelo_vendas.pkl
├── train_model.py
└── README.md

inputs: Contém o arquivo de dados dados_temperatura_vendas.csv com temperatura e vendas.

models: Contém o modelo treinado modelo_vendas.pkl.

train_model.py: Script para treinar o modelo de regressão linear.

🚀 Como Executar o Projeto

1. Clone o Repositório

git clone https://github.com/seu_usuario/gelato-magico.git
cd gelato-magico

2. Instale as Dependências

Certifique-se de ter o Python instalado e rode o comando:

pip install pandas scikit-learn joblib

3. Treine o Modelo

Execute o script train_model.py:

python train_model.py

O modelo treinado será salvo na pasta models como modelo_vendas.pkl.

🔎 Resultados e Insights

A correlação positiva entre temperatura e vendas confirma a relação esperada.

O modelo de regressão linear simples apresentou um desempenho adequado para previsões iniciais.
