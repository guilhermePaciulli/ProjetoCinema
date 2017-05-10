import filme
import sala

sessoes = []
cod_sessao = 0

def gerar_codigo():
    cod_sessao+=1
    return cod_sessao

def criar_sessao(cod_sessao,cod_filme,cod_sala,horario):
    ss = gerar_codigo()
    f = filme.buscar_filme(cod_filme)
    s = sala.buscar_sala(cod_sala)

    sessao = [ss,f,s,horario]
    sessoes.append(sessao)
    
def recuperar_sessao(cod_sessao):
    for c in sessoes:
        if (c[0] == cod_sessao):
            return c
    return None
def verificar_lotacao(cod_sessao):
    for c in range(len(sessoes)):
        return c[2]
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
    global cod_sessao

    sessoes = []
    cod_sessao = 0
def iniciar_ingressos():
    criar_sessao(1,1,1,"17:30")
