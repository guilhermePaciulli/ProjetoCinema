import filme
import sala

sessoes = []

def criar_sessao(cod_sessao,cod_filme,cod_sala,horario):
    f = filme.buscar_filme(cod_filme)
    s = sala.buscar_sala(cod_sala)
    sessoes.append([cod_sessao,f,s,horario, s[1]])

def recuperar_sessao(cod_sessao):
    for c in sessoes:
        if (c[0] == cod_sessao):
            return c
    return None

def verificar_lotacao(cod_sessao):
    for s in sessoes:
        if s[0] == cod_sessao:
            return s[4] < 0
    return None

def listar_sessoes():
    return sessoes

def remover_sessao(cod_sessao):
    for c in sessoes:
        if (c[0] == cod_sessao):
            sessoes.remove(c)
            return True
    return False

def remover_todos_ingressos():
    global sessoes
    sessoes = []

def iniciar_ingressos():
    criar_sessao(1,1,1,"17:30")
