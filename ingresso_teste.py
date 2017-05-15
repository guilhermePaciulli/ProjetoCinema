# -*- coding: utf-8 -*-

from logica import ingresso
from logica import sala
from logica import sessao
from logica import filme
import unittest

class IngressoTeste(unittest.TestCase):

    def setUp(self):
        ingresso.remover_todos_ingresso()
        sala.remover_todas_salas()
        sessao.remover_todas_sessoes()
        sala.adicionar_sala(0, 2)
        filme.iniciar_filmes()
        sessao.criar_sessao(0, 0, 0, "14:30")

    def test_vender_ingresso(self):
        s = ingresso.venda_ingresso_meia(1)
        self.assertIsNone(s)
        s = ingresso.venda_ingresso_meia(0)
        self.assertEqual("0", s)
        s = ingresso.venda_ingresso_inteira(0)
        self.assertEqual("1", s)
        s = ingresso.venda_ingresso_inteira(0)
        self.assertEqual(False, s)

    def test_remover_ingresso(self):
        s = ingresso.venda_ingresso_inteira(0)
        ingresso.remover_ingresso((s))
        self.assertEqual(0, len(ingresso.listar_ingressos()))
        self.assertEqual(2, sessao.recuperar_sessao(0)[4])

    def test_buscar_ingresso(self):
        s = ingresso.venda_ingresso_meia(0)
        self.assertIsNotNone(ingresso.buscar_ingresso((s)))

    def test_remover_todos_ingressos(self):
        s = ingresso.venda_ingresso_inteira(0)
        s = ingresso.venda_ingresso_inteira(0)
        ingresso.remover_todos_ingresso()
        self.assertEqual(0, len(ingresso.listar_ingressos()))

    def test_listar_ingressos(self):
        s = ingresso.venda_ingresso_inteira(0)
        s = ingresso.venda_ingresso_inteira(0)
        self.assertEqual(2, len(ingresso.listar_ingressos()))

    def listar_ingresso_vendidos(self):
        s = ingresso.venda_ingresso_inteira(0)
        v = ingresso.listar_ingresso_vendidos(0)
        self.assertEqual(1, len(v))
if __name__ == '__main__':
    unittest.main()
