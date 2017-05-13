from logica import elenco

def menu_adicionar_elenco():
    print("\nAdicionar elenco:\n")
    cod_elenco = int(input("Digite o código do elenco:"))
    tipo = input("Digite o tipo do papel do ator:"))
    elenco.adicionar_ator(cod_elenco,cod_ator,cod_filme,tipo)

def _imprimir_elenco(elenco):
    print("Código do elenco:",elenco[0])
    atores = elenco.consultar_atores_por_filme(elenco[0])
    for a in atores:
        print("Ator do elenco:",a[1])
        print("Nacionalidade do ator:",ator[2])
    print(":",ator[3])
    print()

def menu_buscar_elenco():
    print("\nBuscar elenco por código:\n")
    cod_elenco = int(input("Digite o código do elenco"))
    elenco = elenco.buscar_elenco(cod_elenco)
    if (cod_elenco == None):
        print("Elenco não encontrado!")
    else:
        _imprimir_elenco(elenco)

def menu_buscar_elenco_por_filme():
    print("\nBuscar elenco por filme:\n")
    cod_filme = int(input("Digite o código do filme:"))
    elenco = elenco.buscar_elenco_por_filme(cod_filme)
    if (cod_filme == None):
        print("Elenco não encontrado!")
    else:
        _imprimir_elenco(elenco)

def menu_listar_elencos():
    print("\nListar elencos:\n")
    elenco = elenco.buscar_elenco()
    for e in elencos:
        _imprimir_elenco(e)

def menu_remover_ator():
    print("\nRemover Ator:\n")
    cod_ator = int(input("Digite o código do ator:"))
    a = ator.remover_ator(cod_ator)
    if (a == False):
        print("Ator não encontrado!")
    else:
        print("Ator Removido")

def menu_remover_atores():
    ator.remover_atores()
    print("Todos os atores foram removidos do banco de dados!")

def menu():
    while(True):
        print("1 - Adicionar novo ator")
        print("2 - Listar atores")
        print("3 - Buscar ator por código")
        print("4 - Remover ator")
        print("5 - Remover todos os atores")
        print("0 - Voltar")

        op = int(input("Digite sua escolha: "))

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
        elif (op == 0):
            break
