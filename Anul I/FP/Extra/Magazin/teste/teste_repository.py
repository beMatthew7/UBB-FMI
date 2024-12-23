import unittest
from domain.produs import Produs
from repository.repository_produse import RepositoryProduse, RepositoryProduseFile

import os
class TesteRepository(unittest.TestCase):
    def test_store(self):
        repo = RepositoryProduse()
        produs = Produs(1, "Laptop", 1000)
        repo.store(produs)
        self.assertEqual(len(repo.get_all()), 1)
        produs2 = Produs(2, "PC", 2000)
        repo.store(produs2)
        self.assertEqual(len(repo.get_all()), 2)

    def test_delete(self):
        repo = RepositoryProduse()
        produs = Produs(1, "Laptop", 1000)
        repo.store(produs)
        produs2 = Produs(2, "PC", 2000)
        repo.store(produs2)
        repo.delete(1)
        self.assertEqual(len(repo.get_all()), 1)
        repo.delete(2)
        self.assertEqual(len(repo.get_all()), 0)    

    def test_undo(self):
        repo = RepositoryProduse()
        produs = Produs(1, "Laptop", 1000)
        repo.store(produs)
        produs2 = Produs(2, "PC", 2000)
        repo.store(produs2)
        repo.delete(1)
        self.assertEqual(len(repo.get_all()), 1)
        repo.undo()
        self.assertEqual(len(repo.get_all()), 2)
        repo.delete(2)
        self.assertEqual(len(repo.get_all()), 1)
        repo.undo()
        self.assertEqual(len(repo.get_all()), 2)    

class TesteRepositoryFile(unittest.TestCase):
    def setUp(self):
        with open("Magazin/data/test_produse.txt", "w") as f:
            f.write("")

    def teste_load_from_file(self):
        repo = RepositoryProduseFile("Magazin/data/test_produse.txt")
        produs1 = Produs(1, "Laptop", 1000)
        repo.store(produs1)
        self.assertEqual(len(repo.get_all()), 1)
        produs2 = Produs(2, "PC", 2000)
        repo.store(produs2)
        self.assertEqual(len(repo.get_all()), 2)

    def teste_store(self):
        repo = RepositoryProduseFile("Magazin/data/test_produse.txt")
        produs1 = Produs(1, "Laptop", 1000)
        repo.store(produs1)
        self.assertEqual(len(repo.get_all()), 1)
        produs2 = Produs(2, "PC", 2000)
        repo.store(produs2)
        self.assertEqual(len(repo.get_all()), 2)

    def teste_delete(self):
        repo = RepositoryProduseFile("Magazin/data/test_produse.txt")
        produs1 = Produs(1, "Laptop", 1000)
        repo.store(produs1)
        produs2 = Produs(2, "PC", 2000)
        repo.store(produs2)
        repo.delete(1)
        self.assertEqual(len(repo.get_all()), 1)
        repo.delete(2)
        self.assertEqual(len(repo.get_all()), 0)

    def teste_undo(self):
        repo = RepositoryProduseFile("Magazin/data/test_produse.txt")
        produs1 = Produs(1, "Laptop", 1000)
        repo.store(produs1)
        self.assertEqual(len(repo.get_all()), 1)
        repo.delete(1)
        self.assertEqual(len(repo.get_all()), 0)
        repo.undo()
        self.assertEqual(len(repo.get_all()), 1)

    def tearDown(self):
        os.remove("Magazin/data/test_produse.txt")
                  