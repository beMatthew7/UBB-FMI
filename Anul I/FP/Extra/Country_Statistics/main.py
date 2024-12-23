from domain.tara import Tara
from repository.repository_tara import RepositoryTaraFile
from service.service_tara import ControllerTara
from domain.validator import Validator
from ui.console import Console

repo = RepositoryTaraFile("Country_Statistics/data/statistici.txt")
validator = Validator()
serv = ControllerTara(repo, validator)

console = Console(serv)

console.run()


