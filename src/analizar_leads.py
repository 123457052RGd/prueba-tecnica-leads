import pandas as pd

df = pd.read_csv("leads.csv")

print("===== INFORMACIÓN GENERAL =====")
print(f"Filas: {df.shape[0]}")
print(f"Columnas: {df.shape[1]}")

print("\n===== COLUMNAS =====")
print(df.columns.tolist())

print("\n===== VALORES NULOS =====")
print(df.isnull().sum())

print("\n===== TIPOS DE DATOS =====")
print(df.dtypes)

print("\n===== ESTATUS =====")
print(df["estatus"].value_counts(dropna=False))

print("\n===== ORIGEN =====")
print(df["origen"].value_counts(dropna=False))

print("\n===== DUPLICADOS =====")
print(f"Registros duplicados: {df.duplicated().sum()}")
