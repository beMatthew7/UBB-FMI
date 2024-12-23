import unittest
from domain.curs import Curs
class TesteDomain(unittest.TestCase):
    def test_domain(self):
        curs = Curs(1, "engleza", "A2", 1000)
        self.assertEqual(curs.get_id_curs(), 1)
        self.assertEqual(curs.get_limba_straina(), "engleza")
        self.assertEqual(curs.get_nivel(), "A2")
        self.assertEqual(curs.get_pret(), 1000)