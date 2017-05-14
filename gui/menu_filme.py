from logica import filme

def menu_adicionar_filme():
    print("\nAdicionar filme:\n")
    cod_filme = int(input("Digite o código do filme:"))
    titulo = input("Digite o título do filme:")
    duracao = float(input("Digite a duração do filme:"))
    classificacao = input("Digite a classificação do filme:"))
    diretor = input("Digite o diretor do filme:"))
    dist = input("Digite a distribuidora do filme:"))
    status = input("Digite o status do filme:"))
    genero = input("Digite o genero do filme:"))
    filme.cadastrar_filme(cod_filme, titulo, duracao, classificao, diretor, distribuidora, status, genero)

def _imprimir_elenco(elenco):
    print("Código do elenco:",elenco[0])
    atores = elenco.consultar_atores_por_filme(elenco[0])
    for a in atores:
        print("Ator do elenco:",a[1])
        print("Nacionalidade do ator:",ator[2])
        print("Tipo do ator:",ator[3])
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

def menu_remover_elenco():
    print("\nRemover Elenco:\n")
    cod_elenco = int(input("Digite o código do elenco:"))
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
        print("1 - Adicionar novo elenco")
        print("2 - Listar elencos")
        print("3 - Buscar elenco por código")
        print("4 - Buscar elenco por filme")
        print("5 - Remover elenco")
        print("6 - Remover todos os elencos")
        print("0 - Voltar")

        op = int(input("Digite sua escolha: "))

        if(op == 1):
            menu_adicionar_elenco()
        elif(op == 2):
            menu_listar_elencos()
        elif(op == 3):
            menu_buscar_elenco()
        elif(op == 4):
            menu_buscar_elenco_por_filme()
        elif(op == 5):
            menu_remover_elenco()
        elif(op == 6):
            menu_remover_todos_elencos()                            
        elif(op == 0):
            break

