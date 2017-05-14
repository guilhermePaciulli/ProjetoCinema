from gui import menu_sessao
from gui import menu_ator
from gui import menu_filme
from gui import menu_sala
from gui import menu_elenco
from gui import menu_ingresso

from logica import sessao
from logica import ator
from logica import filme
from logica import sala
from logica import elenco
from logica import ingresso

def limparTela():
    for i in range(0, 30):
        print("")
#Initial SetUp
sala.iniciar_salas()
ator.iniciar_atores()
filme.iniciar_filmes()
elenco.iniciar_elencos()
sessao.iniciar_sessoes()
ingresso.iniciar_ingressos()

while True:
    print("Bem vindo ao CineMania")
    print("1 - Ingressos")
    print("2 - Sessão")
    print("3 - Filme")
    print("4 - Elenco")
    print("5 - Sala")
    print("6 - Ator")
    print("7 - Sair")
    option = int(input("Para onde você quer ir? "))
    while(option < 1 or option > 6):
        option = int(input("Insira um valor válido "))
    if option == 1:
        menu_ingresso.menu()
        limparTela()
    else if option == 2:
        menu_sessao.menu()
        limparTela()
    else if option == 3:
        menu_filme.menu()
        limparTela()
    else if option == 4:
        menu_elenco.menu()
        limparTela()
    else if option == 5:
        menu_sala.menu()
        limparTela()
    else if option == 6:
        menu_ator.menu()
    else:
        limparTela()
        break