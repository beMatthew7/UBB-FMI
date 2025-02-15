from colorama import Fore, Style

class Console:
    def __init__(self, serv):
        self.__serv = serv


    @staticmethod
    def afiseaza_meniu():
        print("1. Adauga piesa")
        print("2. Modifica piesa")
        print("3. Creeaza piese aleator")
        print("4. Exporta piese sortate dupa regizor si titlu")

    def __adauga_piesa_ui(self):
        print("Introduceti datele despre piesa")
        titlu = input("Introduceti titul piesei de teatru: ")
        regizor = input("Introduceti regizorul piesei de teatru: ")
        gen = input("Introduceti genul piesei de teatru: ")
        try:
            durata = int(input("Introduceti durata piesei de teatru: "))
        except:
            print("Durata trebuie sa fie un numar")
            return
        try:    
            self.__serv.adauga_piesa(titlu, regizor, gen, durata)
            print(Fore.GREEN + "Piesa de teatru a fost adăugat cu succes." + Style.RESET_ALL)
        except Exception as ve:
            print(Fore.RED + str(ve) + Style.RESET_ALL)  

    def __modifica_piesa_ui(self):
        titlu = input("Introduceti titlul piesei pe care doriri sa o modificati: ")
        regizor = input("Introduceti regizorul piesei pe care doriti sa o modificati: ")
        new_gen = input("Introduceti noul gen al piesei: ")
        try:
            new_durata = int(input("Introduceti noua durata a piesei de teatru: "))
        except:
            print(Fore.RED + "Durata trebuie sa fie un numar" + Style.RESET_ALL)
            return
        try:
            self.__serv.modifica_piesa(titlu, regizor, new_gen, new_durata)
            print(Fore.GREEN + "Piesa a fost modificata cu succes" + Style.RESET_ALL)
        except Exception as ve:
            print(Fore.RED + str(ve) + Style.RESET_ALL) 


    def __exporta_piese_ui(self):
        nume_fisier = input("Introduceti numele fisierurlui unde doriti sa exportati: ")
        self.__serv.exporta_piese(nume_fisier)

    def __creeaza_piese_random_ui(self):
        try:
            numar = int(input("Introduceti cate piese de teatru aleatoriu doriti sa se genereze: "))
        except: 
            print(Fore.RED + "trebuie sa fie un numar" + Style.RESET_ALL)
            return    

        self.__serv.creeaza_piese_random(numar)
        print(Fore.GREEN + F"Au fost generate {numar} piese de teatru" + Style.RESET_ALL)
    def run(self):
        while True:
            self.afiseaza_meniu()
            option = input(">>>>").strip().capitalize()
            match option:
                case '1':
                    self.__adauga_piesa_ui()  
                case '2':
                    self.__modifica_piesa_ui()   
                case '3':
                    self.__creeaza_piese_random_ui()
                case '4':
                    self.__exporta_piese_ui()
