import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# ------------------------
# Conjunto de dados fictício
# ------------------------
dados = {
    'data': pd.date_range(start='2025-01-01', periods=24, freq='ME'),
    'vendas': [200, 220, 210, 230, 250, 260, 240, 270, 290, 300, 310, 330, 
               340, 360, 370, 380, 400, 390, 410, 420, 430, 450, 460, 480],
}

# Criando o DataFrame
df = pd.DataFrame(dados)

# Extraindo características (mês) e target (vendas)
df['mes'] = df['data'].dt.month
X = df[['mes']]
y = df['vendas']

# ------------------------
# Divisão entre treino e teste
# ------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# ------------------------
# Modelo: Árvore de Decisão
# ------------------------
modelo_tree = DecisionTreeRegressor()
modelo_tree.fit(X_train, y_train)

# ------------------------
# Predição
# ------------------------
y_pred_tree = modelo_tree.predict(X_test)

# ------------------------
# Avaliação
# ------------------------
mse_tree = mean_squared_error(y_test, y_pred_tree)
print(f"MSE Árvore de Decisão: {mse_tree:.2f}")

# ------------------------
# Visualização
# ------------------------
# Criar um DataFrame para ordenar os dados de teste
test_df = pd.DataFrame({
    'mes': X_test['mes'].values,
    'y_test': y_test.values,
    'y_pred': y_pred_tree
}).sort_values('mes')

plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Dados Reais', alpha=0.6)
plt.scatter(test_df['mes'], test_df['y_test'], color='red', label='Teste Real', s=100)
plt.plot(test_df['mes'], test_df['y_pred'], 'g--', linewidth=2, label='Previsão Árvore')
plt.title('Previsão de Vendas com Árvore de Decisão')
plt.xlabel('Mês')
plt.ylabel('Vendas')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()