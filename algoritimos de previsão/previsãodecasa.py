# ==========================================
# PREVISÃO DE PREÇO DE CASAS COM IA
# ==========================================
 
# Bibliotecas
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
 
# ==========================================
# BASE DE DADOS
# ==========================================
 
dados = {
    'metragem': [50, 60, 80, 100, 120, 150, 200],
    'bairro': ['Centro', 'Centro', 'Bairro A', 'Bairro A',
                'Bairro B', 'Bairro B', 'Centro'],
    'idade': [20, 15, 10, 8, 5, 2, 1],
    'preco': [200000, 250000, 320000, 400000,
              500000, 650000, 800000]
}
 
# Criando DataFrame
df = pd.DataFrame(dados)
 
print("BASE DE DADOS")
print(df)
 
# ==========================================
# TRANSFORMANDO TEXTO EM NÚMEROS
# ==========================================
 
encoder = LabelEncoder()
 
df['bairro'] = encoder.fit_transform(df['bairro'])
 
print("\nBAIRROS CONVERTIDOS")
print(df)
 
# ==========================================
# DEFININDO ENTRADAS E SAÍDA
# ==========================================
 
X = df[['metragem', 'bairro', 'idade']]
 
y = df['preco']
 
# ==========================================
# DIVIDINDO DADOS
# ==========================================
 
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.2, random_state=42
)
 
# ==========================================
# CRIANDO O MODELO
# ==========================================
 
modelo = LinearRegression()
 
# Treinando IA
modelo.fit(X_treino, y_treino)
 
# ==========================================
# TESTANDO O MODELO
# ==========================================
 
previsoes = modelo.predict(X_teste)
 
print("\nPREVISÕES")
print(previsoes)
 
# ==========================================
# PREVENDO NOVA CASA
# ==========================================
 
# Casa:
# 130 m²
# Bairro B
# 3 anos
 
bairro_novo = encoder.transform(['Bairro B'])[0]
 
nova_casa = [[130, bairro_novo, 3]]
 
preco_previsto = modelo.predict(nova_casa)
 
print("\nPREÇO PREVISTO:")
print(f"R$ {preco_previsto[0]:,.2f}")