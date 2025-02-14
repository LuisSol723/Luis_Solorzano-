# main.py

from funciones import leer_datos, graficar_datos

def main():
    # Suponiendo que tienes un archivo CSV llamado 'datos.csv'
    ruta = 'fifa_data.csv'
    
    # Leer datos
    df = leer_datos(ruta)
    
    # Verificar que se hayan cargado datos y graficar la columna 'valor'
    if df is not None:
        # Mostrar las primeras filas
        print(df.head())
        # Graficar la columna 'valor' (asegúrate de que exista en tu CSV)
        graficar_datos(df, 'Age')

if __name__ == '__main__':
    main()