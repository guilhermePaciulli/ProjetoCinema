import sessao

ingresso =[]
def _venda_ingresso(cod_sessao):
    s = sessao.verificar_lotacao(cod_sessao)
    if s != None:
        if !s :
            ingresso.append(cod_sessao)
            s[4] -= 1
        else:
            print("Sessão ocupada")
    else:
        print("Código de sessão inválido")

def venda_ingreso_meia(cod_sessao):
    _venda_ingresso(cod_sessao)

def venda_ingresso_inteira(cod_sessao):
    _venda_ingresso(cod_sessao)

def listar_ingresso_vendidos(cod_sessao):
    ingressosVendidos = []
    for i in ingresso:
        ingressosVendidos.append(i)
    return ingressosVendidos

def listar_ingressos():
    return ingresso

def buscar_ingresso(cod_ingresso):
    for c in ingresso:
        if (c[0] == cod_ingresso):
            return c
    return None

def remover_ingresso(cod_ingresso):
    for c in ingresso:
        if (c[0] == cod_ingresso):
            ingresso.remove(c)
            return True
        return False

def remover_todos_ingresso(cod_ingresso):
    global ingresso
    ingresso = []

def iniciar_ingressos():
    pass
