# -*- coding: utf-8 -*-

from logica import ator

def menu_adicionar_ator():
    print("\nAdicionar ator:\n")
    cod_ator = (input("Digite o código do ator:"))
    nome = input("Digite o nome do ator:")
    nacionalidade = input("Digite a nacionalidade:")
    idade = input("Digite a idade:")
    ator.cadastrar_ator(cod_ator,nome,nacionalidade,idade)

def _imprimir_ator(ator):
    print("Código do ator:",ator[0])
    print("Nome do ator:",ator[1])
    print("Nacionalidade do ator:",ator[2])
    print("Idade do ator:",ator[3])
    print()

def menu_buscar_ator():
    print("\nBuscar ator por código:\n")
    cod_ator = (input("Digite o código do ator"))
    a = ator.buscar_ator(cod_ator)
    if (a == None):
        print("Ator não encontrado!")
    else:
        _imprimir_ator(a)

def menu_listar_atores():
    print("\nListar Atores:\n")
    atores = ator.buscar_atores()
    for a in atores:
        _imprimir_ator(a)

def menu_remover_ator():
    print("\nRemover Ator:\n")
    cod_ator = (input("Digite o código do ator:"))
    a = ator.remover_ator(cod_ator)
    if (a == False):
        print("Ator não encontrado!")
    else:
        print("Ator Removido")

def menu_remover_atores():
    ator.remover_todos_atores()
    print("Todos os atores foram removidos do banco de dados!")

def menu():
    while(True):
        print("1 - Adicionar novo ator")
        print("2 - Listar atores")
        print("3 - Buscar ator por código")
        print("4 - Remover ator")
        print("5 - Remover todos os atores")
        print("6 - Voltar")

        op = int(input("Digite sua escolha: "))
        while op < 1 or op > 6:
            op = int(input("Entre com uma escolha válida: "))
        if (op == 1):
            menu_adicionar_ator()
        elif(op == 2):
            menu_listar_atores()
        elif(op == 3):
            menu_buscar_ator()
        elif (op == 4):
            menu_remover_ator()
        elif (op == 5):
            menu_remover_atores()
        elif (op == 6):
            break
