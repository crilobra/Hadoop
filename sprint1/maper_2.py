#!/usr/bin/python3
import sys

dias = []
contador = 0
for linea in sys.stdin:
    
    linea = linea.strip()
    datos = linea.split(",")
    if contador !=0:
        print(datos[11],"\t1")
    contador = contador + 1