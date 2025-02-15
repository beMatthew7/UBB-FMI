import unittest
from domain.client import Client


class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = Client(1, "Ion Popescu", "1234567890123")

    def test_get_id_client(self):
        self.assertEqual(self.client.get_id_client(), 1)

    def test_get_nume(self):
        self.assertEqual(self.client.get_nume(), "Ion Popescu")

    def test_set_nume(self):
        self.client.set_nume("Alexandru Ionescu")
        self.assertEqual(self.client.get_nume(), "Alexandru Ionescu")

    def test_get_CNP(self):
        self.assertEqual(self.client.get_CNP(), "1234567890123")

    def test_set_CNP(self):
        self.client.set_CNP("9876543210987")
        self.assertEqual(self.client.get_CNP(), "9876543210987")

    def test_eq_operator(self):
        client2 = Client(1, "Ion Popescu", "1234567890123")
        self.assertTrue(self.client == client2)

        client3 = Client(2, "Maria Ionescu", "2345678901234")
        self.assertFalse(self.client == client3)

    def test_hash(self):
        client_set = {self.client}
        client2 = Client(1, "Ion Popescu", "1234567890123")
        client_set.add(client2)  # Nu ar trebui să adauge un client duplicat
        self.assertEqual(len(client_set), 1)

    def test_str(self):
        expected_str = "[1] Client: Nume = Ion Popescu; CNP = 1234567890123"
        self.assertEqual(str(self.client), expected_str)


if __name__ == "__main__":
    unittest.main()
