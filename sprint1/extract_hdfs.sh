hdfs dfs -mkdir /data
hdfs dfs -put ../2024_3.csv /data/marzo2024.csv
hdfs dfs -mv /data/marzo2024.csv /data/2024_3.csv
hdfs fsck  /data/2024_3.csv -files -blocks
hdfs dfs -cat /data/2024_3.csv | head -n 10
hdfs dfs -ls /