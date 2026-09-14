
import pandas as pd #comando para importar o pandas.

df = pd.read_csv("bons_Burguers.csv") #comando para ler o arquivo csv e armazená-lo dentro da variável df (dataFrame).

print(df) #comando para imprimir e mostrar o conteúdo do arquivo(dataFrame) no terminal.

print(df.dtypes) #mostra o tipo de cada coluna da dataFrame.

df["nome"] = df["nome"].str.replace("pao francês", "pão francês", regex=False) #remove espaço antes ou depois do texto e substitui palavras

df["nome"] = df["nome"].str.replace("pao brioche", "pão brioche", regex=False)

df["nome"] = df["nome"].str.replace("Rúculla", "rúcula", regex=False)

df["nome"] = df["nome"].str.replace("Catupiry", "catupiry", regex=False) 

df["nome"] = df["nome"].str.replace("Bacon", "bacon", regex=False)

df["nome"] = df["nome"].str.replace("Hetchup", "ketchup", regex=False)

df["nome"] = df["nome"].str.replace("Mostarda", "mostarda", regex=False) 

df["nome"] = df["nome"].str.replace("Maionese Tradicional", "maionese tradicional", regex=False)

df["nome"] = df["nome"].str.replace("Maionese de Bacon defumada", "maionese de bacon defumada", regex=False)

df["nome"] = df["nome"].str.replace("Nuggets", "nuggets", regex=False) 

df["nome"] = df["nome"].str.replace("caixa de Nuggets", "caixa de nuggets", regex=False)

df["nome"] = df["nome"].str.replace("caixa de batat frita", "caixa de batata frita", regex=False)

df["nome"] = df["nome"].str.replace("Coca-Cola tradicional 2l", "coca-cola tradicional 2l", regex=False) 

df["nome"] = df["nome"].str.replace("Coca-cola Zero Açucar 2l", "coca-cola zero açúcar 2l", regex=False)

df["nome"] = df["nome"].str.replace("Coca-cola tradicional 1,5l", "coca-cola tradicional 1,5l", regex=False)

df["nome"] = df["nome"].str.replace("Coca-cola Zero Açúcar 1,5l", "coca-cola zero açúcar 1,5l", regex=False) 

df["nome"] = df["nome"].str.replace("coca-cola tradiciopnal 600ml", "coca-cola tradicional 600ml", regex=False)

df["nome"] = df["nome"].str.replace("coca-cola tradciional lata 350ml", "coca-cola tradicional lata 350ml", regex=False)

#alterando os valores
df["valor"] = df["valor"].astype(float).replace(9999.00, 43.90)

df["tipo"] = df["tipo"].str.replace("pao", "pão", regex=False)

df["tipo"] = df["tipo"].str.replace("veruda", "verdura", regex=False)

df.to_csv("bons_Burguers_tratado.csv", index=False)

df_limpo = pd.read_csv("bons_Burguers_tratado.csv")

import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password="root",
    database="ingredientes"
)

cursor = conexao.cursor()

print("Conectado ao MySQL!")

