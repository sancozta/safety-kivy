# -*- coding: utf-8 -*-
from kivy.uix.screenmanager import ScreenManager, SwapTransition, SlideTransition

from home.home import TelaHome
from login.login import TelaLogin
from kivy.lang import Builder
tempo_transicao = 0.4
sm = ScreenManager()


def teste():
    print("teste")

# carrega os arquivos de layout .kv
def carregar_telas():
    Builder.load_file('login/telalogin.kv')
    Builder.load_file('home/telahome.kv')


# adiciona as telas no objeto ScreenManager
def adicionarTelas(sm):
    sm.add_widget(TelaLogin(name='TelaLogin'))
    sm.add_widget(TelaHome(name='TelaHome'))



def alterar_tela_atual(tela, direcao, efeito=False):
    if efeito:
        sm.transition = SwapTransition(duration=tempo_transicao)
    else:
        sm.transition = SlideTransition()
    sm.transition.direction = direcao
    sm.current = tela


def inicar_gerenciador():
    # gerenciador de telas
    carregar_telas()
    adicionarTelas(sm)
    return sm
