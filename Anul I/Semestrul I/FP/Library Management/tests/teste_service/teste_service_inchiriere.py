import unittest
from unittest.mock import MagicMock
from domain.carte import Carte
from domain.client import Client
from domain.inchiriere import Inchiriere
from service.controller_inchiriere import ControllerInchirieri
from repository.repository_inchirieri import RepoInchirieri


class TestControllerInchirieri(unittest.TestCase):

    def setUp(self):
        self.client = Client(1, "Ion Popescu", "1234567890123")
        self.client2 = Client(2, "Maria Ionescu", "1234567890124")
        self.carte = Carte(1, "Cartea Test", "Descrierea cărții de test", "Autor Test", 10)
        self.inchiriere = Inchiriere(self.carte, self.client)
        self.repo = MagicMock(RepoInchirieri)
        self.controller = ControllerInchirieri(self.repo)


    def test_returneaza_carte(self):
        self.inchiriere.set_returnata = MagicMock()
        self.controller.returneaza_carte(self.inchiriere)

        self.inchiriere.set_returnata.assert_called_once_with(True)

    def test_cele_mai_inchiriate_carti(self):
        inchiriere2 = Inchiriere(self.carte, self.client2, 2)
        self.repo.get_all.return_value = [self.inchiriere, inchiriere2]

        cele_mai_inchiriate = self.controller.cele_mai_inchiriate_carti()
        self.assertEqual(cele_mai_inchiriate[0][0], self.carte)
        self.assertEqual(cele_mai_inchiriate[0][1], 3)

    def test_clienti_ord_desch_numar_carti(self):
        inchiriere2 = Inchiriere(self.carte, self.client2, 2)
        self.repo.get_all.return_value = [self.inchiriere, inchiriere2]

        clienti_ord = self.controller.clienti_ord_desch_numar_carti()
        self.assertEqual(clienti_ord[0][0], self.client)
        self.assertEqual(clienti_ord[0][1], 1)

    def test_primii_20_proc_activi(self):
        inchiriere2 = Inchiriere(self.carte, self.client2, 2)
        inchiriere3 = Inchiriere(self.carte, self.client2, 3)
        self.repo.get_all.return_value = [self.inchiriere, inchiriere2, inchiriere3]

        top_20 = self.controller.primii_20_proc_activi()


    def test_cauta_inchiriere_dupa_carte_si_client(self):
        self.repo.get_all.return_value = [self.inchiriere]
        inchiriere_gasita = self.controller.cauta_inchiriere_dupa_carte_si_client(self.carte, self.client)
        self.assertEqual(inchiriere_gasita, self.inchiriere)

    def test_sterge_inchirieri_dupa_client(self):
        self.repo.get_all.return_value = [self.inchiriere]
        self.repo.sterge_inchiriere = MagicMock()
        self.controller.sterge_inchirieri_dupa_client(self.client)
        self.repo.sterge_inchiriere.assert_called_once_with(self.inchiriere)

