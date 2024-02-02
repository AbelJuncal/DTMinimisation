import pandas as pd
import seaborn as sns

df = pd.read_csv('tiempos.csv')
filtered = df.groupby(["programa", "ejemplo"])["tiempo"].mean()

prueba = filtered.reset_index()

print(prueba)

prueba['tiempo'] = prueba['tiempo'].round(4)

prueba.to_csv('filtrado.txt', index=False)