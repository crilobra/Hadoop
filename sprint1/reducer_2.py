#!/usr/bin/python3
import sys

# inicializamos el diccionario
origenes = {}

for linea in sys.stdin:
    # quitamos espacios de sobra
    linea = linea.strip()
    # parseamos la entrada de mapper.py
    origenId, cuenta = linea.split('\t', 1)
    # convertimos cuenta de string a int
    try:
        cuenta = int(cuenta)
    except ValueError:
        # cuenta no era un numero, descartamos la linea
        continue

    try:
        origenes[origenId] += cuenta
    except IndexError:
        origenes[origenId] = cuenta

for origenId in origenes.keys():
    print(origenId.strip(), ",", origenes[origenId])
