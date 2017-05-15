# -*- coding: utf-8 -*-

import ator
import filme

elencos = []

def adicionar_ator(cod_elenco, cod_ator, cod_filme, tipo):
    if(ator.buscar_ator(cod_ator) != None and filme.buscar_filme(cod_filme) != None):
        e = buscar_elenco(cod_elenco)
        a = ator.buscar_ator(cod_ator)
        if e != None:
            elencos[elencos.index(e)][1].append(a)
        else:
            a = ator.buscar_ator(cod_ator)
            f = filme.buscar_filme(cod_filme)
            elencos.append([cod_elenco, [[a, tipo]], f])
        return True
    return False

def consultar_atores_por_filme(cod_elenco):
    for e in elencos:
        if e[0] == cod_elenco:
            return e[1]

def buscar_elenco(cod_elenco):
    for e in elencos:
        if e[0] == cod_elenco:
            return e
    return None

def remover_elenco(cod_elenco):
    elencos.remove(buscar_elenco(cod_elenco))

def buscar_elenco_por_filme(cod_filme):
    for e in elencos:
        if e[2][0] == cod_filme:
            return e[1]

def remover_todos_elencos():
    global elencos
    elencos = []

def iniciar_elencos():
    adicionar_ator(0, 0, 0, "Principal")
    adicionar_ator(1, 1, 1, "Coadjuvante")
