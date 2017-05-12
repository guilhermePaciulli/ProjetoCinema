from logica import sala

def menu_adicionar_sala():
    print("\nAdicionar sala:")
    cod_sala = int(input("Digite o código da sala:"))
    lotacao = int(input("Digite a lotação da sala:"))
    sala.salas.append(cod_sala,lotacao)

def _imprimir_sala(sala):
    print("Código da sala:", sala[0])
    print("Lotação da sala:",sala[1])
    if sala[2] == True:
        print("Sala completamente ocupada!")
    else:
        print("Sala vazia ou com lugares ainda disponíveis!")

def menu_buscar_sala():
    print("\nBuscar sala por código/:\n")
    cod_sala = int(input("Digite o código da sala:"))
    sala = sala.buscar_sala(cod_sala)
    if (cod_sala == None):
        print("Sala não encontrada!")
    else:
        _imprimir_sala(cod_sala)

def menu_listar_salas():
    print("\nListar salas:\n")
    salas = sala.listar_salas()
    for s in salas:
        _imprimir_sala(s)

def menu_remover_sala():
    print("\nRemover sala:\n")
    cod_sala = int(input("Digite o código da sala:"))
    s = sala.remover_sala(cod_sala)
    if (s == False):
        print("
    
