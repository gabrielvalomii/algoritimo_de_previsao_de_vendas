import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# ------------------------
# Conjunto de dados fictício - CRIANDO ARRAYS MANUALMENTE COM NUMPY
# ------------------------
# Criando array de datas manualmente
datas = np.array([
    '2025-01-31', '2025-02-28', '2025-03-31', '2025-04-30', 
    '2025-05-31', '2025-06-30', '2025-07-31', '2025-08-31',
    '2025-09-30', '2025-10-31', '2025-11-30', '2025-12-31',
    '2026-01-31', '2026-02-28', '2026-03-31', '2026-04-30',
    '2026-05-31', '2026-06-30', '2026-07-31', '2026-08-31',
    '2026-09-30', '2026-10-31', '2026-11-30', '2026-12-31'
], dtype='datetime64[D]')  # Array numpy de datas

# Criando array de vendas manualmente
vendas = np.array([
    200, 220, 210, 230, 250, 260, 240, 270, 290, 300, 310, 330, 
    340, 360, 370, 380, 400, 390, 410, 420, 430, 450, 460, 480
])  # Array numpy de números

# Agora criamos o dicionário com arrays numpy
dados = {
    'data': datas,
    'vendas': vendas
}

# Criando o DataFrame (agora a partir de arrays numpy)
df = pd.DataFrame(dados)

# Extraindo características (mês) e target (vendas)
df['mes'] = pd.to_datetime(df['data']).dt.month  # Mês da venda
X = df[['mes']]
y = df['vendas']

# ------------------------
# Divisão entre treino e teste
# ------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# ------------------------
# Modelo: Rede Neural Simples
# ------------------------
modelo_nn = MLPRegressor(
    hidden_layer_sizes=(50,), 
    activation='relu', 
    solver='adam', 
    max_iter=1000, 
    random_state=42
)
modelo_nn.fit(X_train, y_train)

# ------------------------
# Predição
# ------------------------
y_pred_nn = modelo_nn.predict(X_test)

# ------------------------
# Avaliação
# ------------------------
mse_nn = mean_squared_error(y_test, y_pred_nn)
print(f"MSE Rede Neural Simples: {mse_nn:.2f}")

# ------------------------
# Visualização (CORRIGIDA)
# ------------------------
# Criar DataFrame ordenado para visualização correta
test_df = pd.DataFrame({
    'mes': X_test['mes'].values,
    'y_test': y_test.values,
    'y_pred': y_pred_nn
}).sort_values('mes')

plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Dados Reais', alpha=0.6, s=50)
plt.scatter(test_df['mes'], test_df['y_test'], color='red', label='Teste Real', s=100, zorder=5)
plt.plot(test_df['mes'], test_df['y_pred'], 'g--', linewidth=2, label='Previsão Rede Neural')
plt.title('Previsão de Vendas com Rede Neural Simples')
plt.xlabel('Mês')
plt.ylabel('Vendas')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()