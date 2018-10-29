# -*- coding: utf-8 -*-
from threading import Thread
from kivy.uix.screenmanager import Screen
from api import api
from home import home
import manager

# SALVAR DADOS DO USUARIO
DadosUsuario = []

class TelaLogin(Screen):

    # BUILD
    def build(self):
        pass

    # ERRO LOGIN
    def erroLogin(self, msg):
        self.ids["msg"].text = msg

    # REALIZAR LOGIN
    def processarLogin(self):
        self.ids["msg"].text            = ""
        self.ids["bt_login"].text       = "Conectando ..."
        self.ids["bt_login"].disabled   = True
        
        email = self.ids["ti_email"].text
        senha = self.ids["ti_senha"].text

        DadosLogin = api.loginUser(email, senha)

        self.ids["bt_login"].disabled = False
        self.ids["bt_login"].text = "Login"

        if not DadosLogin:
            self.erroLogin("E-mail ou senha incorreta")
        elif DadosLogin[0] == "erro":
            self.erroLogin("Conecte-se à internet")
        else:
            manager.alterarTelaAtual(tela="TelaHome", direcao="left", efeito=True)
            home.carregarDados(DadosLogin)
    
    # INICIAR PROCESSO DE LOGIN
    def logar(self):
        Thread(target=self.processarLogin).start()