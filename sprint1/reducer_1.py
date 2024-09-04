#!/usr/bin/python3
import sys

# inicializamos el diccionario
dias = {}

for linea in sys.stdin:
    # quitamos espacios de sobra
    linea = linea.strip()
    # parseamos la entrada de mapper.py
    dia, cuenta = linea.split('\t', 1)
    # convertimos cuenta de string a int
    try:
        cuenta = int(cuenta)
    except ValueError:
        # cuenta no era un numero, descartamos la linea
        continue

    try:
        dias[dia] += cuenta
    except IndexError:
        dias[dia] = cuenta

for dia in dias.keys():
    print(dia.strip(), ",", dias[dia])
