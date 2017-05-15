# -*- coding: utf-8 -*-

import menu_inicial
from logica import sala

def menu_adicionar_sala():
    print("\nAdicionar sala:")
    cod_sala = int(input("Digite o código da sala:"))
    lotacao = int(input("Digite a lotação da sala:"))
    sala.salas.append(cod_sala,lotacao)

def menu_sala_ocupada():
    print("\nTornar sala ocupada:\n")
    cod_sala = int(input("Digite o código da sala:"))
    sala.definir_status_ocupada(cod_sala)

def menu_sala_livre():
    print("\nTornar sala livre:\n")
    cod_sala = int(input("Digite o código da sala:"))
    sala.definir_status_livre(cod_sala)

def _imprimir_sala(sala):
    print("Código da sala:", sala[0])
    print("Lotação da sala:",sala[1])
    if sala[2] == True:
        print("Sala completamente ocupada!")
    else:
        print("Sala vazia ou com lugares ainda disponíveis!")

def menu_buscar_sala():
    print("\nBuscar sala por código/:\n")
    cod_sala = int(input("Digite o código da sala:"))
    sala = sala.buscar_sala(cod_sala)
    if (cod_sala == None):
        print("Sala não encontrada!")
    else:
        _imprimir_sala(cod_sala)

def menu_listar_salas():
    print("\nListar salas:\n")
    salas = sala.listar_salas()
    for s in salas:
        _imprimir_sala(s)

def menu_remover_sala():
    print("\nRemover sala:\n")
    cod_sala = int(input("Digite o código da sala:"))
    s = sala.remover_sala(cod_sala)
    if (s == False):
        print("Sala não encontrada!")
    else:
        print("Sala removida!")

def menu_remover_todas_salas():
    sala.remover_todas_salas()
    print("Todas as salas foram apagadas do banco de dados!")

def menu():
    while(True):
        print("1 - Adicionar nova sala")
        print("2 - Tornar sala ocupada")
        print("3 - Tornar sala livre")
        print("4 - Buscar sala")
        print("5 - Listar salas")
        print("6 - Remover sala por código")
        print("7 - Remover todas as salas")
        print("8 - Voltar")

        op = int(input("Digite sua escolha: "))

        while op < 1 or op > 8:
            op = int(input("Entre com uma escolha válida: "))

        if(op == 1):
            menu_adicionar_sala()()
        elif(op == 2):
            menu_sala_ocupada()
        elif(op == 3):
            menu_sala_livre()
        elif(op == 4):
            menu_buscar_sala()
        elif(op == 5):
            menu_listar_salas()
        elif(op == 6):
            menu_remover_sala()
        elif(op == 7):
            menu_remover_todas_salas()
        elif(op == 8):
            break
