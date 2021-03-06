# -*- coding: utf-8 -*-

from logica import sessao

def menu_adicionar_sessao():
    print("\nAdicionar sessão:\n")
    cod_sessao = (input("Digite o código da sessão:"))
    cod_filme = (input("Digite o código do filme:"))
    cod_sala = (input("Digite o código da sala:"))
    horario = input("Digite o horário da sessão:")
    b = sessao.criar_sessao(cod_sessao,cod_filme,cod_sala,horario)
    if b:
        print("Sessão adicionada com sucesso")
    else:
        print("Código do filme ou da sala inválido(s) ou sala lotada!")

def _imprimir_sessao(s):
    print("Código da sessão:",s[0])
    print("Código do filme:",s[1][0])
    print("Código da sala:",s[2][0])
    print("Horário da sessão:",s[3])
    print("")

def menu_buscar_sessao():
    print("\nBuscar sessão por código:\n")
    cod_sessao = (input("Digite o código da sessão:"))
    se = sessao.recuperar_sessao(cod_sessao)
    if (se == None):
        print("Sessão não encontrada!")
    else:
        _imprimir_sessao(se)

def menu_listar_sessoes():
    print("\nListar sessões:\n")
    se = sessao.listar_sessoes()
    for s in se:
        _imprimir_sessao(s)

def menu_remover_sessao():
    print("\nRemover Sessão:\n")
    cod_sessao = (input("Digite o código do sessão:"))
    s = sessao.remover_sessao(cod_sessao)
    if (s == False):
        print("Sessão não encontrada!")
    else:
        print("Sessão Removida!")

def menu_remover_todas_sessoes():
    sessao.remover_todas_sessoes()
    print("Todos as sessões foram removidas do banco de dados!")

def menu():
    while(True):
        print("1 - Adicionar nova sessão")
        print("2 - Listar sessões")
        print("3 - Buscar sessão por código")
        print("4 - Remover sessão")
        print("5 - Remover todas as sessões")
        print("6 - Voltar")

        op = int(input("Digite sua escolha: "))
        while op < 1 or op > 6:
            op = int(input("Entre com uma escolha válida: "))
        if(op == 1):
            menu_adicionar_sessao()
        elif(op == 2):
            menu_listar_sessoes()
        elif(op == 3):
            menu_buscar_sessao()
        elif(op == 4):
            menu_remover_sessao()
        elif(op == 5):
            menu_remover_todas_sessoes()
        elif(op == 6):
            break
