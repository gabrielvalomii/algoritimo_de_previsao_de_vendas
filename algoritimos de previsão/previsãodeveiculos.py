# ==========================================

# PREVISÃO DE PREÇO DE VEÍCULOS 

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

    'marca': [

        'Toyota', 'Honda', 'Ford', 'Chevrolet',

        'Toyota', 'Honda', 'Ford', 'Chevrolet'

    ],
 
    'modelo': [

        'Corolla', 'Civic', 'Focus', 'Onix',

        'Hilux', 'HRV', 'Ranger', 'Cruze'

    ],
 
    'ano': [

        2018, 2019, 2017, 2020,

        2021, 2022, 2020, 2019

    ],
 
    'quilometragem': [

        50000, 40000, 70000, 30000,

        20000, 15000, 35000, 45000

    ],
 
    'pintura': [

        'Boa', 'Excelente', 'Regular', 'Excelente',

        'Excelente', 'Excelente', 'Boa', 'Regular'

    ],
 
    'preco': [

        85000, 95000, 70000, 80000,

        180000, 140000, 160000, 90000

    ]

}
 
# Criando DataFrame

df = pd.DataFrame(dados)
 
print("BASE DE DADOS")

print(df)
 
# ==========================================

# CONVERTENDO TEXTO EM NÚMEROS

# ==========================================
 
encoder_marca = LabelEncoder()

encoder_modelo = LabelEncoder()

encoder_pintura = LabelEncoder()
 
df['marca'] = encoder_marca.fit_transform(df['marca'])

df['modelo'] = encoder_modelo.fit_transform(df['modelo'])

df['pintura'] = encoder_pintura.fit_transform(df['pintura'])
 
print("\nDADOS TRATADOS")

print(df)
 
# ==========================================

# DEFININDO ENTRADAS E SAÍDA

# ==========================================
 
X = df[['marca', 'modelo', 'ano',

        'quilometragem', 'pintura']]
 
y = df['preco']
 
# ==========================================

# DIVIDINDO DADOS

# ==========================================
 
X_treino, X_teste, y_treino, y_teste = train_test_split(

    X,

    y,

    test_size=0.2,

    random_state=42

)
 
# ==========================================

# CRIANDO O MODELO DE IA

# ==========================================
 
modelo = LinearRegression()
 
# Treinando o modelo

modelo.fit(X_treino, y_treino)
 
# ==========================================

# TESTANDO O MODELO

# ==========================================
 
previsoes = modelo.predict(X_teste)
 
print("\nPREVISÕES")

print(previsoes)
 
# ==========================================

# PREVENDO NOVO VEÍCULO

# ==========================================
 
# Dados do veículo:

# Toyota Corolla 2020

# 25.000 km

# Pintura Excelente
 
marca_nova = encoder_marca.transform(['Toyota'])[0]

modelo_novo = encoder_modelo.transform(['Corolla'])[0]

pintura_nova = encoder_pintura.transform(['Excelente'])[0]
 
novo_veiculo = [[

    marca_nova,

    modelo_novo,

    2020,

    25000,

    pintura_nova

]]
 
preco_previsto = modelo.predict(novo_veiculo)
 
print("\nPREÇO PREVISTO DO VEÍCULO:")

print(f"R$ {preco_previsto[0]:,.2f}")
 