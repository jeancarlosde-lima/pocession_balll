#!/usr/bin/env python
# coding: utf-8

# In[44]:


import pandas as pd
import matplotlib.pyplot as plt


# In[56]:


# Dados fictícios para demonstração
dados_barcelona = {'Jogador': ['Messi', 'Suarez', 'Busquets'],
                   'Passes': [87, 32, 67]}

dados_bayern = {'Jogador': ['Lewandowski', 'Müller', 'Thiago'],
                'Passes': [25, 65, 95]}

# Criar dataframes com os dados
df_barcelona = pd.DataFrame(dados_barcelona)
df_bayern = pd.DataFrame(dados_bayern)

# Calcular a soma total de passes de cada time
total_passes_barcelona = df_barcelona['Passes'].sum()
total_passes_bayern = df_bayern['Passes'].sum()

# Plotar gráfico de pizza
times = ['Barcelona', 'Bayern de Munique']
total_passes = [total_passes_barcelona, total_passes_bayern]
cores = ['purple', 'red']

plt.pie(total_passes, labels=times, colors=cores, autopct='%1.1f%%')
plt.title('Comparação de Passes Totais')

plt.show()


# In[ ]:




