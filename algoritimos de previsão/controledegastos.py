# ==========================================

# CONTROLE DE GASTOS E QUITAÇÃO DE DÍVIDA

# ==========================================
 
# salário mensal

salario = 15000
 
# dívida total

divida = 100000
 
# gastos mensais

aluguel = 3500

carro = 2000

alimentacao = 2500

lazer = 1500

streaming = 300

outros = 2200
 
# ==========================================

# CALCULANDO GASTOS

# ==========================================
 
gastos_totais = (

    aluguel +

    carro +

    alimentacao +

    lazer +

    streaming +

    outros

)
 
# saldo restante

saldo = salario - gastos_totais
 
print("===== CONTROLE FINANCEIRO =====")

print(f"Salário: R$ {salario:,.2f}")

print(f"Gastos Totais: R$ {gastos_totais:,.2f}")

print(f"Saldo Mensal: R$ {saldo:,.2f}")
 
# ==========================================

# SIMULAÇÃO DE QUITAÇÃO DA DÍVIDA

# ==========================================
 
if saldo <= 0:

    print("\nVocê não possui saldo para quitar a dívida.")
 
else:
 
    meses = divida / saldo
 
    print(f"\nTempo estimado para quitar a dívida:")

    print(f"{meses:.1f} meses")
 
# ==========================================

# SIMULAÇÃO COM CORTES DE GASTOS

# ==========================================
 
print("\n===== SIMULAÇÃO COM CORTES =====")
 
# cortes planejados

novo_lazer = 500

novo_streaming = 100

novo_outros = 1200
 
# novos gastos

novos_gastos = (

    aluguel +

    carro +

    alimentacao +

    novo_lazer +

    novo_streaming +

    novo_outros

)
 
novo_saldo = salario - novos_gastos
 
novos_meses = divida / novo_saldo
 
print(f"Novo saldo mensal: R$ {novo_saldo:,.2f}")
 
print(f"Novo tempo para quitar dívida:")

print(f"{novos_meses:.1f} meses")
 
# economia obtida

economia = saldo - novo_saldo
 
print(f"\nMudança no orçamento:")

print(f"Economia mensal adicional: R$ {-economia:,.2f}")
 