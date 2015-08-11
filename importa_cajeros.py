#!/bin/python
# coding: utf8

import csv
import json
import psycopg2
import db

class ImportaCajeros():
    db = db.Modelo()
    conn = db.Conectar()

    def sacapuntos(self, cadena):

        lista = cadena.split('.')
        datos = ''
        n = 0
        for i in lista:
            if n == 0:
                datos += i
            elif n == 1:
                datos += '.' + i
            else:
                datos += i
            n += 1
        return datos

    def Importa(self, archivo = "cajeros.csv"):

        # cadena de conexión a la base de datos, en windows agregar host="localhost", user="usuario", password="clave":
        #conn = psycopg2.connect("dbname=final port=5432 host=localhost user=postgres password=hola")

        # crear un cursor para ejecutar consultas, y limpiar todos los registros:
        cur = self.conn.cursor()
        #cur.execute("TRUNCATE tcajeros;")

        query = "drop table if exists tcajeros"
        cur.execute(query)

        query = 'CREATE TABLE tcajeros('\
            'banco text,'\
            'red text,'\
            'direccion text,'\
            'terminales integer,'\
            'web text,'\
            'actualizacion text,'\
            'lon real,'\
            'lat real)'
        cur.execute(query)

        #llamo a la funcion para crear la tabla
        cur.execute("truncate tcajeros;")

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
                print linea
                # convertir el texto de cada campo a valores python:
                banco = linea[0]
                red = linea[1]
                direccion = linea[2]
                terminales = int(linea[3])
                web = linea[4]
                actualizacion = linea[5]
                lon = float(self.sacapuntos(linea[6]))
                lat = float(self.sacapuntos(linea[7]))

                # insertar datos, evitar inyección SQL separando sentencias de parámetros
                parametros = [banco, red, direccion, terminales, web, actualizacion, lon, lat]
                print parametros
                cur.execute("INSERT INTO tcajeros "
                            " (banco, red, direccion, terminales, web, actualizacion, lon, lat)"
                            " VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                            parametros)

        self.conn.commit()
        self.conn.close()

if __name__ == "__main__":
    imp = ImportaCajeros()
    imp.Importa('cajeros.csv')