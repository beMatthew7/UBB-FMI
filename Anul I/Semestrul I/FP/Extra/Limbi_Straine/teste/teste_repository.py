from repository.repository_cursuri import RepositoryCursuri, RepositoryCursuriFile
import unittest
from domain.curs import Curs
import os
class TesteRepositoryCursuri(unittest.TestCase):
    def test_store(self):
        repo = RepositoryCursuri()
        curs = Curs(1, "engleza", "A2", 1000)
        repo.store(curs)
        self.assertEqual(curs.get_id_curs(), 1)
        self.assertEqual(curs.get_limba_straina(), "engleza")
        self.assertEqual(curs.get_nivel(), "A2")
        self.assertEqual(curs.get_pret(), 1000)
        self.assertEqual(len(repo.get_all()), 1)

class TesteRepositoryCursuriFile(unittest.TestCase):
    def setUp(self):
        with open("test_cursuri.txt", "w") as f:
            f.write("1,engleza,A2,1000\n")
            f.write("2,franceza,B1,1500\n")

    def test_load_from_file(self):
        repo = RepositoryCursuriFile("test_cursuri.txt")
        cursuri = repo.get_all()
        self.assertEqual(len(cursuri), 2)

    def test_save_to_file(self):
        repo = RepositoryCursuriFile("test_cursuri.txt")
        curs = Curs(3, "spaniola", "C1", 2000)
        repo.store(curs)
        cursuri = repo.get_all()
        self.assertEqual(len(cursuri), 3)
        curs2 = Curs(3, "spaniola", "C1", 2000)
        repo.store(curs)
        with open("test_cursuri.txt", "r") as f:
            lines = f.readlines()
            self.assertEqual(lines[2].strip(), "3,spaniola,C1,2000")

    def tearDown(self):
        os.remove("test_cursuri.txt")        