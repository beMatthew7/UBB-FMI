from colorama import Fore, Style

class Console:
    def __init__(self, serv):
        self.__serv = serv

    @staticmethod
    def afiseaza_meniu():
        print("1. Cauta curs pe baza limbii vizate")
        print("2. Inscriere la curs")

    def __cauta_curs_ui(self):
        """
        C
        """
        limba_straina = input("Introduceti limba straina: ")
        try:
            cursuri_disponibile = self.__serv.cauta_curs(limba_straina)
            for curs in cursuri_disponibile:
                print(Fore.GREEN + str(curs) + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + str(e) + Style.RESET_ALL) 

    def __inscriere_curs_ui(self):
        id_curs = input("Introduceti id-ul cursului: ")
        try:
            numar_ore = int(input("Introduceti numarul de ore: "))
        except  ValueError:
            print(Fore.RED + "Numarul de ore trebuie sa fie un numar intreg" + Style.RESET_ALL)
            return    
        try:
            inscriere = self.__serv.inscriere_curs(id_curs, numar_ore)
            print(inscriere)
            print(Fore.GREEN + "Inscriere efectuata cu succes" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + str(e) + Style.RESET_ALL)              
    def run(self):
        while True:
            self.afiseaza_meniu()
            optiune = input("Introduceti optiunea: ")
            match optiune:
                case "1":
                    self.__cauta_curs_ui()
                case "2":
                    self.__inscriere_curs_ui()    
                case "E":
                    break
                case _:
                    print(Fore.RED + "Optiune invalida" + Style.RESET_ALL)        
   