#!/usr/bin/python3
import sys

dias = []
# Inicializamos contador
contador = 0
for linea in sys.stdin:
    # quitamos espacios de sobra
    linea = linea.strip()
    # dividimos la linea en elementos
    datos = linea.split(",")
    if contador != 0:
        print(datos[11], "\t1")
    contador = contador + 1
