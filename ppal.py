#!/usr/bin/python
# -*- coding: utf-8 -*-


import wx
import wx.xrc
import importa_cajeros
import importa_barrios
import Normaliza
import buscacajeros

ID_IMPORTACAJERO = 1001
ID_IMPORTABARRIO = 1002
ID_NORMBARRIOS = 1003
ID_NORMCAJEROS = 1004
ID_MODCAJERO = 1005

class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        kwargs['style'] = wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.TAB_TRAVERSAL
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileMenu.AppendSeparator()

        imp = wx.Menu()
        imp.Append(ID_IMPORTACAJERO, 'Importa cajeros...')
        imp.Append(ID_IMPORTABARRIO, 'Importa barrios...')

        fileMenu.AppendMenu(wx.ID_ANY, 'I&mportar', imp)

        norm = wx.Menu()
        norm.Append(ID_NORMBARRIOS, 'Normaliza Barrios...')
        norm.Append(ID_NORMCAJEROS, 'Normaliza Cajeros...')

        fileMenu.AppendMenu(wx.ID_ANY, "&Normaliza tablas", norm)
        fileMenu.AppendSeparator()

        fitem = fileMenu.Append(wx.ID_EXIT, 'Salir', 'Sale de la aplicacion')

        fileMod = wx.Menu()
        fileMod.Append(ID_MODCAJERO, 'Modifica', 'Modifica la tabla de cajeros')

        menubar.Append(fileMenu, '&Archivo')
        menubar.Append(fileMod, '&Modificar')
        self.SetMenuBar(menubar)

        #establezco que debe hacer cada opcion del menu
        self.Bind(wx.EVT_MENU, self.OnQuit, fitem)
        self.Bind(wx.EVT_MENU, self.OnImportaCajeros, id = ID_IMPORTACAJERO)
        self.Bind(wx.EVT_MENU, self.OnImportaBarrios, id = ID_IMPORTABARRIO)
        self.Bind(wx.EVT_MENU, self.OnNormalizaBarrios, id = ID_NORMBARRIOS)
        self.Bind(wx.EVT_MENU, self.OnNormalizaCajeros, id = ID_NORMCAJEROS)
        self.Bind(wx.EVT_MENU, self.OnModificaCajeros, id = ID_MODCAJERO)

        #creo un barra de status
        self.statusbar = self.CreateStatusBar()

        #establezco un texto en la barra
        self.statusbar.SetStatusText('Seleccione una opcion del menu')

        #self.SetSize((800, 600))
        self.SetTitle('Aplicacion')
        self.Centre()

        self.Show(True)

    def OnQuit(self, e):
        self.Close()

    def OnImportaCajeros(self, e):
        imp = importa_cajeros.ImportaCajeros()
        imp.Importa()

    def OnImportaBarrios(self, e):
        imp = importa_barrios.ImportaBarrios()
        imp.Importa()

    def OnNormalizaBarrios(self, e):
        nor = Normaliza.Normaliza()
        nor.NormalizaBarrios()

    def OnNormalizaCajeros(self, e):
        nor = Normaliza.Normaliza()
        nor.NormalizaCajeros()

    def OnModificaCajeros(self, e):
        buscacajeros.BuscarCajeros(self, title="Modifica Cajeros")


def main():

    ex = wx.App()
    Example(None)
    ex.MainLoop()


if __name__ == '__main__':
    main()