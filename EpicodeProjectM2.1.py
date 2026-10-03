import pandas as pd

# PARTE 1: CARICAMENTO ED ESPLORAZIONE DEI DATI

#1. Lettura dataset con pandas
df = pd.read_csv("vendite_riassunto.csv")

#2.Visuliazzazione dei dati
print(df.head())
print(df.info())
print(df.describe())

# PARTE 2: PULIZIA 

#3. Gestione dei valori mancanti
print(df.isnull().sum())
media_vendite = df["Vendite"].mean()
df["Vendite"] = df["Vendite"].fillna(media_vendite)
print(df.isnull().sum())
print(df)

#4. Rimozione duplicati
print(df[df.duplicated()])
df = df.drop_duplicates()
print(df.duplicated().sum())
print(df)

#5. Verifica tipologie e correttezza dei dati
print(df.dtypes)
df["Data"] = pd.to_datetime(df["Data"])
print(df.dtypes)

#PARTE 3: ANALISI ESPLORATIVA

#6. Calcolo delle vendite totali per prodotto
vendite_totali_per_prodotto = df.groupby("Prodotto")["Vendite"].sum()
print(vendite_totali_per_prodotto)

#7. Prodotto più e meno venduto
prodotto_piu_venduto = vendite_totali_per_prodotto.idxmax()
prodotto_meno_venduto = vendite_totali_per_prodotto.idxmin()

print("Prodotto più venduto:", prodotto_piu_venduto)
print("Prodotto meno venduto:", prodotto_meno_venduto)

#8. Vendite medie giornaliera
vendite_media_giornaliere = df.groupby("Data")["Vendite"].sum()
media_giornaliera = vendite_media_giornaliere.mean()

print("Vendite medie giornaliere:", media_giornaliera)