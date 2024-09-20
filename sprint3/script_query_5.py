import pandas as pd
from pyhive import hive
import matplotlib.pyplot as plt
import seaborn as sns
# open connection
HOST = '127.0.0.1'  # La direccion del host
PORT = '10000'  # Puerto donde escucha Hive

# Creamos la conexion con el cliente de Hive
conn = hive.Connection(
    host=HOST,
    port=PORT
    )


# Leer la consulta SQL desde un archivo externo
with open('query_5.hql', 'r') as archivo_sql:
    query = archivo_sql.read()

# recuperamos los datos desde la base de datos
data = pd.read_sql(query, conn)
# creamos el grafico con las 5 aerolineas con mas vuelos
sns.catplot(
            x="originairportid",
            y="cantidad",
            data=data)
plt.show()
