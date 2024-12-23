from service.controller_produs import ControllerProdus
from repository.repository_produse import RepositoryProduseFile

import unittest
import os
class TesteService(unittest.Testcase):
    def setUp(self):
        with open("Magazin/data/test_produse.txt", "w") as f:
            f.write("")
        self.repo = RepositoryProduseFile("Magazin/data/test_produse.txt")
        self.serv = ControllerProdus(self.repo)

    def test_adauga_produs(self):
        self.serv.adauga_produs(1, "Laptop", 1000)
        self.assertEqual(len(self.repo.get_all()), 1)
        self.serv.adauga_produs(2, "PC", 2000)
        self.assertEqual(len(self.repo.get_all()), 2)

    def test_sterge_produs(self):
        self.serv.adauga_produs(1, "Laptop", 1000)
        self.serv.adauga_produs(2, "PC", 2000)
        self.serv.sterge_produs(1)
        self.assertEqual(len(self.repo.get_all()), 1)
        self.serv.sterge_produs(2)
        self.assertEqual(len(self.repo.get_all()), 0)

    def test_filtrare_produse(self):
        self.serv.adauga_produs(1, "Laptop", 1000)
        self.serv.adauga_produs(2, "PC", 2000)
        self.serv.adauga_produs(3, "Telefon", 500)
        self.serv.adauga_produs(4, "Tablet", 300)
        self.serv.adauga_produs(5, "Telefon", 700)
        self.assertEqual(len(self.serv.filtrare_produse("Laptop", 1500)), 1)
        self.assertEqual(len(self.serv.filtrare_produse("Telefon", 600)), 2)
        self.assertEqual(len(self.serv.filtrare_produse("", -1)), 5)
        
        
    def tearDown(self):
        os.remove("Magazin/data/test_produse.txt")    