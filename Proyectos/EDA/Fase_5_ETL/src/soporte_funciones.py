# %%
# Importamos librerias
import pandas as pd
import numpy as np

# Visualización
# ------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración
# -----------------------------------------------------------------------
pd.set_option('display.max_columns', None) # para poder visualizar todas las columnas de los DataFrames

# Gestión de los warnings
# -----------------------------------------------------------------------
import warnings
warnings.filterwarnings("ignore")

# %%

## Funciones EDA y transformación de datos: 

def exploracion(df):

## "Función exploración DF (nulos, tipo de datos, duplicados y principales estadisticas)"

    df_info = pd.DataFrame()

    df_info["% nulos"] = round(df.isna().sum()/df.shape[0]*100, 2).astype(str)+"%"
    df_info["% no_nulos"] = round(df.notna().sum()/df.shape[0]*100, 2).astype(str)+"%"
    df_info["tipo_dato"] = df.dtypes
    df_info["num_valores_unicos"] = df.nunique()

    print(f"""El DataFrame tiene {df.shape[0]} filas y {df.shape[1]} columnas.
Tiene {df.duplicated().sum()} datos duplicados, lo que supone un porcentaje de {round(df.duplicated().sum()/df.shape[0], 2)}% de los datos.

Hay {len(list(df_info[(df_info["% nulos"] != "0.0%")].index))} columnas con datos nulos, y son: 
{list(df_info[(df_info["% nulos"] != "0.0%")].index)}

y sin nulos hay {len(list(df_info[(df_info["% nulos"] == "0.0%")].index))} columnas y son: 
{list(df_info[(df_info["% nulos"] == "0.0%")].index)}


A continuación tienes un detalle sobre los datos nulos y los tipos y número de datos:""")
    
    display(df_info.head())

    print("Principales estadísticos de las columnas categóricas:")

    display(df.describe(include="O").T)

    print("Principales estadísticos de las columnas numéricas:")

    display(df.describe(exclude="O").T)

    return df_info

# %%

# Función para convertir palabras a números

def convertir_a_numero(edad_palabra):
    # Si el valor ya es un número, lo dejamos tal cual
    if isinstance(edad_palabra, (int, float)):
        return edad_palabra
    try:
        # Si no es un número, tratamos de convertirlo a número
        return w2n.word_to_num(edad_palabra)
    except ValueError:
        # Si no se puede convertir, devolvemos None
        return None
    
# %%

#Función para cambiar comas a puntos en decimales: 

def cambiar_comas (columnas_numericas):
    try:
        return float(columnas_numericas.replace(",", ".").replace("$", ""))
    
    except: np.nan

# %%

##Funciones AB Testing: 

## Normalidad de los datos: 
def normalidad(dataframe, columna):
    """
    Evalúa la normalidad de una columna de datos de un DataFrame utilizando la prueba de Shapiro-Wilk.

    Parámetros:
        dataframe (DataFrame): El DataFrame que contiene los datos.
        columna (str): El nombre de la columna en el DataFrame que se va a evaluar para la normalidad.

    Returns:
        None: Imprime un mensaje indicando si los datos siguen o no una distribución normal.
    """

    statistic, p_value = stats.shapiro(dataframe[columna])
    if p_value > 0.05:
        print(f"Para la columna {columna} los datos siguen una distribución normal.")
    else:
        print(f"Para la columna {columna} los datos no siguen una distribución normal.")


# %%
## Mann-Whitney: 

def test_man_whitney(dataframe, columnas_metricas, grupo_control, grupo_test, columna_grupos = "campaign_name"):

    """
    Realiza la prueba de Mann-Whitney U para comparar las medianas de las métricas entre dos grupos en un DataFrame dado.

    Parámetros:
    - dataframe (DataFrame): El DataFrame que contiene los datos.
    - columnas_metricas (list): Una lista de nombres de columnas que representan las métricas a comparar entre los grupos.
    - grupo_control (str): El nombre del grupo de control en la columna especificada por columna_grupos.
    - grupo_test (str): El nombre del grupo de test en la columna especificada por columna_grupos.
    - columna_grupos (str): El nombre de la columna que contiene la información de los grupos. Por defecto, "campaign_name".

    Returns 
    No devuelve nada directamente, pero imprime en la consola si las medianas son diferentes o iguales para cada métrica.
    Se utiliza la prueba de Mann-Whitney U para evaluar si hay diferencias significativas entre los grupos.
    """
    # filtramos el DataFrame para quedarnos solo con los datos de control
    control = dataframe[dataframe[columna_grupos] == grupo_control]
    
    # filtramos el DataFrame para quedarnos solo con los datos de control
    test = dataframe[dataframe[columna_grupos] == grupo_test]
    
    
    # iteramos por las columnas de las metricas para ver si para cada una de ellas hay diferencias entre los grupos
    for metrica in columnas_metricas:
        
        # filtrams el conjunto de datos para quedarnos solo con la columna de la metrica que nos interesa
        metrica_control = control[metrica]
        metrica_test = test[metrica]
        
        # aplicamos el estadístico
        u_statistic, p_value = stats.mannwhitneyu(metrica_control, metrica_test)
        
        if p_value < 0.05:
            print(f"Para la métrica {metrica}, las medianas son diferentes.")
        else:
            print(f"Para la métrica {metrica}, las medianas son iguales.")    


# %%
