# creamos la carpeta data/airlines
hdfs dfs -mkdir /data/airlines
# colocamos el archivo 2024_1.csv an la carpeta /data/airlines
hdfs dfs -put ../2024_1.csv /data/airlines/2024_1.csv 
# colocamos el archivo 2024_2.csv an la carpeta /data/airlines
hdfs dfs -put ../2024_2.csv /data/airlines/2024_2.csv
# colocamos el archivo 2024_3.csv an la carpeta /data/airlines
hdfs dfs -put ../2024_3.csv /data/airlines/2024_3.csv