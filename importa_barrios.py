#!/bin/python
# coding: utf8

import csv
import json
import psycopg2
import db

class ImportaBarrios:
    db = db.Modelo()
    conn = db.Conectar()

    def Importa(self, archivo = "barrios.csv"):

        cur = self.conn.cursor()
        query = "drop table if exists tbarrios;"
        cur.execute(query)

        # crear un cursor para ejecutar consultas, y limpiar todos los registros:
        query = 'CREATE TABLE tbarrios('\
            'barrio text,'\
            'perimetro text,'\
            'area text,'\
            'comuna integer,'\
            'lon real,'\
            'lat real)'
        cur.execute(query)

        #llamo a la funcion para crear la tabla
        cur.execute("truncate tbarrios;")

        # abrir la planilla CSV e iterar sobre cada fila, cerrar el archivo al finalizar
        with open(archivo, 'rb') as csvfile:
            # intentar determinar automaticamente formato del archivo:
            #dialect = csv.Sniffer().sniff(csvfile.read(1024))
            #csvfile.seek(0)
            reader = csv.reader(csvfile, delimiter=";")
            # saltear encabezado (primera fila
            encabezado = reader.next()
            # recorrer las filas de los datos en el CSV:
            for linea in reader:

                datos = linea[0].split(',')
                # convertir el texto de cada campo a valores python:
                print datos[0]
                print datos[1]
                print datos[2]
                print datos[3]
                barrio = datos[0]
                perimetro = datos[1]
                area = datos[2]
                comuna = int(datos[3])
                lon = float(self.sacapuntos(datos[4]))
                lat = float(self.sacapuntos(datos[5]))

                # insertar datos, evitar inyección SQL separando sentencias de parámetros
                parametros = [barrio, perimetro, area, comuna, lon, lat]
                print parametros
                cur.execute("INSERT INTO tbarrios "
                            " (barrio, perimetro, area, comuna, lon, lat)"
                            " VALUES (%s, %s, %s, %s, %s, %s)",
                            parametros)

        self.conn.commit()
        self.conn.close()

if __name__ == "__main__":
    imp = ImportaBarrios()
    imp.Importa('barrios.csv')