#! /usr/bin/python
# -*- coding: utf-8 -*-

import wx
import db

class ModificaCajero(wx.Frame):

    db = db.Modelo()
    conn = db.Conectar()
    cur = conn.cursor()
    idCajero = 0

    def __init__(self, parent):

	wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 699,508 ), style = wx.TAB_TRAVERSAL )
	
	bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
	
	sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Modificacion de Datos" ), wx.HORIZONTAL )
	
	gSizer1 = wx.GridSizer( 9, 2, 0, 0 )
	
	self.m_staticText3 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Direccion", wx.DefaultPosition, wx.DefaultSize, 0 )
	self.m_staticText3.Wrap( -1 )
	gSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )
	
	self.txtDir = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
	gSizer1.Add( self.txtDir, 0, wx.ALL|wx.EXPAND, 5 )
	
	self.m_staticText4 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Terminales", wx.DefaultPosition, wx.DefaultSize, 0 )
	self.m_staticText4.Wrap( -1 )
	gSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )
	
	self.txtTerminales = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
	gSizer1.Add( self.txtTerminales, 0, wx.ALL|wx.EXPAND, 5 )
	
	self.m_staticText5 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Actualizacion", wx.DefaultPosition, wx.DefaultSize, 0 )
	self.m_staticText5.Wrap( -1 )
	gSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )
	
	self.txtActualizacion = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
	gSizer1.Add( self.txtActualizacion, 0, wx.ALL|wx.EXPAND, 5 )
	
	self.m_staticText6 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Longitud", wx.DefaultPosition, wx.DefaultSize, 0 )
	self.m_staticText6.Wrap( -1 )
	gSizer1.Add( self.m_staticText6, 0, wx.ALL, 5 )
	
	self.txtLong = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
	gSizer1.Add( self.txtLong, 0, wx.ALL|wx.EXPAND, 5 )
	
	self.m_staticText8 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Latitud", wx.DefaultPosition, wx.DefaultSize, 0 )
	self.m_staticText8.Wrap( -1 )
	gSizer1.Add( self.m_staticText8, 0, wx.ALL, 5 )
	
	self.txtLat = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
	gSizer1.Add( self.txtLat, 0, wx.ALL|wx.EXPAND, 5 )
	
	self.m_staticText9 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Barrio", wx.DefaultPosition, wx.DefaultSize, 0 )
	self.m_staticText9.Wrap( -1 )
	gSizer1.Add( self.m_staticText9, 0, wx.ALL, 5 )
	
	self.txtBarrio = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
	gSizer1.Add( self.txtBarrio, 0, wx.ALL|wx.EXPAND, 5 )
	
	self.m_staticText10 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Banco", wx.DefaultPosition, wx.DefaultSize, 0 )
	self.m_staticText10.Wrap( -1 )
	gSizer1.Add( self.m_staticText10, 0, wx.ALL, 5 )
	
	self.txtBanco = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
	gSizer1.Add( self.txtBanco, 0, wx.ALL|wx.EXPAND, 5 )
	
	self.m_staticText11 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Red", wx.DefaultPosition, wx.DefaultSize, 0 )
	self.m_staticText11.Wrap( -1 )
	gSizer1.Add( self.m_staticText11, 0, wx.ALL, 5 )
	
	self.txtRed = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
	gSizer1.Add( self.txtRed, 0, wx.ALL|wx.EXPAND, 5 )
	
	bSizer7 = wx.BoxSizer( wx.VERTICAL )
	
	self.btnAceptar = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.DefaultSize, 0 )
	bSizer7.Add( self.btnAceptar, 0, wx.ALL|wx.EXPAND, 5 )
	
	
	gSizer1.Add( bSizer7, 1, wx.EXPAND, 5 )
	
	bSizer8 = wx.BoxSizer( wx.VERTICAL )
	
	self.btnCancelar = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
	bSizer8.Add( self.btnCancelar, 0, wx.ALL|wx.EXPAND, 5 )
	
	
	gSizer1.Add( bSizer8, 1, wx.EXPAND, 5 )
	
	
	sbSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )
	
	
	bSizer1.Add( sbSizer1, 1, wx.EXPAND, 5 )
	
	
	self.SetSizer( bSizer1 )
	self.Layout()
	
	# Connect Events
	self.btnAceptar.Bind( wx.EVT_BUTTON, self.btnAceptarOnButtonClick )
	self.btnCancelar.Bind( wx.EVT_BUTTON, self.onClose )

        self.SetSizer( bSizer1 )
        self.Layout()
        self.Centre()
        self.Show()

    def __del__( self ):
        pass

    # Virtual event handlers, overide them in your derived class
    def btnAceptarOnButtonClick( self, event ):
    	event.Skip()


    def CargaValores(self, idCajero):
        self.idCajero = idCajero
        self.registros = self.db.seleccionar(self.idCajero)
        print self.registros[0][2]
        self.txtDir.SetValue(self.registros[0][1])
        self.txtTerminales.SetValue(str(self.registros[0][2]))
        self.txtActualizacion.SetValue(str(self.registros[0][3]))
        self.txtLong.SetValue(str(self.registros[0][4]))
        self.txtLat.SetValue(str(self.registros[0][5]))
        self.txtBarrio.SetValue(str(self.registros[0][6]))
        self.txtBanco.SetValue(str(self.registros[0][7]))
        self.txtRed.SetValue(str(self.registros[0][8]))

    def onClose(self, event):
        self.Close()

        # Virtual event handlers, overide them in your derived class
    def btnAceptarOnButtonClick( self, event ):
        parametros = [self.txtDir.GetValue(), self.txtTerminales.GetValue(),
            self.txtLong.GetValue(),
            self.txtLat.GetValue(), self.txtBarrio.GetValue(),
            self.txtBanco.GetValue(), self.txtRed.GetValue(), self.idCajero]
        self.db.actualizaDatosCajero(parametros)
        self.Close()
