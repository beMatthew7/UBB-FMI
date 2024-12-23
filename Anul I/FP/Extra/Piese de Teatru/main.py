from teste.run_tests import run_all_tests
from domain.piesa import Piesa
from domain.validator import PiesaValidator, ValidationException
from repository.repository_piese import RepositoryPieseFile
from service.service_piesa import ControllerPiesa
from ui.console import Console
run_all_tests()

validator = PiesaValidator()
repo = RepositoryPieseFile("data/piese_de_teatru.txt")
service = ControllerPiesa(repo, validator)

console = Console(service)

console.run()