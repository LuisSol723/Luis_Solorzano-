# funciones.py

import pandas as pd
import matplotlib.pyplot as plt

def leer_datos(ruta_archivo):
    """
    Lee un archivo CSV y devuelve un DataFrame.
    """
    try:
        df = pd.read_csv(ruta_archivo)
        print("Datos cargados correctamente.")
        return df
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

def graficar_datos(df, columna):
    """
    Genera un gráfico de línea de la columna especificada.
    """
    if df is not None and columna in df.columns:
        plt.figure(figsize=(10,5))
        plt.plot(df[columna], marker='o', linestyle='-')
        plt.title(f'Gráfico de {columna}')
        plt.xlabel('Índice')
        plt.ylabel(columna)
        plt.grid(True)
        plt.show()
    else:
        print("El DataFrame es None o la columna no existe.")
        