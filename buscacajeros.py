#! /usr/bin/python
#encoding:utf-8

import wx, wx.grid
import db
import modificacajeros


class BuscarCajeros(wx.Frame):
    db = db.Modelo()
    conn = db.Conectar()
    cur = conn.cursor()

    def __init__(self, parent, title):
        super(BuscarCajeros, self).__init__(parent, title=title,
            size=(750, 580))
        self.InitUi()
        self.Centre()
        self.Show(True)

    def InitUi(self):

        #definimos el panel principal
        panel = wx.Panel(self, -1)
        vbox = wx.BoxSizer(wx.VERTICAL)

        #creamos un sizer para la busqueda
        busqSizer = wx.BoxSizer(wx.HORIZONTAL)
        #establecemos el label
        st1 = wx.StaticText(panel, label='Buscar direccion')
        #lo agregamos al sizer
        busqSizer.Add(st1, flag=wx.RIGHT, border=8)
        #creamos una caja de texto
        self.tc = wx.TextCtrl(panel)
        busqSizer.Add(self.tc, proportion=1)
        #agregamos un boton
        button1 = wx.Button(panel, label="Buscar...")
        busqSizer.Add(button1, flag=wx.TOP|wx.RIGHT, border=8)

        #hacemos que cuando se presione el boton buscar nos llame al metodo OnBuscar
        self.Bind(wx.EVT_BUTTON, self.OnBuscar, id = button1.GetId())
        #añadimos la grilla
        self.grid = wx.grid.Grid(panel, -1, size=(500,400))
        grid = self.grid
        #creamos la grilla
        grid.CreateGrid(0, 5)
        #cargamos los datos a la grilla
        self.ArmaGrilla()

        #Añadimos los botones
        BtnSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.crearBotones(panel, BtnSizer)
        #closeBtn = wx.Button(panel, -1, 'Cerrar')
        #closeBtn.Bind(wx.EVT_BUTTON, self.onClose)
        #BtnSizer.Add(closeBtn, 0, wx.ALL, 5)
        vbox.Add(busqSizer, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add(self.gridTableSizer, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        vbox.Add(BtnSizer, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        panel.SetSizer(vbox)


    def datosBotones(self):
        """ Define el rótulo y el manejador de evento del botón """
        return (
                ('', ''), # un espaciador
                ('Guardar', self.guardarRegistro),
                ('Eliminar', self.eliminarRegistro),
                ('Modificar', self.modificaRegistro),
                ('Limpiar', self.limpiarRejilla),
                ('',''),
                ('Cerrar', self.cerrar),
                ('', '')
               )

    def crearBotones(self,panel,sizer):
        """ Crea y posiciona los botones de la interfaz """
        for etiqueta, manejador in self.datosBotones():
            # Si no existe etiqueta, añadir un espaciador
            # y continuar con la siguiente tupla
            if not etiqueta:
                sizer.Add((20, 20), 1, wx.EXPAND)
                continue
            boton = wx.Button(panel, -1, etiqueta)
            self.Bind(wx.EVT_BUTTON, manejador, boton)
            sizer.Add(boton, 0, wx.EXPAND|wx.TOP|wx.LEFT|wx.BOTTOM, 3)

    def cerrar(self, event):
        self.Close()

    def OnBuscar(self, e):
        self.ArmaGrilla(self.tc.GetValue().upper())

    # Plantilla para los manejadores de evento de los botones
    def guardarRegistro(self, event):
        # obtener el índice de la fila seleccionada.
        fila = self.GetSelectedRows()[0]
        # desempaquetar los datos utilizando una comprensión de lista
        id, direccion, terminales, latitud, longitud = [self.grid.GetCellValue(fila, col)
                                      for col in xrange(self.numCols)]
        datos1 = (direccion, terminales, latitud, longitud)
        # datos requeridos por insertar
        datos2 = (direccion, terminales, latitud, longitud, id)
        # datos requeridos por actualizar
        # si no existe el id, es un nuevo registro y se inserta
        if not id:
            id = self.db.insertarCajero(datos1)
            # si existe el id, el registro es actualizado
        else:
            self.db.actualizarCajero(datos2)
        # mostrar el registro actualizado
        #self.refrescarRegistro(id, fila)


    def GetSelectedRows(self):
        """Ejemplo tomado desde http://wxpython-users.1045709.n5.nabble.com/BUG-wx-Grid-GetSelectedRows-broken-td2303648.html
        debido a que el GetSelectedRows al estar editando una celda me devolvia siempre []
        """
        rows=[]
        gcr=self.grid.GetGridCursorRow()
        set1=self.grid.GetSelectionBlockTopLeft()
        set2=self.grid.GetSelectionBlockBottomRight()
        if len(set1):
            assert len(set1)==len(set2)
            for i in range(len(set1)):
                for row in range(set1[i][0], set2[i][0]+1): # range in wx is inclusive of last element
                    if row not in rows:
                        rows.append(row)
        else:
             rows.append(gcr)
        return rows


    def refrescarRegistro(self, id, fila):
        registro = self.db.seleccionar(id)
        for dato in registro:
            for col, valor in enumerate(dato):
                self.grid.SetCellValue(fila, col, valor)

    def eliminarRegistro(self, event):
        # Obtener el índice de la fila del registro
        fila = self.GetSelectedRows()[0]
        # Obtener la id del registro
        id = self.grid.GetCellValue(fila, 0)
        self.db.eliminarCajero(id)
        # Borrar la fila de la rejilla
        self.grid.DeleteRows(fila, 1)

    def modificaRegistro(self, event):
        # obtener el índice de la fila seleccionada.
        fila = self.GetSelectedRows()[0]
        # desempaquetar los datos utilizando una comprensión de lista
        idCajero = self.grid.GetCellValue(fila, 0)
        mCa = modificacajeros.ModificaCajero(self)
        mCa.CargaValores(idCajero)
        print idCajero

    def limpiarRejilla(self, event):
        pass

    def ArmaGrilla(self, condicion = ""):
        self.numFilas = self.grid.GetNumberRows()
        self.numCols = self.grid.GetNumberCols()

        if condicion:
            query = "select id, direccion, terminales, longitud, latitud "\
                " from cajeros " \
                " where direccion like '%" + condicion + "%'" \
                " order by direccion"
            self.cur.execute(query)
        else:
            self.cur.execute("select id, direccion, terminales, longitud, latitud "\
                "from cajeros order by direccion")
        resultado = self.cur.fetchall()

        grid = self.grid
        #creamos las filas y las columnas
        grid.ClearGrid()

        actual, nuevo = (self.grid.GetNumberRows(), len(resultado))

        if nuevo < actual:
            #- Borro filas:
            self.grid.DeleteRows(0, actual - nuevo, True)

        if nuevo > actual:
            #- agrego filas:
            self.grid.AppendRows(nuevo - actual)

        #definimos los campos que contendra el grid
        grid.SetColLabelValue(0, 'ID')
        grid.SetColLabelValue(1, 'Direccion')
        grid.SetColLabelValue(2, 'Terminales')
        grid.SetColLabelValue(4, 'Longitud')
        grid.SetColLabelValue(5, 'Latitud')

        #definimos los tamaños
        grid.SetRowLabelSize(50)
        grid.SetColSize(0,30)
        grid.SetColSize(1,150)
        grid.SetColSize(2,50)
        grid.SetColSize(3,150)
        grid.SetColSize(4,150)

        self.gridTableSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.gridTableSizer.Add(grid, wx.ALIGN_CENTER | wx.ALL,0)

        # Añadimos los campos de la base de datos a las columnas
        for i in range(0,len(resultado)):
            grid.SetCellValue(i,0,"%s" % resultado[i][0])
            grid.SetCellValue(i,1,"%s" % resultado[i][1])
            grid.SetCellValue(i,2,"%s" % resultado[i][2])
            grid.SetCellValue(i,3,"%s" % resultado[i][3])
            grid.SetCellValue(i,4,"%s" % resultado[i][4])
        self.Refresh()

if __name__ == "__main__":
    app = wx.App()
    BuscarCajeros(None, title="Modifica Cajeros")
    app.MainLoop()
