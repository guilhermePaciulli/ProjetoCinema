import sessao

ingresso =[]

def venda_ingreso_meia(cod_sessao):
    pass

def venda_ingresso_inteira(cod_sessao):
    pass

def listar_ingresso_vendidos(cod_sessao):
    pass

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
