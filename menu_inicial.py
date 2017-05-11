import menu_sessao
import menu_ator
import menu_filme
import menu_sala
import menu_elenco
import menu_ingresso

def limparTela():
    for i in range(0, 30):
        print("")

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
