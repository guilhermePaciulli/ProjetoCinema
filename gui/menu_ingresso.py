from logica import sessao
from logica import filme
from logica import ingresso

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


