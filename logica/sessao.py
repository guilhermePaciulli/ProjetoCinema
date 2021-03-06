# -*- coding: utf-8 -*-

from logica import filme
from logica import sala

sessoes = []

def criar_sessao(cod_sessao,cod_filme,cod_sala,horario):
    f = filme.buscar_filme(cod_filme)
    s = sala.buscar_sala(cod_sala)
    if s != None and f != None and not(s[2]):
        sessoes.append([cod_sessao,f,s,horario, s[1]])
        return True
    return False

def recuperar_sessao(cod_sessao):
    for c in sessoes:
        if (c[0] == cod_sessao):
            return c
    return None

def verificar_lotacao(cod_sessao):
    for s in sessoes:
        if s[0] == cod_sessao:
            return s[4] <= 0
    return None

def listar_sessoes():
    return sessoes

def remover_sessao(cod_sessao):
    for c in sessoes:
        if (c[0] == cod_sessao):
            sessoes.remove(c)
            return True
    return False

def remover_todas_sessoes():
    global sessoes
    sessoes = []

def iniciar_sessoes():
    criar_sessao("0", "0", "0", "19:30")
    criar_sessao("1", "1", "1", "17:30")
