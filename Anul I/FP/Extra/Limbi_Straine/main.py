from repository.repository_cursuri import RepositoryCursuriFile
from service.service_curs import ControllerCurs
from ui.console import Console
from teste.run_tests import run_all_tests

run_all_tests()

repo = RepositoryCursuriFile("Limbi_Straine/data/cursuri.txt")
serv = ControllerCurs(repo)

console = Console(serv)

console.run()