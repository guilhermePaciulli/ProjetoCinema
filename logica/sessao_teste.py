import unittest
import sessao

class SessaoTest(unittest.TestCase):

    def setUp(self):
        sessao.remover_todas_sessoes()

    def test_criar_sessao(self):
        sessao.criar_sessao(0,0,0,"16:00")
        sessao.criar_sessao(1,1,1,"15:00")
        self.assertEquals(2, len(sessao.buscar_sessao()))

    def test_remover_todos_ingressos(self):
        pass
