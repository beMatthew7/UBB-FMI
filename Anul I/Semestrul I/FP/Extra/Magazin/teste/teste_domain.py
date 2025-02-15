import unittest
from domain.produs import Produs

class TesteDomain(unittest.TestCase):
    def test_produs(self):
        produs = Produs(1, "Laptop", 1000)
        self.assertEqual(produs.get_id(), 1)
        self.assertEqual(produs.get_denumire(), "Laptop")
        self.assertEqual(produs.get_pret(), 1000)

        produs.set_denumire("PC")
        produs.set_pret(2000)
        self.assertEqual(produs.get_denumire(), "PC")
        self.assertEqual(produs.get_pret(), 2000)