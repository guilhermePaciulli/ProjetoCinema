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
    pass
def verificar_lotacao(cod_sessao):
    pass
def listar_sessoes():
    return sessoes
def remover_sessao(cod_sessao):
    pass
def remover_todos_ingressos():
    pass
def iniciar_ingressos():
    pass
