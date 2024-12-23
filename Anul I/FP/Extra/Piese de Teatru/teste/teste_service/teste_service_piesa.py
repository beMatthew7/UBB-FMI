from service.service_piesa import ControllerPiesa
from repository.repository_piese import RepositoryPieseFile
from domain.piesa import Piesa
from domain.validator import PiesaValidator
import unittest
import os
class TesteService(unittest.TestCase):
    def setUp(self):
        self.repo = RepositoryPieseFile("data/test_piese.txt")
        self.service = ControllerPiesa(self.repo, PiesaValidator())

    def test_adauga_piesa(self):
        self.service.adauga_piesa("titlu3", "regizor3", "Comedie", 10)
        self.assertEqual(len(self.repo.get_all()), 1)

    def test_modifica_piesa(self):
        self.service.adauga_piesa("titlu", "regizor", "Comedie", 10)
        self.service.modifica_piesa("titlu", "regizor", "Altele", 20)
        piese = self.repo.get_all()
        self.assertEqual(piese[0].get_gen(), "Altele")
        self.assertEqual(piese[0].get_durata(), 20)

    def test_genereaza_piese_random(self):
        self.service.creeaza_piese_random(5)
        self.assertEqual(len(self.repo.get_all()), 5)

    def test_exporta_piese(self):
        self.service.adauga_piesa("titlu2", "regizor2", "Comedie", 10)
        self.service.exporta_piese("data/export_test.txt")
        with open("data/export_test.txt", "r") as f:
            lines = f.readlines()
            self.assertEqual(len(lines), 1)
            self.assertEqual(lines[0], "titlu2,regizor2,Comedie,10\n")

    def tearDown(self):

        file_path = "data/test_piese.txt"
        if os.path.exists(file_path):
            with open(file_path, 'w') as file:
                file.truncate(0)  

                