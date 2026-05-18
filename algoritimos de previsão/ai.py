import pandas as pd                 # Manipulação de dados
import numpy as np                  # Operações numéricas
import matplotlib.pyplot as plt     # Visualização
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
 
# ==========================================
# Geração dos dados
# ==========================================
 
data = {
    'Meses': [1,2,3,4,5,6,7,8,9,10,11,12],
    'Vendas': [200,190,220,230,250,250,260,230,250,290,280,300]
}
 
# Criando DataFrame
df = pd.DataFrame(data)
 
# ==========================================
# Separação das variáveis
# ==========================================
 
X = df[['Meses']]   # Variável independente
y = df['Vendas']    # Variável dependente
 
# ==========================================
# Divisão treino/teste
# ==========================================
 
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
 
# ==========================================
# Criando e treinando o modelo
# ==========================================
 
modelo = LinearRegression()
 
modelo.fit(X_train, y_train)
 
# ==========================================
# Previsões
# ==========================================
 
y_pred = modelo.predict(X_test)
 
# ==========================================
# Visualização dos resultados
# ==========================================
 
# Ordenar para a linha ficar correta
ordem = X_test['Meses'].argsort()
 
plt.figure(figsize=(8,5))
 
# Dados reais
plt.scatter(X, y, color='blue', label='Dados reais')
 
# Linha de previsão
plt.plot(
    X_test.iloc[ordem],
    y_pred[ordem],
    color='red',
    linewidth=2,
    label='Previsão'
)
 
plt.xlabel('Meses')
plt.ylabel('Vendas')
plt.title('Regressão Linear - Previsão de Vendas')
plt.legend()
plt.grid(True)
 
plt.show()
 
# ==========================================
# Previsão para novos meses
# ==========================================
 
novos_meses = pd.DataFrame({
    'Meses': [13,14,15,16,17,18]
})
 
previsoes = modelo.predict(novos_meses)
 
print("Previsão para os novos meses:\n")
 
for mes, venda in zip(novos_meses['Meses'], previsoes):
    print(f"Mês {mes}: {venda:.2f} vendas")