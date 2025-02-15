from colorama import Fore, Style

class Console:
    def __init__(self, serv):
        self.__serv = serv

    @staticmethod
    def afiseaza_meniu():
        print("1. Adauga produs")
        print("2. Sterge produs")
        print("3. Filtrare produse")
        print("4. Undo")
        print("E. Exit")

    def adauga_produs_ui(self):
        """
        Interfata pentru adaugat produs
        """
        try:
            id = int(input("Introduceti id-ul: "))
        except ValueError:
            print(Fore.RED + "Id ul trebuie sa fie un numar" + Style.RESET_ALL)
            return  
        denumire = input("Introduceti denumirea: ")
        try:
            pret = float(input("Introduceti pretul: "))
        except ValueError:
            print(Fore.RED + "Pretul trebuie sa fie un numar" + Style.RESET_ALL)
            return 
        try:   
            self.__serv.adauga_produs(id, denumire, pret)
            print(Fore.GREEN + "Produs adaugat cu succes" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + str(e) + Style.RESET_ALL)    

    def sterge_produs_ui(self):
        """
        Interfata pentru stergere produs
        """
        try:
            cifra = int(input("Introduceti cifra: "))
        except ValueError:
            print(Fore.RED + "Cifra trebuie sa fie un numar" + Style.RESET_ALL)
            return
        try:
            self.__serv.sterge_produs(cifra)
            print(Fore.GREEN + "Produse sterse cu succes" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + str(e) + Style.RESET_ALL)

    def filtrare_produse_ui(self):
        """
        Interfata pentru filtrare produse
        """
        text = input("Introduceti textul: ")
        try:
            numar = int(input("Introduceti numarul: "))
        except ValueError:
            print(Fore.RED + "Numarul trebuie sa fie un numar" + Style.RESET_ALL)
            return
        produse_filtrate = self.__serv.filtrare_produse(text, numar)
        if len(produse_filtrate) == 0:
            print(Fore.RED + "Nu exista produse care sa contina textul si sa aiba pretul mai mic decat numarul introdus" + Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Produsele filtrate sunt: " + Style.RESET_ALL)
            for produs in produse_filtrate:
                print(produs)

    def undo_ui(self):
        """
        Interfata pentru undo
        """
        try:
            self.__serv.undo()
            print(Fore.GREEN + "Undo realizat cu succes" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + str(e) + Style.RESET_ALL)

    def run(self):
        while True:
            self.afiseaza_meniu()
            optiune = input("Introduceti optiunea: ").strip().capitalize()
            match optiune:
                case "1":
                    self.adauga_produs_ui()
                case "2":
                    self.sterge_produs_ui()
                case "3":
                    self.filtrare_produse_ui()
                case "4":
                    self.undo_ui()
                case "E":
                    break
                case _:
                    print(Fore.RED + "Optiune invalida" + Style.RESET_ALL)
