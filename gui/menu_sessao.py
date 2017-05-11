from logica import sessao
from logica import filme

def menu_sessao(sessao):
    print("\nCriar sessão:\n")
    cod_sessao = int(input("Digite o código da sessão:"))
    cod_filme = int(input("Digite o código do filme:"))
    cod_sala = int(input("Digite o código da sala:"))
    horario = input("Digite o horário da sessão:"))

    agendou = sessao.criar_sessao(cod_sessao,cod_filme,cod_sala,horario)

    print("Sessão criada!")

def imprimir_sessao(sessao):
    
    
