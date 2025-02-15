from colorama import Fore, Style

class Console:
    def __init__(self, serv):
        """
        Initializam consola
        :param serv: service-ul pentru tari
        """
        self.__serv = serv

    def __afisare_vm_cpu_ui(self):
        try:
            x = int(input("Introduceti capatul inferior al intervalului: "))
        except ValueError:
            print(Fore.RED + "Capatul inferior trebuie sa fie un numar intreg!" + Style.RESET_ALL)
            return
        try:
            y = int(input("Introduceti capatul superior al intervalului: "))
        except ValueError:
            print(Fore.RED + "Capatul superior trebuie sa fie un numar intreg!" + Style.RESET_ALL)
        if x > y:
            print(Fore.RED + "Capatul inferior trebuie sa fie mai mic decat capatul superior!" + Style.RESET_ALL)
            return
        
        try:
            lista = self.__serv.afisare_vm_cpu(x, y)
            for vm in lista:
                print(vm) 
        except Exception as e:
            print(Fore.RED + str(e) + Style.RESET_ALL)   

    def __afisare_pret_mediu_ui(self):
        try:
            ore = int(input("Introduceti numarul de ore: "))  
        except ValueError:
            print(Fore.RED + "Numarul de ore trebuie sa fie un numar intreg!" + Style.RESET_ALL)
            return
        
        lista = self.__serv.afisare_pret_mediu(ore)
        for vm in lista:
            print(vm)
                            
    @staticmethod
    def afisare_meniu():
        print("1. Afisare VM cu capcaitatea CPU intr-un interval dat")
        print("2. Pretul mediu calculcat pe un numar de ore citite")

    def run(self):
        while True:
            self.afisare_meniu()
            optiune = input("Introduceti optiunea: ")
            match optiune:
                case "1":
                    self.__afisare_vm_cpu_ui()
                case "2":
                    self.__afisare_pret_mediu_ui()
                case "exit":
                    break
                case _:
                    print(Fore.RED + "Optiune invalida!" + Style.RESET_ALL)       