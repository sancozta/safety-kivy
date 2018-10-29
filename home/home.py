# -*- coding: utf-8 -*-
from threading import Thread
from kivy.uix.screenmanager import Screen
from api import api
import manager


idUser      = []
nomeUser    = []
flag    = []

class TelaHome(Screen):

    # LOGOUT
    def sair(self):

        # LIMPA OS DADOS DO LOGIN
        self.ids["list"].adapter.data = ["Clique abaixo para atualizar"]
        self.ids["name"].text = "-"
        self.ids["flag"].disabled = True
        self.ids["flag"].text = '...'
        # RETORNA PARA TELA DE LOGIN
        manager.alterarTelaAtual(tela="TelaLogin", direcao="right")

    # DEFINIR USUARIO
    def setUsuario(self, dados):

        # USAR AS VARIAVEIS GLOBAIS NESTE MÉTODO
        global idUser
        global nomeUser
        global flag

        # DEFINE OS DADOS DO USUARIO
        nomeUser    = dados[0]["name"]
        idUser      = dados[0]["id"]
        flag        = dados[0]["token"]

    # CARREGAR LOGS
    def carregar(self):

        global idUser


        dadosUsuario = api.getDeteccoes(str(idUser))
        flag = api.getFlag(idUser)

        self.ids["name"].text = nomeUser
        self.ids["list"].adapter.data = []



        if str(flag) != "1":
            self.ids["flag"].text = 'ON'
            self.ids["flag"].background_color=(.3, .9, .3, 1.0)

        else:
            self.ids["flag"].text = 'OFF'
            self.ids["flag"].background_color = (1, .1, .1, 1.0)


        self.ids["flag"].disabled = False
        self.ids["atualizar"].disabled = False
        self.ids["atualizar"].text = 'Atualizar'
        for i in dadosUsuario:
            self.ids["list"].adapter.data.append(i["registry"])

    # ATUALIZAR DADOS DE LOGS
    def atualizarDados(self):

        self.ids["list"].adapter.data = []
        self.ids["list"].adapter.data.append("Atualizando ...")

        self.ids["atualizar"].disabled = True
        self.ids["atualizar"].text = 'Atualizando ...'

        Thread(target=self.carregar).start()

        # ATUALIZAR DADOS DE LOGS






    def flag(self):
        global idUser
        global nomeUser
        global flag
        textoBotao = self.ids["flag"].text

        novaFlag = "1" if textoBotao == 'ON' else "0"


        try:
            if (api.updateFlag(idUser, novaFlag)['message']=='Update Flag Sucess'):

                if str(novaFlag) != "1":
                    self.ids["flag"].text = 'ON'
                    self.ids["flag"].background_color = (.3, .9, .3, 1.0)

                else:
                    self.ids["flag"].text = 'OFF'
                    self.ids["flag"].background_color = (1, .1, .1, 1.0)

            else:
                self.ids["flag"].text = "OFF"
        except:
            pass

        self.ids["flag"].disabled = False

    def atualizarFlag(self):
        self.ids["flag"].disabled = True
        Thread(target=self.flag).start()

# CARREGAR DADOS
def carregarDados(dados):
    TelaHome.setUsuario(TelaHome(), dados)
