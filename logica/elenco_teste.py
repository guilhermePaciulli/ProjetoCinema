# -*- coding: utf-8 -*-

import elenco
import filme
import ator
import unittest

filme.iniciar_filmes()
ator.iniciar_atores()

class TesteElenco(unittest.TestCase):

    def setUp(self):
        elenco.remover_todos_elencos()

    def test_adicionar_ator(self):
        elenco.adicionar_ator(0, 0, 0, "Coadjuvante")
        elenco.adicionar_ator(1, 1, 1, "Principal")
        self.assertEquals(2, len(elenco.elencos))

    def test_buscar_elenco(self):
        elenco.adicionar_ator(0, 0, 0, "Coadjuvante")
        self.assertIsNotNone(elenco.buscar_elenco(0))

    def test_remover_todos_elencos(self):
        elenco.adicionar_ator(0, 0, 0, "Coadjuvante")
        elenco.adicionar_ator(1, 1, 1, "Principal")
        elenco.remover_todos_elencos()
        self.assertEquals(0, len(elenco.elencos))

    def test_remover_elenco(self):
        elenco.adicionar_ator(0, 0, 0, "Coadjuvante")
        elenco.remover_elenco(0)
        self.assertEquals(0, len(elenco.elencos))

    def test_iniciar_elenco(self):
        elenco.iniciar_elencos()
        self.assertEquals(2, len(elenco.elencos))

if __name__ == '__main__':
    unittest.main()
