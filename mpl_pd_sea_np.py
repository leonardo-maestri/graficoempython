import numpy as np
import pandas as pd
import matplotlib as mat
import matplotlib.pyplot as plt
import seaborn as sea

np.random.seed(42)

# Número de amostras
n = 1000
pct_smokers = 0.2

# Gerar dados aleatórios, com altura e peso sendo arredondados para 2 casas decimais
flag_fumante = np.random.rand(n) < pct_smokers
idade = np.random.normal(40, 10, n)
altura = np.random.normal(170, 10, n)
peso = np.random.normal(70, 10, n)
altura = np.round(altura, 2)
peso = np.round(peso, 2)

# Criar DF com os dados 
dados = pd.DataFrame({'altura': altura, 'peso': peso, 'flag_fumante': flag_fumante})
dados['flag_fumante'] = dados['flag_fumante'].map({True: 'Fumante', False: 'Não Fumante'})

# Definir o estilo do Seaborn
sea.set(style="ticks")

# Criar o gráfico de dispersão com ajuste de regressão linear
sea.lmplot(x='altura', y='peso', data=dados, hue='flag_fumante', palette=['tab:blue', 'tab:orange'], height=7)

# Definir rótulos e título
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.title('Relação entre Altura e Peso de Fumantes e Não Fumantes')

# Remover as bordas superiores e direita
sea.despine()

# Mostrar o gráfico
plt.show()
# grafico resultante está no readme
