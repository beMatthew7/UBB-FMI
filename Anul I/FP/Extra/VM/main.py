from repository.repository_vm import RepositoryVMFile
from service.service_vm import ControllerVm
from ui.console import Console

repo = RepositoryVMFile("VM/data/vm.txt")
serv = ControllerVm(repo)
console = Console(serv)

console.run()