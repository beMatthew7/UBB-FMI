import unittest
from unittest.mock import MagicMock
from domain.carte import Carte
from domain.client import Client
from domain.inchiriere import Inchiriere
from repository.repository_inchirieri import RepoInchirieri, RepositoryInchirieriFile

class TestRepoInchirieri(unittest.TestCase):

    def setUp(self):
        self.client = Client(1, "Ion Popescu", "1234567890123")
        self.carte = Carte(1, "Cartea Test", "Descrierea cărții de test", "Autor Test", 10)
        self.inchiriere = Inchiriere(self.carte, self.client, 3)
        self.repo = RepoInchirieri()

    def test_adauga_inchiriere(self):
        self.repo.adauga_inchiriere(self.inchiriere)
        inchirieri = self.repo.get_all()
        self.assertIn(self.inchiriere, inchirieri)

    def test_sterge_inchiriere(self):
        self.repo.adauga_inchiriere(self.inchiriere)
        self.repo.sterge_inchiriere(self.inchiriere)
        inchirieri = self.repo.get_all()
        self.assertNotIn(self.inchiriere, inchirieri)


class TestRepositoryInchirieriFile(unittest.TestCase):

    def setUp(self):
        self.client = Client(1, "Ion Popescu", "1234567890123")
        self.carte = Carte(1, "Cartea Test", "Descrierea cărții de test", "Autor Test", 10)
        self.inchiriere = Inchiriere(self.carte, self.client, 3)


        self.repo_carti = MagicMock()
        self.repo_clienti = MagicMock()
        self.repo = RepositoryInchirieriFile("test_inchirieri.txt", self.repo_carti, self.repo_clienti)

    def test_incarcare_inchirieri_din_fisier(self):
        self.repo_carti.find_book.return_value = self.carte
        self.repo_clienti.find_client.return_value = self.client


        data_fisier = "1,Cartea Test,Autor Test,3,1,Ion Popescu,1234567890123\n"
        with open(self.repo._RepositoryInchirieriFile__filename, 'w') as file:
            file.write(data_fisier)

        self.repo._RepositoryInchirieriFile__load_from_file()

        inchirieri = self.repo.get_all()
        self.assertEqual(len(inchirieri), 1)
        self.assertEqual(inchirieri[0].get_carte(), self.carte)
        self.assertEqual(inchirieri[0].get_client(), self.client)

    def test_salvare_inchirieri_in_fisier(self):

        self.repo.adauga_inchiriere(self.inchiriere)

        with open(self.repo._RepositoryInchirieriFile__filename, 'r') as file:
            lines = file.readlines()

        self.assertEqual(len(lines), 1)
        self.assertTrue("Cartea Test" in lines[0])
        self.assertTrue("Ion Popescu" in lines[0])

    def test_stergere_inchiriere_si_salvare(self):

        self.repo.adauga_inchiriere(self.inchiriere)
        self.repo.sterge_inchiriere(self.inchiriere)

        with open(self.repo._RepositoryInchirieriFile__filename, 'r') as file:
            lines = file.readlines()

        self.assertEqual(len(lines), 0)


if __name__ == '__main__':
    unittest.main()
