atores = []

def cadastrar_ator(cod_ator, nome, nacionalidade, idade):
    atores.append([cod_ator, nome, nacionalidade, idade])

def buscar_ator(cod_ator):
    for a in atores:
        if a[0] == cod_ator:
            return a
    return None

def remover_ator(cod_ator):
    atores.remove(buscar_ator(cod_ator))

def buscar_atores():
    return atores

def remover_todos_atores():
    global atores
    atores = []

def iniciar_atores():
    cadastrar_ator(0, "Morgan Freeman", "EUA", 79)
    cadastrar_ator(1, "Tony Ramos", "BR", 68)
