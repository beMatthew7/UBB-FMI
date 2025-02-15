from domain.vm import VM

class RepositoryVm:
    def __init__(self):
        self.__vms = []

    def store(self, vm):
        """
        Adaugam o vm in lista
        :param vm: vm
        :return: None
        """
        self.__vms.append(vm)


    def get_all(self):
        """
        Returneaza lista de vms
        :return: lista de vms
        """
        return self.__vms
    
class RepositoryVMFile(RepositoryVm):
    def __init__(self, filename):
        super().__init__()
        self.__filename = filename
        self.__load_from_file()

    def __load_from_file(self):
        """
        Incarca datele din fisier
        :return: None
        """
        with open(self.__filename, 'r') as f:
            for line in f:
                id, nume, cpu_capacity, disk_type, price_hour = line.strip().split(',')
                id = int(id)
                cpu_capacity = float(cpu_capacity.replace("Gh", ""))
                price_hour = float(price_hour.replace("$", ""))
                vm = VM(id, nume, cpu_capacity, disk_type, price_hour)
                self.store(vm) 

    def __save_to__file(self):
        """
        Salveaza datele in fisier
        :return: None
        """
        with open(self.__filename, 'w') as f:
            for vm in self.get_all():
                f.write(f"{vm.get_id()},{vm.get_nume()},{vm.get_cpu_capacity()}Gh,{vm.get_disk_type()},{vm.get_price_hour()}$\n")

    def store(self, vm):
        """
        Adaugam o vm in lista
        :param vm: vm
        :return: None
        """
        super().store(vm)
        self.__save_to__file()                           