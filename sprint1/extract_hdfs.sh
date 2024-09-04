# creamos la carpeta data
hdfs dfs -mkdir /data
# colocamos el archivo correspondiente al mes de marzo
hdfs dfs -put ../2024_3.csv /data/marzo2024.csv
# renombramos el archivo
hdfs dfs -mv /data/marzo2024.csv /data/2024_3.csv
# verificamos los blockes utilizados por el archivo
hdfs fsck  /data/2024_3.csv -files -blocks
# mostramos los primeros 10 datos del archivo
hdfs dfs -cat /data/2024_3.csv | head -n 10
#listamos los directorios existentes
hdfs dfs -ls /