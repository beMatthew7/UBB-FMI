import unittest
from domain.client import Client
from domain.validation_client import ValidatorClient
from repository.repository_clienti import RepositoryClienti
from service.controller_client import ControllerClienti

class TestControllerClienti(unittest.TestCase):
    
    def setUp(self):
        self.repo = RepositoryClienti()
        self.validator = ValidatorClient()
        self.controller = ControllerClienti(self.repo, self.validator)

    def test_adauga_client_nou(self):
        self.controller.adauga_client_nou(1, "Ion Popescu", "1234567890123")
        client = self.repo.find_client(1)
        self.assertIsNotNone(client)
        self.assertEqual(client.get_nume(), "Ion Popescu")
        self.assertEqual(client.get_CNP(), "1234567890123")

    def test_adauga_client_nou_dupa_id_existent(self):
        self.controller.adauga_client_nou(1, "Ion Popescu", "1234567890123")
        with self.assertRaises(ValueError):
            self.controller.adauga_client_nou(1, "Maria Ionescu", "2234567890123")

    def test_actualizeaza_date_client(self):
        self.controller.adauga_client_nou(2, "Ion Popescu", "1234567890123")
        self.controller.actualizeaza_date_client(2, nume_nou="Marian Ion", cnp_nou="2234567890123")
        client = self.repo.find_client(2)
        self.assertEqual(client.get_nume(), "Marian Ion")
        self.assertEqual(client.get_CNP(), "2234567890123")

    def test_actualizeaza_date_client_nonexistent(self):
        with self.assertRaises(ValueError):
            self.controller.actualizeaza_date_client(999, nume_nou="Marian Ion")

    def test_cauta_client_dupa_id(self):
        self.controller.adauga_client_nou(3, "Ion Popescu", "1234567890123")
        client = self.controller.cauta_client_dupa_id(3)
        self.assertIsNotNone(client)
        self.assertEqual(client.get_nume(), "Ion Popescu")

    def test_cauta_client_dupa_id_inexistent(self):
        client = self.controller.cauta_client_dupa_id(999)
        self.assertIsNone(client)

    def test_sterge_client_dupa_id(self):
        self.controller.adauga_client_nou(4, "Ion Popescu", "1234567890123")
        self.controller.sterge_client_dupa_id(4)
        client = self.repo.find_client(4)
        self.assertIsNone(client)

    def test_sterge_client_dupa_id_inexistent(self):
        with self.assertRaises(ValueError):
            self.controller.sterge_client_dupa_id(999)

    def test_filtreaza_clienti_dupa_nume(self):
        self.controller.adauga_client_nou(5, "Ion Popescu", "1234567890123")
        self.controller.adauga_client_nou(6, "Maria Ionescu", "2234567890123")
        clienti = self.controller.filtreaza_clienti_dupa_nume("Ion Popescu")
        self.assertEqual(len(clienti), 1)
        self.assertEqual(clienti[0].get_nume(), "Ion Popescu")

    def test_cauta_client_pe_baza_cnp(self):
        self.controller.adauga_client_nou(7, "Ion Popescu", "1234567890123")
        client = self.controller.cauta_client_pe_baza_cnp("1234567890123")
        self.assertIsNotNone(client)
        self.assertEqual(client.get_nume(), "Ion Popescu")

    def test_obtine_toti_clientii(self):
        self.controller.adauga_client_nou(8, "Ion Popescu", "1234567890123")
        self.controller.adauga_client_nou(9, "Maria Ionescu", "2234567890123")
        clienti = self.controller.obtine_toti_clientii()
        self.assertEqual(len(clienti), 2)

if __name__ == '__main__':
    unittest.main()
