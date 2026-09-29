"""
Módulo de Procesamiento y Limpieza de Leads
Completa las funciones indicadas para limpiar, validar y generar métricas del dataset.
"""
import os
import pandas as pd
import requests

DATA_IN = os.path.join(os.path.dirname(__file__), "..", "data", "leads.csv")
DATA_OUT = os.path.join(os.path.dirname(__file__),
                        "..", "data", "leads_limpios.csv")


def cargar_datos() -> pd.DataFrame:
    """1. Cargar el dataset crudo."""
    df = pd.read_csv(DATA_IN)
    print(f"Total registros cargados: {len(df)}")
    return df


def limpiar_datos(df: pd.DataFrame) -> pd.DataFrame:
    """
    2. Limpieza de datos:

    - Eliminar registros duplicados considerando el campo email.
    - Descartar registros con email vacío.
    - Normalizar los valores de estatus a:
      NUEVO, CONTACTADO, EN_SEGUIMIENTO, CONVERTIDO, PERDIDO.
    - Rellenar valores nulos en presupuesto con 0.
    """

    df_limpio = df.copy()

    # Eliminar registros con email vacío o nulo
    df_limpio = df_limpio.dropna(subset=["email"])
    df_limpio = df_limpio[
        df_limpio["email"].astype(str).str.strip() != ""
    ]

    # Eliminar duplicados considerando únicamente el email
    df_limpio = df_limpio.drop_duplicates(
        subset=["email"],
        keep="first"
    )

    # Normalizar estatus
    mapa_estatus = {
        "nuevo": "NUEVO",
        "contactado": "CONTACTADO",
        "en seguimiento": "EN_SEGUIMIENTO",
        "en_seguimiento": "EN_SEGUIMIENTO",
        "convertido": "CONVERTIDO",
        "perdido": "PERDIDO"
    }

    df_limpio["estatus"] = (
        df_limpio["estatus"]
        .astype(str)
        .str.strip()
        .str.lower()
        .map(mapa_estatus)
    )

    # Rellenar presupuestos nulos con 0
    df_limpio["presupuesto"] = df_limpio["presupuesto"].fillna(0)

    return df_limpio


def generar_resumen(df: pd.DataFrame):
    """
    3. Imprimir métricas en consola:

    - Total de prospectos limpios.
    - Cantidad de prospectos por origen.
    - Cantidad de prospectos por estatus normalizado.
    """

    print("\n--- RESUMEN DE LEADS ---")

    print(f"Total de prospectos limpios: {len(df)}")

    print("\nProspectos por origen:")
    print(df["origen"].value_counts())

    print("\nProspectos por estatus:")
    print(df["estatus"].value_counts())


if __name__ == "__main__":
    # Cargar datos
    df = cargar_datos()

    # Limpiar datos
    df_limpio = limpiar_datos(df)

    # Guardar dataset limpio
    df_limpio.to_csv(DATA_OUT, index=False)
    print(f"Dataset limpio guardado en: {DATA_OUT}")

    # Generar resumen
    generar_resumen(df_limpio)
