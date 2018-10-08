# -*- coding: utf-8 -*-
from threading import Thread
from kivy.uix.screenmanager import Screen
import gerenciador
from api import dados
from home import home



dados_usuario = []

class TelaLogin(Screen):
    def build(self):
        pass

    def erro_login(self, msg):
        self.ids['msg'].text = msg



    def processar_login(self):
        self.ids['msg'].text = ""
        self.ids['bt_login'].text = 'Conectando ...'
        self.ids['bt_login'].disabled = True
        email = self.ids['ti_email'].text;
        senha = self.ids['ti_senha'].text;

        dados_login = dados.login(email, senha)
        self.ids['bt_login'].disabled = False
        self.ids['bt_login'].text = 'Login'

        if not dados_login:
            self.erro_login('E-mail ou senha incorreta')

        elif dados_login[0] == 'erro':
            self.erro_login('Conecte-se à internet')

        else:
            gerenciador.alterar_tela_atual(tela='TelaHome', direcao='left', efeito=True)
            home.carregar_dados(dados_login)




    def logar(self):
        Thread(target=self.processar_login).start()





