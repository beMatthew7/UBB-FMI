from domain.produs import Produs
from repository.repository_produse import RepositoryProduseFile
from service.controller_produs import ControllerProdus
from ui.console import Console
from teste.run_tests import run_all_tests

run_all_tests()
repo = RepositoryProduseFile("Magazin/data/produse.txt")
serv = ControllerProdus(repo)

console = Console(serv)

console.run()