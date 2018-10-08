# -*- coding: utf-8 -*-
import kivy
from kivy.app import App
import gerenciador


# classe principal
class Aplicativo(App):
    def build(self):
        return gerenciador.inicar_gerenciador()


# inicar aplicativo
Aplicativo().run()
