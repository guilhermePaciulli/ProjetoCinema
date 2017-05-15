# -*- coding: utf-8 -*-

import unittest
from logica import sessao
from logica import sala
from logica import filme

sala.iniciar_salas()
filme.iniciar_filmes()

class SessaoTeste(unittest.TestCase):

    def setUp(self):
        sessao.remover_todas_sessoes()

    def test_criar_sessao(self):
        sessao.criar_sessao("0", "0", "0", "16:00")
        sessao.criar_sessao("1", "1", "1", "17:00")
        self.assertEquals(2, len(sessao.listar_sessoes()))

    def test_remover_todas_sessoes(self):
        sessao.criar_sessao("0", "0", "0", "16:00")
        sessao.criar_sessao("1", "1", "1", "17:00")
        sessao.criar_sessao("0", "0", "0", "16:00")
        sessao.criar_sessao("1", "1", "1", "17:00")
        sessao.remover_todas_sessoes()
        self.assertEquals(0, len(sessao.listar_sessoes()))

    def test_iniciar_sessoes(self):
        sessao.iniciar_sessoes()
        self.assertEquals(2, len(sessao.listar_sessoes()))

    def test_listar_sessoes(self):
        sessao.criar_sessao("0", "0", "0", "16:00")
        sessao.criar_sessao("1", "1", "1", "17:00")
        sessao.criar_sessao("0", "0", "0", "16:00")
        sessao.criar_sessao("1", "1", "1", "17:00")
        s = sessao.listar_sessoes()
        self.assertEquals(4, len(sessao.listar_sessoes()))

    def test_recuperar_sessao(self):
        sessao.criar_sessao("0", "0", "0", "16:00")
        s = sessao.recuperar_sessao("0")
        self.assertIsNotNone(s)

    def test_remover_sessao(self):
        sessao.criar_sessao("1", "1", "1", "17:00")
        sessao.remover_sessao("1")
        self.assertEquals(0, len(sessao.listar_sessoes()))

    def test_verficar_lotacao(self):
        sessao.criar_sessao("0", "0", "0", "16:00")
        s = sessao.recuperar_sessao("0")
        self.assertFalse(sessao.verificar_lotacao("0"))


if __name__ == '__main__':
    unittest.main()
