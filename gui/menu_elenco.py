# -*- coding: utf-8 -*-

from logica import elenco

def menu_adicionar_elenco():
    print("\nAdicionar ator ao elenco:\n")
    cod_elenco = input("Digite o código do elenco:")
    cod_ator = input("Digite o código do ator:")
    tipo = input("Digite o tipo do papel do ator:")
    cod_filme = input("Digite o código do filme:")
    b = elenco.adicionar_ator(cod_elenco,cod_ator,cod_filme,tipo)
    if not(b):
        print("Código do filme ou do ator inválido(s)")

def _imprimir_elenco(e):
    print("Código do elenco:",e[0])
    print("Código do filme:",e[2][0])
    print("Título do filme:",e[2][1])
    print("Duração do filme:",e[2][2])
    print("Classificação do filme:",e[2][3])
    print("Diretor do filme:",e[2][4])
    print("Distribuidor do filme:",e[2][5])
    print("Status do filme:",e[2][6])
    print("Gênero do filme:",e[2][7])
    for a in e[1]:
        print("Código do ator:",a[0][0])
        print("Nome do ator:",a[0][1])
        print("Nacionalidade do ator:",a[0][2])
        print("Idade do ator:",a[0][3])
        print("Tipo do ator:",a[1])
        print()
    print()

def menu_buscar_elenco():
    print("\nBuscar elenco por código:\n")
    cod_elenco = (input("Digite o código do elenco"))
    e = elenco.buscar_elenco(cod_elenco)
    if (e == None):
        print("Elenco não encontrado!")
    else:
        _imprimir_elenco(e)

def menu_buscar_elenco_por_filme():
    print("\nBuscar elenco por filme:\n")
    cod_filme = (input("Digite o código do filme:"))
    e = elenco.buscar_elenco_por_filme(cod_filme)
    if (e == None):
        print("Elenco não encontrado!")
    else:
        _imprimir_elenco(e)

def menu_remover_elenco():
    print("\nRemover Elenco:\n")
    cod_elenco = (input("Digite o código do elenco:"))
    e = elenco.remover_elenco(cod_elenco)
    if (e == False):
        print("Elenco não encontrado!")
    else:
        print("Elenco Removido")

def menu_remover_todos_elencos():
    elenco.remover_todos_elencos()
    print("Todos os elencos foram removidos do banco de dados!")

def menu():
    while(True):
        print("1 - Adicionar ator ao elenco ou adicionar novo elenco")
        print("2 - Buscar elenco por código")
        print("3 - Buscar elenco por filme")
        print("4 - Remover elenco")
        print("5 - Remover todos os elencos")
        print("6 - Voltar")

        op = int(input("Digite sua escolha: "))
        while op < 1 or op > 6:
            op = int(input("Entre com uma escolha válida: "))

        if(op == 1):
            menu_adicionar_elenco()
        elif(op == 2):
            menu_buscar_elenco()
        elif(op == 3):
            menu_buscar_elenco_por_filme()
        elif(op == 4):
            menu_remover_elenco()
        elif(op == 5):
            menu_remover_todos_elencos()
        elif(op == 6):
            break
