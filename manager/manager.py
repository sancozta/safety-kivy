# -*- coding: utf-8 -*-
from kivy.uix.screenmanager import ScreenManager, SwapTransition, SlideTransition
from home.home import TelaHome
from login.login import TelaLogin
from kivy.lang import Builder

# TEMPO DE TRANSCICAO
TempoTransicao = 0.4

# OBJECT SCREEN MANAGER
sm = ScreenManager()

# CARREGA OS ARQUIVOS DE LAYOUT .KV
def carregarTelas():
    Builder.load_file("login/login.kv")
    Builder.load_file("home/home.kv")

# ADICIONA AS TELAS NO OBJETO SCREENMANAGER
def adicionarTelas(sm):
    sm.add_widget(TelaLogin(name="TelaLogin"))
    sm.add_widget(TelaHome(name="TelaHome"))

# ALTERAR TELA
def alterarTelaAtual(tela, direcao, efeito=False):
    if efeito:
        sm.transition = SwapTransition(duration=TempoTransicao)
    else:
        sm.transition = SlideTransition()
    sm.transition.direction = direcao
    sm.current = tela

# INIT SCREEN
def inicarGerenciador():
    carregarTelas()
    adicionarTelas(sm)
    return sm
