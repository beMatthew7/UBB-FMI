from colorama import Fore, Style

class Console:
    def __init__(self, serv):
        """
        Initializam consola
        :param serv: service-ul pentru tari
        """
        self.__serv = serv

    @staticmethod
    def afiseaza_meniu():
        print("1.Adaugare statistica")
        print("2. Afisarea tarilor cu o rata de inflatie mai mica")

    def __adaugare_statistica_ui(self):
        nume = input("Introduceti numele tarii: ")
        try:
            an = int(input("Introduceti anul: "))
        except ValueError:
            print(Fore.RED + "Anul trebuie sa fie un numar intreg!" + Style.RESET_ALL) 
            return   
        try:
            inflatie = float(input("Introduceti inflatia: "))
        except ValueError:
            print(Fore.RED + "Inflatia trebuie sa fie un numar!" + Style.RESET_ALL) 
            return
        try:       
            unemployment_rate = float(input("Introduceti rata de desemnare: "))
        except ValueError:
            print(Fore.RED + "Rata de somaj trebuie sa fie un numar!" + Style.RESET_ALL)  
            return  
        try:
            populatie = int(input("Introduceti populatia: "))
        except ValueError:
            print(Fore.RED + "Populatia trebuie sa fie un numar intreg!" + Style.RESET_ALL)
            return
        try:    
            self.__serv.adaugare_statistica(nume, an, inflatie, unemployment_rate, populatie)
            print(Fore.GREEN + "Tara adaugata cu succes!" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + str(e) + Style.RESET_ALL)

    def __afisare_tari_cu_inflatie_mica_ui(self):
        try:
            rata = float(input("Introduceti rata de inflatie: "))
            self.__serv.afisare_tari_cu_inflatie_mica(rata)
            
            
        except ValueError:
            print(Fore.RED + "Rata de inflatie trebuie sa fie un numar!" + Style.RESET_ALL)

    def run(self):
        while True:
            self.afiseaza_meniu()
            optiune = input("Introduceti optiunea: ")
            match optiune:
                case "1":
                    self.__adaugare_statistica_ui()
                case "2":
                    self.__afisare_tari_cu_inflatie_mica_ui()
                case "exit":
                    break
                case _:
                    print(Fore.RED + "Optiune invalida!" + Style.RESET_ALL)
    