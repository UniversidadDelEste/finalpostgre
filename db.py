#!/bin/python
# coding: utf8
"""
aqui creo la clase que va a manejar las conexiones a la base de datos

como asi tambien todo lo relacionado a las tablas
"""

import psycopg2

class Modelo(object):

    def __init__(self):
        self.conn = self.Conectar()

    def Conectar(self):
        # cadena de conexión a la base de datos, en windows agregar host="localhost", user="usuario", password="clave":
        self.conn = psycopg2.connect("dbname=final port=5432 host=localhost user=postgres ")
        return self.conn

    def actualizarCajero(self, d2):
        """ Actualiza los datos de un registro existente.
        Es necesario proporcionar la id del registro
        junto con los valores de las otras columnas
        en el parámetro d2. """
        sql = '''
              UPDATE Cajeros Set direccion=%s, terminales=%s, longitud=%s, latitud=%s
              WHERE id=%s
              '''
        cursor = self.conn.cursor()
        cursor.execute(sql, d2)
        self.conn.commit()


    def seleccionar(self, id=None):
        """ Selecciona registros en la base de datos """
        cursor = self.conn.cursor()
        sql1 = ' SELECT * FROM cajeros '
        sql2 = sql1 + ' WHERE id = %s'
        if not id:
            cursor.execute(sql1)
        else:
            cursor.execute(sql2, (id,))
        registros = cursor.fetchall()   # recupera todos los registros
        cursor.close()
        return registros

    def eliminarCajero(self, id = None):
        sql = 'DELETE FROM cajeros WHERE id = %s'
        cursor = self.conn.cursor()
        cursor.execute(sql, (id,))
        self.conn.commit()
        cursor.close()

    def actualizaDatosCajero(self, datos):
        sql = '''
            UPDATE cajeros set direccion = %s, terminales = %s, longitud = %s, latitud = %s,
                barrio = %s, banco = %s, red = %s
                WHERE id = %s
        '''
        cursor = self.conn.cursor()
        cursor.execute(sql, datos)
        self.conn.commit()
