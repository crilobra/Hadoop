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
with open('query_4.hql', 'r') as archivo_sql:
    query = archivo_sql.read()

# recuperamos los datos desde la base de datos
data = pd.read_sql(query, conn)

print(data["_u2.tipo"])


categorias = data["_u2.tipo"]
valores = data["_u2.porcentaje"]

# Aplicar el estilo de Seaborn
sns.set(style="whitegrid")

# Dibujar gráfico de torta usando Matplotlib
plt.figure(figsize=(7, 7))
plt.pie(
    valores,
    labels=categorias,
    autopct='%1.1f%%',
    startangle=90,
    colors=sns.color_palette("pastel")
    )

# Asegurarse de que el gráfico sea circular
plt.axis('equal')

# Mostrar gráfico
plt.title("Gráfico de Performance", fontsize=16)
plt.show()
