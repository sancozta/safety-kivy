# -*- coding: utf-8 -*-
from threading import Thread
from kivy.uix.screenmanager import Screen
from api import api
from manager import manager

idUser      = []
nomeUser    = []

class TelaHome(Screen):

    # LOGOUT
    def sair(self):

        # LIMPA OS DADOS DA LISTA
        self.ids["list"].adapter.data = ["Clique abaixo para atualizar"]

        # RETORNA PARA TELA DE LOGIN
        manager.alterarTelaAtual(tela="TelaLogin", direcao="right")

    # DEFINIR USUARIO
    def setUsuario(self, dados):

        # USAR AS VARIAVEIS GLOBAIS NESTE MÉTODO
        global idUser
        global nomeUser

        # DEFINE OS DADOS DO USUARIO
        nomeUser    = dados[0]["name"]
        idUser      = dados[0]["id"]

    # CARREGAR LOGS
    def carregar(self):

        global idUser
        
        dadosUsuario = api.getDeteccoes(str(idUser))
        self.ids["name"].text = nomeUser
        self.ids["list"].adapter.data = []
        
        for i in dadosUsuario:
            self.ids["list"].adapter.data.append(i["registry"])

    # ATUALIZAR DADOS DE LOGS
    def atualizarDados(self):

        self.ids["list"].adapter.data = []
        self.ids["list"].adapter.data.append("Atualizando ...")

        Thread(target=self.carregar).start()

# CARREGAR DADOS
def carregarDados(dados):
    TelaHome.setUsuario(TelaHome(), dados)
