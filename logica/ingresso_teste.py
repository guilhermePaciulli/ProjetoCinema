import ingresso
import sala
import sessao
import unittest

sala.adicionar_sala(0, 2)
sessao.criar_sessao(0, 0, 0, "14:30")

class IngressoTeste(unittest.TestCase):

    def tearDown(self):
        ingresso.remover_todos_ingresso()

    def test_vender_ingresso(self):
        s = ingresso.venda_ingresso_meia(1)
        self.assertEqual(-1, s[1])
        s = ingresso.venda_ingresso_inteira(0)
        self.assertEqual(True, s[0])
        self.assertEqual(1, s[1])
        s = ingresso.venda_ingresso_inteira(0)
        s = ingresso.venda_ingresso_inteira(0)
        self.assertEqual(-1, s[1])
        self.assertEqual(2, len(ingresso.listar_ingressos()))

    def test_remover_ingresso(self):
        s = ingresso.venda_ingresso_inteira(0)
        self.assertEqual(1, len(ingresso.listar_ingressos()))
        self.assertEqual(2, sessao.recuperar_sessao(0)[4])

    def test_buscar_ingresso(self):
        s = ingresso.venda_ingresso_meia(0)
        self.assertIsNotNone(ingresso.buscar_ingresso(int(s[1])))
