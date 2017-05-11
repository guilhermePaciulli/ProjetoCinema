salas = []

def adicionar_sala(cod_sala, lotacao):
    salas.append([cod_sala, lotacao, False])

def definir_status_ocupada(cod_sala):
    indice_sala = salas.index(buscar_sala(cod_sala))
    salas[indice_sala][2] = True

def definir_status_livre(cod_sala):
    indice_sala = salas.index(buscar_sala(cod_sala))
    salas[indice_sala][2] = False

def buscar_sala(cod_sala):
    for s in salas:
        if s[0] == cod_sala:
            return s
    return None

def listar_salas():
    return salas

def remover_sala(cod_sala):
    salas.remove(buscar_sala(cod_sala))

def remover_todas_salas():
    global salas
    salas = []

def iniciar_salas():
    adicionar_sala(0, 40)
    adicionar_sala(1, 60)
