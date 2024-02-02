import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('tiempos.csv')
filtered = df.groupby(["programa", "ejemplo"])["tiempo"].mean()

prueba = filtered.reset_index()

prueba['tiempo'] = prueba['tiempo'].round(4)

prueba = prueba.sort_values(by="ejemplo")

prueba = prueba.pivot(index='ejemplo', columns='programa', values='tiempo')

prueba = prueba.reset_index()

prueba = prueba[['ejemplo', 'prolog', 'python', 'optimized']]

prueba = prueba.replace(120.0, 0.0)

print(prueba)



prueba.to_csv('filtrado.txt', index=False)


sns.set(style='whitegrid')

prolog_without_timeout = prueba[prueba['prolog'] != 0.0]
sns.scatterplot(x='ejemplo', y='prolog', data=prolog_without_timeout, label='prolog')

python_without_timeout = prueba[prueba['python'] != 0.0]
sns.scatterplot(x='ejemplo', y='python', data=python_without_timeout, label='python')

optimized_without_timeout = prueba[prueba['optimized'] != 0.0]
sns.scatterplot(x='ejemplo', y='optimized', data=optimized_without_timeout, label='optimized')

plt.xticks(rotation=90)

plt.legend()

# Mostrar el gráfico
plt.show()