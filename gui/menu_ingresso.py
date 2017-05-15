# -*- coding: utf-8 -*-

from logica import sessao
from logica import filme
from logica import ingresso
import menu_inicial

def menu_vender_ingresso_meia():
    print("\nVender ingresso meia:\n")
    cod_sessao = int(input("Digite o código da sessão:"))
    comprovante = input("Digite o comprovante de meia:")
    b = ingresso.venda_ingresso_meia(cod_sessao)
    if b == None:
        print("Código de sessão inválido!")
    elif b == False:
        print("Sessão lotada!")
    else:
        print("\nVenda concluída com sucesso!\n")

def menu_vender_ingresso_inteira():
    print("\nVender ingresso inteira:\n")
    cod_sessao = int(input("Digite o código da sessão:"))
    b = ingresso.venda_ingresso_inteira(cod_sessao)
    if b == None:
        print("Código de sessão inválido!")
    elif b == False:
        print("Sessão lotada!")
    else:
        print("\nVenda concluída com sucesso!\n")

def _imprimir_ingresso(ingresso):
    print("Código da sessão:",ingresso[0])
    print("Código do ingresso:",ingresso[1])
    print("")

def menu_buscar_ingresso():
    print("\nBuscar ingresso por código:\n")
    cod_ingresso = int(input("Digite o código do ingresso:"))
    ingresso = ingresso.buscar_ingresso(cod_ingresso)
    if (cod_ingresso == None):
        print("Ingresso não encontrada!")
    else:
        _imprimir_ingresso(ingresso)

def menu_listar_ingressos():
    print("\nListar ingressos:\n")
    ingressos = ingresso.listar_ingressos()
    for i in ingressos:
        _imprimir_ingresso(i)

def menu_listar_ingressos_vendidos():
    print("\nListar ingressos vendidos por sessão:\n")
    cod_sessao = int(input("Digite a sessão desejada:"))
    ingressos = ingresso.listar_ingressos_vendidos(cod_sessao)
    for i in ingressos:
        _imprimir_ingresso(i)

def menu_remover_ingresso():
    print("\nRemover Ingresso:\n")
    cod_ingresso = int(input("Digite o código do ingresso:"))
    i = ingresso.remover_ingreso(cod_ingresso)
    if i == False:
        print("Ingresso não encontrado!")
    else:
        print("Ingresso Removido!")

def menu_remover_todos_ingressos():
    ingresso.remover_todos_ingresso()
    print("Todos os ingressos foram removidos do banco de dados!")

def menu():
    while(True):
        print("1 - Vender ingresso meia")
        print("2 - Vender ingresso inteira")
        print("3 - Buscar ingresso por código")
        print("4 - Listar ingressos")
        print("5 - Listar ingressos vendidos por sessão")
        print("6 - Remover ingresso")
        print("7 - Remover todos os ingressos")
        print("8 - Voltar")

        op = int(input("Digite sua escolha: "))

        while op < 1 or op > 8:
            op = int(input("Entre com uma escolha válida: "))

        if(op == 1):
            menu_vender_ingresso_meia()
        elif(op == 2):
            menu_vender_ingresso_inteira()
        elif(op == 3):
            menu_buscar_ingresso()
        elif(op == 4):
            menu_listar_ingressos()
        elif(op == 5):
            menu_listar_ingressos_vendidos()
        elif(op == 6):
            menu_remover_ingresso()
        elif(op == 7):
            menu_remover_todos_ingressos
        elif(op == 8):
            break
