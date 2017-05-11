from logica import ator

def menu_adicionar():
    print("\nAdicionar ator:\n")
    cod_ator = int(input("Digite o código do ator:"))
    nome = input("Digite o nome do ator:"))
    nacionalidade = input("Digite a nacionalidade:")
    idade = int(input("Digite a idade:"))
    ator.cadastrar_ator(cod_ator,nome,nacionalidade,idade)

def _imprimir_ator(ator):
    print("Código do ator:",ator[0])
    print("Nome do ator:",ator[1])
    print("Nacionalidade do ator:",ator[2])
    print("Idade do ator:",ator[3])
    print()

def buscar_ator():
    cod_ator = input("")
    ator = ator.buscar_ator(cod_ator)
    _imprimir_ator(ator)

    
