# algoritimo de previsão de vendas
este projeto tem como finalidade a previsão de vendas utilizando algotitimos como arvore de desisão, analizando datas anteriores e vendas efetuadas e as comparando
# 📊 Previsão de Vendas com Machine Learning

Projeto de análise e previsão de vendas utilizando algoritmos de Machine Learning (Árvore de Decisão e Rede Neural).

## 🎯 Objetivo

Desenvolver modelos preditivos para estimar vendas futuras com base em dados históricos mensais, comparando a performance de diferentes algoritmos de aprendizado de máquina.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Pandas** - Manipulação e análise de dados
- **NumPy** - Operações com arrays e computação numérica
- **Scikit-learn** - Algoritmos de Machine Learning
- **Matplotlib** - Visualização de dados

## 📦 Instalação

### 1. Clone o repositório (ou baixe os arquivos)

```bash
git clone <url-do-repositorio>
cd <nome-do-projeto>
```

### 2. Crie um ambiente virtual (recomendado)

```bash
python -m venv .venv
```

### 3. Ative o ambiente virtual

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install pandas numpy scikit-learn matplotlib
```

## 📁 Estrutura do Projeto

```
projeto/
│
├── exercicio_arvore.py      # Modelo com Árvore de Decisão
├── exercicio_rede_neural.py # Modelo com Rede Neural
├── README.md                # Documentação do projeto
└── .venv/                   # Ambiente virtual (criado após instalação)
```

## 🚀 Como Usar

### Modelo com Árvore de Decisão

```bash
python exercicio_arvore.py
```

### Modelo com Rede Neural

```bash
python exercicio_rede_neural.py
```

## 📊 Conjunto de Dados

O projeto utiliza um dataset fictício com 24 meses de dados de vendas:

- **Período:** Janeiro/2025 a Dezembro/2026
- **Frequência:** Mensal (final de cada mês)
- **Variável preditora:** Mês do ano (1-12)
- **Variável alvo:** Volume de vendas

### Exemplo de dados:

| Data       | Vendas | Mês |
|------------|--------|-----|
| 2025-01-31 | 200    | 1   |
| 2025-02-28 | 220    | 2   |
| 2025-03-31 | 210    | 3   |
| ...        | ...    | ... |

## 🤖 Modelos Implementados

### 1. Árvore de Decisão (Decision Tree Regressor)

**Características:**
- Modelo não-linear
- Simples e interpretável
- Adequado para capturar padrões complexos

**Configuração:**
```python
DecisionTreeRegressor(random_state=42)
```

### 2. Rede Neural (MLP Regressor)

**Características:**
- Modelo de aprendizado profundo
- 1 camada oculta com 50 neurônios
- Função de ativação ReLU

**Configuração:**
```python
MLPRegressor(
    hidden_layer_sizes=(50,),
    activation='relu',
    solver='adam',
    max_iter=1000,
    random_state=42
)
```

## 📈 Avaliação dos Modelos

Ambos os modelos são avaliados usando **MSE (Mean Squared Error - Erro Quadrático Médio)**:

- Quanto **menor** o MSE, **melhor** o modelo
- MSE = 0 indica previsões perfeitas

### Divisão dos Dados

- **70%** para treinamento
- **30%** para teste
- `random_state=42` para reprodutibilidade

## 📉 Visualizações

Cada modelo gera um gráfico mostrando:

- **Pontos azuis:** Dados reais completos
- **Pontos vermelhos:** Dados de teste (30%)
- **Linha verde tracejada:** Previsões do modelo

## 🔧 Personalização

### Modificar o conjunto de dados

Edite a seção de criação de arrays no código:

```python
# Arrays manuais com NumPy
datas = np.array([
    '2025-01-31', '2025-02-28', ...
], dtype='datetime64[D]')

vendas = np.array([
    200, 220, 210, ...
])
```

### Ajustar parâmetros dos modelos

**Árvore de Decisão:**
```python
modelo_tree = DecisionTreeRegressor(
    max_depth=5,           # Profundidade máxima
    min_samples_split=2,   # Mínimo de amostras para dividir
    random_state=42
)
```

**Rede Neural:**
```python
modelo_nn = MLPRegressor(
    hidden_layer_sizes=(100, 50),  # Múltiplas camadas
    activation='relu',
    learning_rate_init=0.001,      # Taxa de aprendizado
    max_iter=2000,
    random_state=42
)
```

## 📚 Conceitos Importantes

### Arrays vs Listas

- **Lista Python:** `[200, 220, 210]` - Estrutura básica
- **Array NumPy:** `np.array([200, 220, 210])` - Otimizado para cálculos numéricos
- **DatetimeIndex:** Array especial do pandas para datas

### Frequências de Datas (freq)

- `'D'` - Diário
- `'W'` - Semanal
- `'MS'` - Início do mês (Month Start)
- `'ME'` - Final do mês (Month End)
- `'QE'` - Final do trimestre
- `'YE'` - Final do ano

## ⚠️ Problemas Comuns

### Erro: "All arrays must be of the same length"

**Causa:** Arrays com tamanhos diferentes no dicionário de dados.

**Solução:** Certifique-se de que todos os arrays têm o mesmo número de elementos:

```python
len(datas)   # Deve retornar 24
len(vendas)  # Deve retornar 24
```

### Erro: "'M' is no longer supported"

**Causa:** Versão antiga do código usando `freq='M'`.

**Solução:** Use `freq='ME'` para final do mês.

### Erro: "sklearn not found"

**Causa:** Pacote instalado incorretamente.

**Solução:** 
```bash
pip install scikit-learn  # NÃO use 'sklearn'
```

## 🎓 Aprendizados do Projeto

1. **Manipulação de dados temporais** com Pandas
2. **Criação de arrays** com NumPy
3. **Divisão de dados** para treino e teste
4. **Treinamento de modelos** de Machine Learning
5. **Avaliação de performance** com métricas
6. **Visualização de resultados** com Matplotlib

## 📝 Próximos Passos

- [ ] Adicionar mais variáveis preditoras (sazonalidade, promoções, etc.)
- [ ] Implementar validação cruzada
- [ ] Comparar com modelos de séries temporais (ARIMA, Prophet)
- [ ] Criar pipeline de preprocessamento
- [ ] Exportar modelos treinados
- [ ] Desenvolver interface web para previsões

## 👤 Autor

**Gabriel**

## 📄 Licença

Este projeto é de código aberto e está disponível para fins educacionais.

---

⭐ **Dica:** Para melhores resultados, utilize dados reais de vendas da sua empresa ou organização!