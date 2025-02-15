from domain.vm import VM
class ControllerVm:
    def __init__(self, repo):
        self.__repo = repo

    def afisare_vm_cpu(self, x, y):
        """
        Afisam toate vm-urile care au cpu_capacity intre x si y
        :param x: int
        :param y: int
        :return: lista de vm-uri
        """
        lista = []
        for vm in self.__repo.get_all():
            if vm.get_cpu_capacity() >= x and vm.get_cpu_capacity() <= y:
                lista.append(f"{vm.get_nume()} , {vm.get_disk_type()}")
                
        if(lista == []):
            raise ValueError(f"Nu exista vm-uri cu cpu_capacity intre {x} si {y}!")  

        return lista    
    
    def afisare_pret_mediu(self, ore):
        """
        Afisam pretul mediu al vm-urilor pentru un anumit interval
        :param ore:
        :return: float
        """
        lista = []
        suma_price_hour = {}
        for vm in self.__repo.get_all():
            if suma_price_hour.get(vm.get_disk_type()) is None:
                suma_price_hour[vm.get_disk_type()] = 0
            suma_price_hour[vm.get_disk_type()] += vm.get_price_hour()  

        numar_elemente = {}

        for vm in self.__repo.get_all():
            if numar_elemente.get(vm.get_disk_type()) is None:
                numar_elemente[vm.get_disk_type()] = 0
            numar_elemente[vm.get_disk_type()] += 1

        medie_price_hour = {}

        for vm in self.__repo.get_all():
            medie_price_hour[vm.get_disk_type()] = round((suma_price_hour[vm.get_disk_type()] / numar_elemente[vm.get_disk_type()] * ore)} , 2)

        for vm in self.__repo.get_all():
            lista.append(f"     -{vm.get_disk_type()}: {medie_price_hour[vm.get_disk_type()]}$")

        lista = list(set(lista))
        return lista    


            