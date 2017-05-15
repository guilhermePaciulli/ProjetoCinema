# -*- coding: utf-8 -*-

from logica import sessao

ingresso =[]
def _venda_ingresso(cod_sessao):
    s = sessao.recuperar_sessao(cod_sessao)
    if s != None:
        lot = sessao.verificar_lotacao(cod_sessao)
        if not(lot) :
            cod_ingresso = str(len(ingresso))
            ingresso.append([cod_sessao, cod_ingresso])
            s[4] -= 1
            return cod_ingresso
        else:
            return False
    else:
        return None

def venda_ingresso_meia(cod_sessao):
    return _venda_ingresso(cod_sessao)

def venda_ingresso_inteira(cod_sessao):
    return _venda_ingresso(cod_sessao)

def listar_ingressos_vendidos(cod_sessao):
    ingressosVendidos = []
    for i in ingresso:
        if i[0] == cod_sessao:
            ingressosVendidos.append(i)
    return ingressosVendidos

def listar_ingressos():
    return ingresso

def buscar_ingresso(cod_ingresso):
    for i in ingresso:
        if (i[1] == cod_ingresso):
            return i
    return None

def remover_ingresso(cod_ingresso):
    for i in ingresso:
        if (i[1] == cod_ingresso):
            sessao.recuperar_sessao(i[0])[4] += 1
            ingresso.remove(i)
            return True
    return False

def remover_todos_ingresso():
    global ingresso
    ingresso = []
    for s in sessao.sessoes:
        s[4] = s[2][1]

def iniciar_ingressos():
    venda_ingresso_meia("0")
    venda_ingresso_inteira("0")
