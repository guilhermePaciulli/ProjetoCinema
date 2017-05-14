filmes = []

def cadastrar_filme(cod_filme, titulo, duracao, classificao, diretor, distribuidora, status, genero):
    filmes.append(cod_filme, titulo, duracao, classificao, diretor, distribuidora, status, genero)

def buscar_filme(cod_filme):
    for f in filmes:
        if f[0] == cod_filme:
            return f
    return None

def listar_filmes():
    return filmes

def remover_filme():
    filmes.remove(buscar_filme(cod_filme))

def remover_todos_filmes():
    global filmes
    filmes = []

def iniciar_filmes():
    cadastrar_filme(0, "A volta daqueles não foram", 1.2, "Livre", "Steven Spielberg", "Universal", "Em cartaz", "Aventura")
    cadastrar_filme(1, "A volta daqueles não foram 2: O retorno", 3.4, "Livre", "George Lucas", "Walt Disney", "Em breve", "Ação")
