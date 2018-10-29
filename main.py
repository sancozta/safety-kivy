# -*- coding: utf-8 -*-
import manager
from kivy.app import App
import kivy

# CLASSE PRINCIPAL
class Aplicativo(App):
    def build(self):
        return manager.inicarGerenciador()

# INICAR APLICATIVO
Aplicativo().run()
