## Atividade 2

* Como identificar e tratar outliers em uma coluna numérica usando desvio
padrão ou quartis?

Desvio padrão
```python
mean = df[coluna].mean()
std = df[coluna].std()
    
# Define limites (3 desvios padrão)
limite_superior = mean + 3*std
limite_inferior = mean - 3*std
    
# Identifica outliers
outliers = df[(df[coluna] > limite_superior) | (df[coluna] < limite_inferior)]
    
# Remove outliers
df_sem_outliers = df[(df[coluna] <= limite_superior) & (df[coluna] >= limite_inferior)] 
```

Quartis
```python
Q1 = df[coluna].quantile(0.25)
Q3 = df[coluna].quantile(0.75)
IQR = Q3 - Q1
    
# Define limites
limite_superior = Q3 + 1.5*IQR
limite_inferior = Q1 - 1.5*IQR
    
# Remove outliers
df_sem_outliers = df[(df[coluna] >= limite_inferior) & (df[coluna] <= limite_superior)]
```

* Como concatenar vários DataFrames (empilhando linhas ou colunas),
mesmo que tenham colunas diferentes?
Dica: Utiliza-se pd.concat() especificando axis=0 (linhas) ou axis=1
(colunas). Quando há colunas diferentes, os valores ausentes são
preenchidos com NaN.

Empilhando linhas
```python
df_final = pd.concat([df1, df2], axis=0)
```

Empilhando colunas
```python
df_final = pd.concat([df1, df2], axis=1)
```

* Utilizando pandas, como realizar a leitura de um arquivo CSV em um
DataFrame e exibir as primeiras linhas?
```python
df = pd.read_csv('nome_do_arquivo.csv')

# Exibir as primeiras 5 linhas
df.head()
```

*Utilizando pandas, como selecionar uma coluna específica e filtrar linhas
em um “DataFrame” com base em uma condição?

```python
df['nome_coluna']

# Filtrar linhas com condições. Ex: valores maiores que 10
df[df['nome_coluna'] > 10] 
```

*Utilizando pandas, como lidar com valores ausentes (NaN) em um
DataFrame?

```python
#saber quais estão com valores ausentes
df.isna()

# conta quantos valores ausentes tem
df.isna().sum()

#exemplo de preencher com 0
df.fillna(0)

#excluir dados com valores ausentes
df.dropna()
```