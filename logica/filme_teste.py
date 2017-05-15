# -*- coding: utf-8 -*-

import unittest
import filme

class FilmeTeste(unittest.TestCase):

    def setUp(self):
        filme.remover_todos_filmes()

    def test_cadastrar_filme(self):
        filme.cadastrar_filme(0, "Jurassic World", 3.2, 0, "Steven Spielberg", "Universal", "Em cartaz", "Aventura")
        filme.cadastrar_filme(0, "Jurassic World", 3.2, 0, "Steven Spielberg", "Universal", "Em cartaz", "Aventura")
        self.assertEquals(2, len(filme.listar_filmes()))

    def test_buscar_filme(self):
        filme.cadastrar_filme(0, "Jurassic World", 3.2, 0, "Steven Spielberg", "Universal", "Em cartaz", "Aventura")
        self.assertIsNotNone(filme.buscar_filme(0))

    def test_listar_filmes(self):
        filme.cadastrar_filme(0, "Jurassic World", 3.2, 0, "Steven Spielberg", "Universal", "Em cartaz", "Aventura")
        filme.cadastrar_filme(1, "Jurassic World", 3.2, 0, "Steven Spielberg", "Universal", "Em cartaz", "Aventura")
        filme.cadastrar_filme(2, "Jurassic World", 3.2, 0, "Steven Spielberg", "Universal", "Em cartaz", "Aventura")
        filme.cadastrar_filme(3, "Jurassic World", 3.2, 0, "Steven Spielberg", "Universal", "Em cartaz", "Aventura")
        filme.cadastrar_filme(4, "Jurassic World", 3.2, 0, "Steven Spielberg", "Universal", "Em cartaz", "Aventura")
        filme.cadastrar_filme(5, "Jurassic World", 3.2, 0, "Steven Spielberg", "Universal", "Em cartaz", "Aventura")
        self.assertEquals(6, len(filme.listar_filmes()))

    def test_remover_todos_filmes(self):
        filme.cadastrar_filme(0, "Jurassic World", 3.2, 0, "Steven Spielberg", "Universal", "Em cartaz", "Aventura")
        filme.cadastrar_filme(1, "Jurassic World", 3.2, 0, "Steven Spielberg", "Universal", "Em cartaz", "Aventura")
        filme.remover_todos_filmes()
        self.assertEquals(0, len(filme.listar_filmes()))

    def test_iniciar_filmes(self):
        filme.iniciar_filmes()
        self.assertEquals(2, len(filme.listar_filmes()))

if __name__ == '__main__':
    unittest.main()
