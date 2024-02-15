import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def tiempo_a_segundos(tiempo):
    if(len(tiempo.split('m')) > 1):
        minutos, segundos = tiempo.split('m')
        minutos = int(minutos)
        segundos = float(segundos.rstrip('s'))
        total_segundos = minutos * 60 + segundos
        return total_segundos
    else:
        return 0.0

df = pd.read_csv('tiempos.csv')

filtered = df.groupby(["programa", "ejemplo"])["tiempo"].mean()

prueba = filtered.reset_index()

prueba['tiempo'] = prueba['tiempo'].round(4)

prueba = prueba.sort_values(by="ejemplo")

prueba = prueba.pivot(index='ejemplo', columns='programa', values='tiempo')

prueba = prueba.reset_index()

prueba = prueba[['ejemplo', 'prolog', 'python', 'optimized']]

prueba = prueba.replace(120.0, 3600.0)



prueba.to_csv('filtrado.txt', index=False)


sns.set(style='whitegrid')

# #Gráfica completa

prolog_without_timeout = prueba[prueba['prolog'] != 0.0]
python_without_timeout = prueba[prueba['python'] != 0.0]
optimized_without_timeout = prueba[prueba['optimized'] != 0.0]

#Sen Heurística vs optimized


fig4 = plt.figure(figsize=(10,10))

ax4 = fig4.add_subplot(1,1,1)

ax4.set_title('Sen Heurística vs Con Heurística')

sns.scatterplot(x='optimized', y='python', data=python_without_timeout)

ax4.set_xlim(left=0,right=3600)
ax4.set_ylim(bottom = 0, top=3600)

ax4.plot(ax4.get_xlim(), ax4.get_ylim(), linestyle='--')

plt.xlabel('Con Heurística')
plt.ylabel("Sen Heurística")

plt.xticks(rotation=90)

#

fig3 = plt.figure(figsize=(10,10))

ax3 = fig3.add_subplot(1,1,1)

ax3.set_title('Prolog vs Sen Heurística')

sns.scatterplot(x='prolog', y='python', data=python_without_timeout)

ax3.set_xlim(left=0,right=3600)
ax3.set_ylim(bottom = 0, top=3600)

ax3.plot(ax3.get_xlim(), ax3.get_ylim(), linestyle='--')

plt.xlabel('Prolog')
plt.ylabel("Sen Heurística")

plt.xticks(rotation=90)

#

fig5 = plt.figure(figsize=(10,10))

ax5 = fig5.add_subplot(1,1,1)

ax5.set_title('Prolog vs Sen Heurística')

sns.scatterplot(x='prolog', y='python', data=python_without_timeout)

ax5.set_xlim(left=0,right=500)
ax5.set_ylim(bottom = 0, top=500)

ax5.plot(ax5.get_xlim(), ax5.get_ylim(), linestyle='--')

plt.xlabel('Prolog')
plt.ylabel("Sen Heurística")

plt.xticks(rotation=90)

#

fig2 = plt.figure(figsize=(10,10))

ax2 = fig2.add_subplot(1,1,1)

ax2.set_title('Prolog vs Con heurística')

sns.scatterplot(x='prolog', y='optimized', data=python_without_timeout)

ax2.set_xlim(left=0,right=3600)
ax2.set_ylim(bottom = 0, top=3600)

ax2.plot(ax2.get_xlim(), ax2.get_ylim(), linestyle='--')

plt.xlabel('Prolog')
plt.ylabel("Con heurística")

plt.xticks(rotation=90)

#

fig6 = plt.figure(figsize=(10,10))

ax6 = fig6.add_subplot(1,1,1)

ax6.set_title('Prolog vs Con heurística')

sns.scatterplot(x='prolog', y='optimized', data=python_without_timeout)

ax6.set_xlim(left=0,right=500)
ax6.set_ylim(bottom = 0, top=500)

ax6.plot(ax6.get_xlim(), ax6.get_ylim(), linestyle='--')

plt.xlabel('Prolog')
plt.ylabel("Con heurística")

plt.xticks(rotation=90)

#

re = pd.read_csv('dt.csv')
re['optimized'] = re['optimized'].apply(tiempo_a_segundos)
re['python'] = re['python'].apply(tiempo_a_segundos)

fig = plt.figure(figsize=(10,10))

ax = fig.add_subplot(1,1,1)

ax.set_title('Árbores reais')

sns.scatterplot(x='python', y='optimized', data=re)

ax.set_xlim(left=0,right=3600)
ax.set_ylim(bottom = 0, top = 3600)

ax.plot(ax.get_xlim(), ax.get_ylim(), linestyle='--')

plt.xlabel('python')
plt.ylabel("optimized")

plt.xticks(rotation=90)

# Mostrar el gráfico
plt.show()