import sessao

ingresso =[]
def _venda_ingresso(cod_sessao):
    s = sessao.verificar_lotacao(cod_sessao)
    if s != None:
        if not(s) :
            cod_ingresso = len(ingresso)
            ingresso.append([cod_sessao, cod_ingresso])
            s[4] -= 1
            return [True, str(cod_ingresso)]
        else:
            return [False, -1]
    else:
        return [False, -1]

def venda_ingresso_meia(cod_sessao):
    _venda_ingresso(cod_sessao)

def venda_ingresso_inteira(cod_sessao):
    _venda_ingresso(cod_sessao)

def listar_ingresso_vendidos(cod_sessao):
    ingressosVendidos = []
    for i in ingresso:
        if i == cod_sessao:
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

def remover_todos_ingresso(cod_ingresso):
    for i in ingresso:
        sessao.recuperar_sessao(i[0])[4] += 1
    global ingresso
    ingresso = []

def iniciar_ingressos():
    venda_ingresso_meia(0)
    venda_ingresso_inteira(0)
