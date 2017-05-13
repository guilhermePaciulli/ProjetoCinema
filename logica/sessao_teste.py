import unittest
import sessao

class SessaoTeste(unittest.TestCase):

    def setUp(self):
        sessao.remover_todas_sessoes()

    def test_criar_sessao(self):
        sessao.criar_sessao(0,0,0,"16:00")
        sessao.criar_sessao(1,1,1,"15:00")
        self.assertEquals(2, len(sessao.buscar_sessao()))

    def test_remover_todos_ingressos(self):
        sessao.criar_sessao(0,0,0,"16:00")
        sessao.criar_sessao(1,1,1,"15:00")
        sessao.criar_sessao(0,0,0,"16:00")
        sessao.criar_sessao(1,1,1,"15:00")
        sessao.remover_todos_ingressos()
        self.assertEquals(0, len(sessao.buscar_sessao()))

    def iniciar_ingressos(self):
        sessao.criar_sessao(1,1,1,"17:30")
        sessao.criar_sessao(1,1,1,"17:30")
        sessao.iniciar_ingressos()
        self.assertEquals(2, len(sessao.buscar_sessao()))
        
    def listar_sessoes(self):
        sessao.criar_sessao(0,0,0,"16:00")
        sessao.criar_sessao(1,1,1,"15:00")
        sessao.criar_sessao(0,0,0,"16:00")
        sessao.criar_sessao(1,1,1,"15:00")
        s = sessao.listar_sessoes()
        self.assertEquals(4, len(sessao.buscar_sessao()))

    def recuperar_sessao(self):
        sessao.criar_sessao(0,0,0,"16:00")
        s = self.assertNotNone(s)

    def remover_sessao(self):
        sessao.criar_sessao(1,1,1,"17:30")
        sessao.criar_sessao(1,1,1,"17:30")
        sessao.criar_sessao(1,1,1,"17:30")
        self.assertEquals(0, len(sessao.buscar_sessao()))

if __name__ == '__main__':
    unittest.main()
