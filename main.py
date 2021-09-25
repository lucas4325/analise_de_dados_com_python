from datetime import timezone
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

df = pd.read_excel('/home/lucas/Documents/vs code/python/Dio/projeto/2be7520c-94cd-463f-8432-d580d0810344/Cusro_Python_Pandas_Digital_Innovation-master/datasets/AdventureWorks.xlsx')
#print(df.dtypes)
#print(df['Valor Venda'].sum())
df['custo'] = df['Custo Unitário'].mul(df['Quantidade'])
#print(round(df['custo'].sum(), 2))
df['lucro'] = df['Valor Venda'] - df['custo']
#print(round(df['lucro'].sum(), 2))
df['Tempo_envio'] = (df['Data Envio'] - df['Data Venda']).dt.days   
#print(df['Tempo_envio'].dtype)
#print(df.groupby('Marca')['Tempo_envio'].mean())
#print(df.isnull().sum())
pd.options.display.float_format = '{:20,.2f}'.format
#print(df.groupby([df['Data Venda'].dt.year, 'Marca'])['lucro'].sum())
lucro_ano = df.groupby([df['Data Venda'].dt.year, 'Marca'])['lucro'].sum().reset_index()
#print(lucro_ano)
#print(df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False))

#print(df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=True).plot.barh(title='Total Produtos Vendidos'))
#plt.xlabel('Total')
#plt.ylabel('Produto');

#print(df.groupby(df['Data Venda'].dt.year)['lucro'].sum().plot.bar(title='Lucro X Ano'))
#plt.xlabel('Ano')
#plt.ylabel('Receita');

#print(df.groupby(df['Data Venda'].dt.year)['lucro'].sum())

df_2009 = df[df['Data Venda'].dt.year == 2009]
print(df_2009)

'''print(df_2009.groupby(df_2009['Data Venda'].dt.month)['lucro'].sum().plot(title='Lucro Mes'))
plt.xlabel('Mês')
plt.ylabel('Lucro');'''

'''df_2009.groupby('Marca')['lucro'].sum().plot.bar(title='Lucro x Marca')
plt.xlabel('Marca')
plt.ylabel('Lucro')
plt.xticks(rotation='horizontal')'''

'''df_2009.groupby('Classe')['lucro'].sum().plot.bar(title='Lucro x Classe')
plt.xlabel('Classe')
plt.ylabel('Lucro')
plt.xticks(rotation='horizontal')'''

df['Tempo_envio'].describe()
plt.boxplot(df['Tempo_espera']);
plt.hist(df['Tempo_envio']);
df['Tempo_envio'].min()
df['Tempo_envio'].max()
df[df['Tempo_envio'] == 20]

#print(df.head())
df.to_csv('df_vendas_novo.csv', index=False)
