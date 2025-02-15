import unittest
from teste import teste_domain, teste_repository, teste_controller

def  run_all_tests():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

  
    suite.addTest(loader.loadTestsFromModule(teste_domain))
    suite.addTest(loader.loadTestsFromModule(teste_repository))
    suite.addTest(loader.loadTestsFromModule(teste_controller))


    runner = unittest.TextTestRunner()

    runner.run(suite)