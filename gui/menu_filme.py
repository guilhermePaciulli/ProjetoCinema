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

def _imprimir_filme(filme):
    print("Código do filme:",filme[0])
    print("Título do filme:",filme[1])
    print("Duração do filme:",filme[2])
    print("Classificação do filme:",filme[3])
    print("Diretor do filme:",filme[4])
    print("Distribuidor do filme:",filme[5])
    print("Status do filme:",filme[6])
    print("Gênero do filme:",filme[7])
    print("")
    
def menu_buscar_filme():
    print("\nBuscar filme por código:\n")
    cod_filme = int(input("Digite o código do filme:"))
    filme = filme.buscar_filme(cod_filme)
    if (cod_filme == None):
        print("Filme não encontrado!")
    else:
        _imprimir_filme(filme)

def menu_listar_filmes():
    print("\nListar filmes:\n")
    filmes = filme.listar_filmes()
    for f in filmes:
        _imprimir_filme(f)

def menu_remover_filme():
    print("\nRemover Filme:\n")
    cod_filme = int(input("Digite o código do filme:"))
    f = filme.remover_filme(cod_filme)
    if (f == False):
        print("Filme não encontrado!")
    else:
        print("Filme Removido!")

def menu_remover_todos_filmes():
    filme.remover_todos_filmes()
    print("Todos os filmes foram removidos do banco de dados!")

def menu():
    while(True):
        print("1 - Adicionar novo filme")
        print("2 - Listar filmes")
        print("3 - Buscar filme por código")
        print("4 - Remover filme")
        print("5 - Remover todos os filmes")
        print("0 - Voltar")

        op = int(input("Digite sua escolha: "))

        if(op == 1):
            menu_adicionar_filme()
        elif(op == 2):
            menu_listar_filmes()
        elif(op == 3):
            menu_buscar_filme()
        elif(op == 4):
            menu_remover_filme()
        elif(op == 5):
            menu_remover_todos_filmes()                           
        elif(op == 0):
            break

