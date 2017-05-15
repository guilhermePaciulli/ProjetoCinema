# -*- coding: utf-8 -*-

import unittest
from logica import sala

class SalaTeste(unittest.TestCase):

    def setUp(self):
        sala.remover_todas_salas()

    def test_adicionar_sala(self):
        sala.adicionar_sala(0, 60)
        self.assertEqual(1, len(sala.listar_salas()))

    def test_definir_status_ocupada(self):
        sala.adicionar_sala(0, 60)
        sala.definir_status_ocupada(0)
        self.assertTrue(sala.salas[0][2])

    def test_definir_status_livre(self):
        sala.adicionar_sala(0, 60)
        sala.definir_status_livre(0)
        self.assertFalse(sala.salas[0][2])

    def test_remover_sala(self):
        sala.adicionar_sala(0, 60)
        sala.remover_sala(0)
        self.assertEqual(0, len(sala.listar_salas()))

    def test_remover_todas_salas(self):
        sala.adicionar_sala(0, 60)
        sala.adicionar_sala(1, 60)
        sala.adicionar_sala(2, 60)
        sala.remover_todas_salas()
        self.assertEqual(0, len(sala.listar_salas()))

    def test_listar_salas(self):
        sala.adicionar_sala(0, 60)
        sala.adicionar_sala(1, 60)
        sala.adicionar_sala(2, 60)
        salas = sala.listar_salas()
        self.assertEqual(3, len(sala.listar_salas()))

    def test_buscar_lista(self):
        sala.adicionar_sala(0, 60)
        s = sala.buscar_sala(0)
        self.assertNotEqual(None, s)

    def test_iniciar_sala(self):
        sala.iniciar_salas()
        self.assertEqual(2, len(sala.listar_salas()))

if __name__ == '__main__':
    unittest.main()
