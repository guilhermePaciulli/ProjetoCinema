# -*- coding: utf-8 -*-

from gui import menu_sessao
from gui import menu_ator
from gui import menu_filme
from gui import menu_sala
from gui import menu_elenco
from gui import menu_ingresso

from logica import sessao
from logica import ator
from logica import filme
from logica import sala
from logica import elenco
from logica import ingresso

def start():
    #Initial SetUp
    sala.iniciar_salas()
    ator.iniciar_atores()
    filme.iniciar_filmes()
    elenco.iniciar_elencos()
    sessao.iniciar_sessoes()
    ingresso.iniciar_ingressos()

    while True:
        print("Bem vindo ao CineMania")
        print("1 - Ingressos")
        print("2 - Sessão")
        print("3 - Filme")
        print("4 - Elenco")
        print("5 - Sala")
        print("6 - Ator")
        print("7 - Sair")
        option = int(input("Para onde você quer ir? "))
        while(option < 1 or option > 7):
            option = int(input("Insira um valor válido "))
        if option == 1:
            menu_ingresso.menu()
        elif option == 2:
            menu_sessao.menu()
        elif option == 3:
            menu_filme.menu()
        elif option == 4:
            menu_elenco.menu()
        elif option == 5:
            menu_sala.menu()
        elif option == 6:
            menu_ator.menu()
        else:
            break
