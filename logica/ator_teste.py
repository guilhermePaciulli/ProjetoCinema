# -*- coding: utf-8 -*-

import unittest
import ator

class AtorTeste(unittest.TestCase):

    def setUp(self):
        ator.remover_todos_atores()

    def test_cadastrar_ator(self):
        ator.cadastrar_ator(0, 0, 0, "Principal")
        ator.cadastrar_ator(1, 1, 1, "Coadjuvante")
        self.assertEquals(2, len(ator.buscar_atores()))

    def test_buscar_ator(self):
        ator.cadastrar_ator(0, 0, 0, "Principal")
        self.assertTrue(ator.buscar_ator(0) != None)

    def test_remover_ator(self):
        ator.cadastrar_ator(0, 0, 0, "Principal")
        ator.remover_ator(0)
        self.assertEquals(0, len(ator.buscar_atores()))

    def test_buscar_atores(self):
        ator.cadastrar_ator(0, 0, 0, "Principal")
        ator.cadastrar_ator(1, 0, 0, "Coadjuvante")
        ator.cadastrar_ator(2, 0, 0, "Figurante")
        ator.cadastrar_ator(3, 0, 0, "Coadjuvante")
        ator.cadastrar_ator(4, 0, 0, "Principal")
        self.assertEquals(5, len(ator.buscar_atores()))

    def test_remover_todos_atores(self):
        ator.cadastrar_ator(0, 0, 0, "Principal")
        ator.cadastrar_ator(1, 0, 0, "Coadjuvante")
        ator.cadastrar_ator(2, 0, 0, "Figurante")
        ator.cadastrar_ator(3, 0, 0, "Coadjuvante")
        ator.remover_todos_atores()
        self.assertEquals(0, len(ator.buscar_atores()))

    def test_iniciar_atores(self):
        ator.iniciar_atores()
        self.assertEquals(2, len(ator.buscar_atores()))

if __name__ == '__main__':
    unittest.main()
