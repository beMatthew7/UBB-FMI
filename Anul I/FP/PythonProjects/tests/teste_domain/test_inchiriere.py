import unittest
from domain.inchiriere import Inchiriere
from domain.carte import Carte
from domain.client import Client

class TestInchiriere(unittest.TestCase):

    def setUp(self):
        self.client = Client(1, "Ion Popescu", "1234567890123")
        self.carte = Carte(1, "Cartea Test", "Descrierea cărții de test", "Autor Test", 10)
        self.inchiriere = Inchiriere(self.carte, self.client, 3)

    def test_initializare_inchiriere(self):
        self.assertEqual(self.inchiriere.get_carte(), self.carte)
        self.assertEqual(self.inchiriere.get_client(), self.client)
        self.assertEqual(self.inchiriere.get_nr_inchirieri(), 3)


    def test_set_nr_inchirieri(self):
        self.inchiriere.set_nr_inchirieri(5)
        self.assertEqual(self.inchiriere.get_nr_inchirieri(), 5)



    def test_str_method(self):
        self.inchiriere.set_returnata(True)
        expected_str = f"Cartea: {self.carte} este închiriată de {self.client}. Status: returnată, Număr de închirieri: 3"
        self.assertEqual(str(self.inchiriere), expected_str)

        self.inchiriere.set_returnata(False)
        expected_str = f"Cartea: {self.carte} este închiriată de {self.client}. Status: ne-returnată, Număr de închirieri: 3"
        self.assertEqual(str(self.inchiriere), expected_str)

    def test_initializare_inchiriere_default(self):
        inchiriere_default = Inchiriere(self.carte, self.client)
        self.assertEqual(inchiriere_default.get_nr_inchirieri(), 1)

if __name__ == "__main__":
    unittest.main()
