#%% 
import mysql.connector 
import pandas as pd
from mysql.connector import errorcode
from sqlalchemy import create_engine
import numpy as np

# Config pandas para ver todas las columnas 
pd.set_option("display.max_columns", None)

#%%

## Función crear base de datos: 
def creacion_bbdd (query,contraseña,nombre_bbdd = 'None'):

    if nombre_bbdd is not None: 
        cnx = mysql.connector.connect(
            user = "root", 
            password = contraseña, 
            host = "127.0.0.1"
        )

        mycursor = cnx.cursor()

        try: 
            mycursor.execute(query)
            print(mycursor)
        except mysql.connector.Error as err: 
            print(err)
            print("Error code: ", err.errno)
            print("SQLSTATE", err.sqlstate )
            print("Message", err.msg)

    else: 
        cnx = mysql.connector.connect(
            user = "root", 
            password = contraseña, 
            host = "127.0.0.1", 
            database = nombre_bbdd)
            
        mycursor = cnx.cursor()

        try: 
            mycursor.execute(query)
            print(mycursor)

        except mysql.connector.Error as err: 
            print(err)
            print("Error code: ", err.errno)
            print("SQLSTATE", err.sqlstate )
            print("Message", err.msg)


#%%


## Función crear tablas: 

def insertar_datos_a_sql(dataframe, tabla, usuario, contraseña, host, base_datos, puerto=3306, if_exists='append'):
    """
    Inserta un DataFrame en una tabla de una base de datos MySQL.
    Parámetros:
        dataframe (pd.DataFrame): DataFrame con los datos a insertar.
        tabla (str): Nombre de la tabla en la base de datos.
        usuario (str): Usuario de la base de datos.
        contraseña (str): Contraseña del usuario de la base de datos.
        host (str): Dirección del host (e.g., '127.0.0.1').
        base_datos (str): Nombre de la base de datos.
        puerto (int): Puerto de la conexión MySQL (por defecto 3306).
        if_exists (str): Comportamiento si la tabla ya existe ('fail', 'replace', 'append').
    """
    try:
        # Crear la conexión con SQLAlchemy
        engine = create_engine(f'mysql+pymysql://{usuario}:{contraseña}@{host}:{puerto}/{base_datos}')
        # Guardar el DataFrame en la base de datos
        dataframe.to_sql(tabla, con=engine, if_exists=if_exists, index=False)
        print(f"Datos insertados exitosamente en la tabla '{tabla}'.")
    except Exception as e:
        print("Ocurrió un error al insertar los datos:", e)
# Ejemplo de uso
# insertar_datos_a_sql(df_personal, 'info_personal', 'root', 'AlumnaAdalab', '127.0.0.1', 'estudio_satisfaccion')


# %%
