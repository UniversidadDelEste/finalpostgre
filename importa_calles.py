#!/bin/python
# coding: utf8

import csv
import json
import psycopg2

# cadena de conexión a la base de datos, en windows agregar host="localhost", user="usuario", password="clave":
conn = psycopg2.connect("dbname=caba port=5432 host=localhost user=oscar password=hola")

# crear un cursor para ejecutar consultas, y limpiar todos los registros:
cur = conn.cursor()
cur.execute("TRUNCATE calles;")

# abrir la planilla CSV e iterar sobre cada fila, cerrar el archivo al finalizar
with open('ejes-calles.csv', 'rb') as csvfile:
    # intentar determinar automaticamente formato del archivo:
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)
    reader = csv.reader(csvfile, dialect, delimiter=";")
    # saltear encabezado (primera fila
    encabezado = reader.next()
    # recorrer las filas de los datos en el CSV:
    for linea in reader:
        print linea
        # convertir el texto de cada campo a valores python:
        val_id = int(linea[0])
        val_codigo = linea[1]
        val_nomoficial = linea[2]
        # convierto la ubicación (latitud/longitud)
        punto = float(linea[11]), float(linea[12])
        # convierto campo geográfico (segmento de linea)
        geojson = json.loads(linea[-1])
        coords = geojson["coordinates"][0]
        lseg = ",".join(["(%s,%s)" % tuple(coords[i]) for i in (0, -1)])

        # evitar clave duplicada!
        if val_id in (30095, ):
            continue
        # insertar datos, evitar inyección SQL separando sentencias de parámetros
        parametros = [val_id, val_codigo, val_nomoficial, punto, lseg]
        cur.execute("INSERT INTO calles "
                    " (id, codigo, nomofical, punto, segmento)"
                    " VALUES (%s, %s, %s, '%s'::POINT, %s::LSEG)",
                    parametros)

conn.commit()