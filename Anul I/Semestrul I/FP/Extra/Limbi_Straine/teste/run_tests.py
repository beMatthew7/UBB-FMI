import unittest
from teste import teste_domain, teste_repository

def run_all_tests():
    """
    Functia care ruleaza toate testele
    """
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromModule(teste_domain))
    suite.addTests(loader.loadTestsFromModule(teste_repository))

    runner = unittest.TextTestRunner()
    runner.run(suite)

