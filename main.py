# -*- coding: utf-8 -*-
from manager import manager
from kivy.app import App
import kivy

# CLASSE PRINCIPAL
class Aplicativo(App):
    def build(self):
        return manager.inicarGerenciador()

# INICAR APLICATIVO
Aplicativo().run()
