# -*- coding: utf-8 -*-
from threading import Thread

from kivy.uix.screenmanager import Screen
import gerenciador
from api import dados

id_user = []
nome = []

class TelaHome(Screen):



    def sair(self):
        #limpa os dados da lista
        self.ids['list'].adapter.data = ['Clique abaixo para atualizar']
        #retorna para tela de login
        gerenciador.alterar_tela_atual(tela='TelaLogin', direcao='right')

    def set_usuario(self, dados):
        #usar as variaveis globais neste método
        global id_user
        global nome

        #define os dados do usuário
        nome = dados[0]['name']
        id_user = dados[0]['id']


    def carregar(self):
        global id_user
        dados_usuario = dados.get_deteccoes(str(id_user))

        self.ids['nome_usuario'].text = nome
        self.ids['list'].adapter.data = []
        for i in dados_usuario:
            self.ids['list'].adapter.data.append(i['registry'])

    def atualizar_dados(self):

        self.ids['list'].adapter.data = []
        self.ids['list'].adapter.data.append('Atualizando ...')

        Thread(target=self.carregar).start()


def carregar_dados(dados_login):
    TelaHome.set_usuario(TelaHome(), dados_login)


