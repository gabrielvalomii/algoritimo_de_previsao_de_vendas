# # ==========================================================
# # Atividade Avaliativa 03 - Engenharia da Computação
# # Simulação de Investimentos Financeiros
# # Autor: Seu Nome
# # ==========================================================

# # Meta financeira
# meta = 100000.00

# # Aporte mensal
# aporte_mensal = 1000.00

# # Dicionário contendo as modalidades de investimento
# # e suas respectivas taxas médias anuais de rentabilidade
# investimentos = {
#     "Poupança": 0.06,       # 6% ao ano
#     "Tesouro Selic": 0.10,  # 10% ao ano
#     "CDB": 0.12,            # 12% ao ano
#     "Ações": 0.15           # 15% ao ano
# }

# print("=" * 65)
# print("SIMULAÇÃO DE INVESTIMENTOS FINANCEIROS")
# print("=" * 65)
# print(f"Meta financeira: R$ {meta:,.2f}")
# print(f"Aporte mensal : R$ {aporte_mensal:,.2f}")
# print("=" * 65)

# # Percorre cada modalidade de investimento
# for nome, taxa_anual in investimentos.items():

#     saldo = 0
#     meses = 0

#     # Conversão da taxa anual para taxa mensal
#     taxa_mensal = (1 + taxa_anual) ** (1/12) - 1

#     # Simulação com juros compostos
#     while saldo < meta:
#         saldo = saldo * (1 + taxa_mensal) + aporte_mensal
#         meses += 1

#     # Conversão do tempo para anos e meses
#     anos = meses // 12
#     meses_restantes = meses % 12

#     # Exibição dos resultados
#     print(f"\nModalidade: {nome}")
#     print(f"Taxa anual: {taxa_anual * 100:.1f}%")
#     print(f"Tempo para atingir a meta: {anos} anos e {meses_restantes} meses")
#     print(f"Saldo acumulado final: R$ {saldo:,.2f}")

# print("\n" + "=" * 65)
# print("Fim da simulação")
# print("=" * 65)

# ==========================================================
# ATIVIDADE AVALIATIVA 03
# Engenharia da Computação
# Simulação de Investimentos com Rede Neural Artificial
# ==========================================================

import numpy as np
from sklearn.neural_network import MLPRegressor

# ----------------------------------------------------------
# Função para calcular quantos meses são necessários
# para atingir a meta utilizando juros compostos.
# ----------------------------------------------------------
def calcular_meses(taxa_anual, aporte=1000, meta=100000):

    saldo = 0
    meses = 0

    taxa_mensal = (1 + taxa_anual) ** (1/12) - 1

    while saldo < meta:
        saldo = saldo * (1 + taxa_mensal) + aporte
        meses += 1

    return meses


# ----------------------------------------------------------
# GERAÇÃO DOS DADOS DE TREINAMENTO
# ----------------------------------------------------------

X = []
y = []

# Taxas de 1% até 20% ao ano
for taxa in np.arange(0.01, 0.21, 0.001):

    meses = calcular_meses(taxa)

    X.append([taxa])
    y.append(meses)

X = np.array(X)
y = np.array(y)

# ----------------------------------------------------------
# CRIAÇÃO E TREINAMENTO DA REDE NEURAL
# ----------------------------------------------------------

rede = MLPRegressor(
    hidden_layer_sizes=(20, 10),
    activation='relu',
    solver='adam',
    max_iter=5000,
    random_state=42
)

rede.fit(X, y)

# ----------------------------------------------------------
# INVESTIMENTOS A SEREM ANALISADOS
# ----------------------------------------------------------

investimentos = {
    "Poupança": 0.06,
    "Tesouro Selic": 0.10,
    "CDB": 0.12,
    "Ações": 0.15
}

print("=" * 70)
print("SIMULAÇÃO DE INVESTIMENTOS UTILIZANDO REDE NEURAL")
print("=" * 70)

meta = 100000
aporte = 1000

for nome, taxa in investimentos.items():

    # Previsão feita pela IA
    meses_previstos = round(
        rede.predict([[taxa]])[0]
    )

    anos = meses_previstos // 12
    meses_restantes = meses_previstos % 12

    # Cálculo do saldo usando o tempo previsto
    saldo = 0
    taxa_mensal = (1 + taxa) ** (1/12) - 1

    for _ in range(meses_previstos):
        saldo = saldo * (1 + taxa_mensal) + aporte

    print(f"\nInvestimento: {nome}")
    print(f"Taxa anual: {taxa * 100:.2f}%")
    print(f"Tempo previsto pela IA: "
          f"{anos} anos e {meses_restantes} meses")
    print(f"Saldo estimado: R$ {saldo:,.2f}")

print("\n" + "=" * 70)
print("Fim da Simulação")
print("=" * 70)