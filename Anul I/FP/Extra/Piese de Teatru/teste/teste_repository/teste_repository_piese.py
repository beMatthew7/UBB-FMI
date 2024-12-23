from domain.piesa import Piesa
from repository.repository_piese import RepositoryPieseFile, RepositoryPiese

import unittest
import os
class TesteRepositoryPiese(unittest.TestCase):
    def test_store(self):
        repo = RepositoryPiese()
        piesa = Piesa("titlu", "regizor", "Comedie", 10)
        repo.store(piesa)
        self.assertEqual(len(repo.get_all()), 1)
        piesa1 = Piesa("titlu1", "regizor1", "Comedie", 10)
        repo.store(piesa1)
        self.assertEqual(len(repo.get_all()), 2)

    def test_update(self):
        repo = RepositoryPiese()
        piesa = Piesa("titlu", "regizor", "Comedie", 10)
        repo.store(piesa)
        piesa1 = Piesa("titlu", "regizor", "Altele", 20)
        repo.update(piesa1)
        self.assertEqual(repo.get_all()[0].get_gen(), "Altele")
        self.assertEqual(repo.get_all()[0].get_durata(), 20)  

    def test_get_all(self):
        repo = RepositoryPiese()
        piesa = Piesa("titlu", "regizor", "Comedie", 10)
        repo.store(piesa)
        piesa1 = Piesa("titlu1", "regizor1", "Comedie", 10)
        repo.store(piesa1)
        self.assertEqual(len(repo.get_all()), 2)

class TesteRepositoryFile(unittest.TestCase):
    def test_store_to_file(self):
        repo = RepositoryPieseFile("data/test_piese.txt")
        piesa = Piesa("titlu3", "regizor3", "Comedie", 10)
        repo.store(piesa)
        piesa1 = Piesa("titlu4", "regizor4", "Comedie", 10)
        repo.store(piesa1)
        piesa2 = Piesa("titlu5", "regizor5", "Comedie", 10)
        repo.store(piesa2)
        self.assertEqual(len(repo.get_all()), 3)

      
    def tearDown(self):

        file_path = "data/test_piese.txt"
        if os.path.exists(file_path):
            with open(file_path, 'w') as file:
                file.truncate(0)  