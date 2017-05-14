from logica import sessao
from logica import filme

def menu_adicionar_sessao():
    print("\nAdicionar sessão:\n")
    cod_sessao = int(input("Digite o código da sessão:"))
    cod_filme = int(input("Digite o código do filme:"))
    cod_sala = int(input("Digite o código da sala:"))
    horario = input("Digite o horário da sessão:"))
    sessao.criar_sessao(cod_sessao,cod_filme,cod_sala,horario)

def _imprimir_sessao(sessao):
    print("Código da sessão:",sessao[0])
    print("Código do filme:",sessao[1])
    print("Código da sala:",sessao[2])
    print("Horário da sessão:",sessao[3])
    print("")
    
def menu_buscar_sessao():
    print("\nBuscar sessao por código:\n")
    cod_sessao = int(input("Digite o código da sessão:"))
    sessao = sessao.recuperar_sessao(cod_sessao)
    if (cod_sessao == None):
        print("Sessão não encontrada!")
    else:
        _imprimir_sessao(sessao)

def menu_listar_sessoes():
    print("\nListar sessões:\n")
    sessoes = sessao.listar_sessoes()
    for s in sessoes:
        _imprimir_sessao(s)

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

