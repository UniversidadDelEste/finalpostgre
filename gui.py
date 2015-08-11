# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Nov 10 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

ID_IMPORTAR = 1000
ID_BUSQUEDA = 1001
ID_SALIR = 1002

###########################################################################
## Class Ppal
###########################################################################

class Ppal ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.archivo = wx.Menu()
		self.importar = wx.MenuItem( self.archivo, ID_IMPORTAR, u"Importar", u"Importa el archivo CSV a la base de datos", wx.ITEM_NORMAL )
		self.archivo.AppendItem( self.importar )
		
		self.busqueda = wx.MenuItem( self.archivo, ID_BUSQUEDA, u"Busqueda", u"Busqueda de calles", wx.ITEM_NORMAL )
		self.archivo.AppendItem( self.busqueda )
		
		self.archivo.AppendSeparator()
		
		self.salir = wx.MenuItem( self.archivo, ID_SALIR, u"Salir"+ u"\t" + u"Alt+F4", wx.EmptyString, wx.ITEM_NORMAL )
		self.archivo.AppendItem( self.salir )
		
		self.m_menubar1.Append( self.archivo, u"Archivo" ) 
		
		self.reportes = wx.Menu()
		self.m_menubar1.Append( self.reportes, u"Reportes" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.importarOnMenuSelection, id = self.importar.GetId() )
		self.Bind( wx.EVT_MENU, self.busquedaOnMenuSelection, id = self.busqueda.GetId() )
		self.Bind( wx.EVT_MENU, self.salirOnMenuSelection, id = self.salir.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def importarOnMenuSelection( self, event ):
		event.Skip()
	
	def busquedaOnMenuSelection( self, event ):
		event.Skip()
	
	def salirOnMenuSelection( self, event ):
		event.Skip()
	

###########################################################################
## Class PanelBusqueda
###########################################################################

class PanelBusqueda ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,106 ), style = wx.TAB_TRAVERSAL )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.SelecionaArchivo = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Selecciona un archivo", u"*.csv", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN )
		bSizer3.Add( self.SelecionaArchivo, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnOK = wx.Button( self, wx.ID_ANY, u"Procesar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btnOK, 0, wx.ALL, 5 )
		
		self.btnCancelar = wx.Button( self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btnCancelar, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		# Connect Events
		self.SelecionaArchivo.Bind( wx.EVT_FILEPICKER_CHANGED, self.SelecionaArchivoOnFileChanged )
		self.btnOK.Bind( wx.EVT_BUTTON, self.btnOKOnButtonClick )
		self.btnCancelar.Bind( wx.EVT_BUTTON, self.btnCancelarOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def SelecionaArchivoOnFileChanged( self, event ):
		event.Skip()
	
	def btnOKOnButtonClick( self, event ):
		event.Skip()
	
	def btnCancelarOnButtonClick( self, event ):
		event.Skip()
	

