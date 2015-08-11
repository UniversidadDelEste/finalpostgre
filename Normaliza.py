#! /usr/bin/python
#encoding:utf-8
"""
aca normalizo todoas la tablas importadas

creo las tablas de bancos, redes, cajeros, barrios y comunas

para poder crearlas por los FK primero elimino las tablas relacionadas y luego si creo las demas
"""

import db
class Normaliza:

    db = db.Modelo()
    conn = db.Conectar()

    def NormalizaBarrios(self):
        #abro una conexion para realizar las consultas
        self.cur = conn.cursor()
        #creo las tablas de barrios
        self.CreaBarrios()
        #cierro la conexion
        self.cur.close()

    def NormalizaCajeros(self):
        #abro la conexion
        self.cur = conn.cursor()
        #elimino las tablas relacionadas
        self.EliminoTablasCajero()
        #creo la tabla de bancos
        self.CreaBancos()
        #creo la tabla de redes de bancos
        self.CreaRedes()
        #creo por ultimo la tabla de cajeros
        self.CreaCajeros()
        #cierro la conexion
        self.cur.close()

    def CreaBarrios(self):

        """si existe la tabla de barrios la elimino
            debo eliminar primero la tabla de barrios por las restricciones
        """
        #en caso de  existir la tabla de barrios la elimino
        query = "drop table if exists barrios"
        self.cur.execute(query)

        #si existe la tabla comuna la elimino
        query = "drop table if exists comunas"
        self.cur.execute(query)

        #creo la tabla de comunas
        query = "CREATE TABLE comunas"\
                "(id serial," \
                "comuna character varying(100), "\
                "CONSTRAINT PK_id PRIMARY KEY (id));"\
                "ALTER TABLE comunas OWNER TO postgres;"
        self.cur.execute(query)

        #creo la tabla de barrios
        query = 'CREATE TABLE barrios' \
                '(id serial NOT NULL,'\
                  'barrio character varying(100),'\
                  'perimetro real,'\
                  'area real,'\
                  'longitud real,'\
                  'latitud real,'\
                  'comuna integer,'\
                  'CONSTRAINT "PK_id" PRIMARY KEY (id),'\
                  'CONSTRAINT "FK_barrio_comuna" FOREIGN KEY (comuna) '\
                      'REFERENCES comunas (id) MATCH SIMPLE '\
                      'ON UPDATE CASCADE ON DELETE RESTRICT) '\
                'WITH (OIDS=FALSE);'\
                "ALTER TABLE comunas OWNER TO postgres;"
        self.cur.execute(query)

        #selecciono todos los barrios
        query = "select distinct comuna from tbarrios"
        self.cur.execute(query)
        resultados = self.cur.fetchall()

        for registro in resultados:
            print registro[0]
            parametro = [registro[0], "Comuna " + str(registro[0])]
            self.cur.execute("insert into comunas (id, comuna) values(%s,%s)", parametro)

        #selecciono los registros de la tabla temporal no normalizada de barrios
        query = "select * from tbarrios"
        self.cur.execute(query)
        resultados = self.cur.fetchall()
        for registro in resultados:
            print registro
            #grabo en la tabla de barrios
            parametros = registro[0], registro[1], registro[2], registro[3], registro[4], registro[5]
            query = "insert into barrios (barrio, perimetro, area, comuna, longitud, latitud)"\
                " values(%s,%s,%s,%s,%s,%s)"
            self.cur.execute(query, parametros)

        #finalizo la transaccion y guardo los cambios
        self.conn.commit()


    def CreaBancos(self):

        #creo la tabla de bancos
        query = 'create table bancos' \
                '(id serial,'\
                'banco character varying(100), '\
                'CONSTRAINT "PK_idBanco" PRIMARY KEY (id));'\
                'ALTER TABLE bancos OWNER TO postgres;'
        self.cur.execute(query)

        #selecciono los bancos de la tabla temporal y los cargo a la tabla de bancos
        query = "select distinct banco from tcajeros"
        self.cur.execute(query)
        resultados = self.cur.fetchall()
        for registro in resultados:
            parametros = [registro[0]]
            query = "insert into bancos (banco) values(%s)"
            self.cur.execute(query, parametros)

        self.conn.commit()

    def CreaRedes(self):
        #creo la tabla de redes
        query = 'create table redes ' \
                '(id serial, red character varying(100), web character varying(100),'\
                'CONSTRAINT "PK_idRedes" PRIMARY KEY (id));'\
                'ALTER TABLE redes OWNER TO postgres;'
        self.cur.execute(query)

        #selecciono todas las redes de la tabla temporal y los cargo a la tabla
        query = "select distinct red, web from tcajeros"
        self.cur.execute(query)
        resultados = self.cur.fetchall()

        for registro in resultados:
            parametros = [registro[0], registro[1]]
            query = "insert into redes (red, web) values(%s, %s)"
            self.cur.execute(query, parametros)

        self.conn.commit()

    def CreaCajeros(self):

        #creo la tabla de cajeros
        query = 'CREATE TABLE cajeros ('\
              'id serial NOT NULL,'\
              'direccion character varying(100),'\
              'terminales integer,'\
              'actualizacion date,'\
              'longitud real,'\
              'latitud real,'\
              'barrio integer,'\
              'banco integer,'\
              'red integer,'\
              'CONSTRAINT "PK_idCajero" PRIMARY KEY (id),'\
             ' CONSTRAINT "FK_cajero_banco" FOREIGN KEY (banco)'\
                  'REFERENCES bancos (id) MATCH SIMPLE '\
                  'ON UPDATE NO ACTION ON DELETE NO ACTION,'\
              'CONSTRAINT "FK_cajero_barrio" FOREIGN KEY (barrio)'\
                  'REFERENCES barrios (id) MATCH SIMPLE '\
                  'ON UPDATE NO ACTION ON DELETE NO ACTION,'\
              'CONSTRAINT "FK_cajero_redes" FOREIGN KEY (red)'\
                  'REFERENCES redes (id) MATCH SIMPLE '\
                  'ON UPDATE NO ACTION ON DELETE NO ACTION)'
        self.cur.execute(query)

        #selecciono los datos de la tabla temporal
        query = "select * from tcajeros"
        self.cur.execute(query)

        #traigo todos los registros
        resultados = self.cur.fetchall()

        #recorro y voy grabando los cajeros
        for registro in resultados:
            #busco el banco relacionado para cargar su id
            query = "select id from bancos where banco = %s"
            self.cur.execute(query, [registro[0]])
            banco = self.cur.fetchone()

            #busco la red relacionada para cargar su id
            query = "select id from redes where red = %s"
            self.cur.execute(query, [registro[1]])
            red = self.cur.fetchone()

            #cargo los parametros
            parametros = [registro[2], registro[3], registro[6], registro[7], 1, banco[0], red[0]]
            query = "insert into cajeros "\
                    "(direccion, terminales, longitud, latitud, barrio, banco, red)"\
                    "values ( %s, %s, %s, %s, %s, %s, %s)"
            self.cur.execute(query, parametros)

        #por ultimo grabo todos los cambios a la base de datos
        self.conn.commit()


    def EliminoTablasCajero(self):
        query = "drop table if exists cajeros"
        self.cur.execute(query)

        query = "drop table if exists redes"
        self.cur.execute(query)

        query = "drop table if exists bancos"
        self.cur.execute(query)