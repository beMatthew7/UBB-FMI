from colorama import Fore, Style

class Console:
    def __init__(self, book_service):
        self.__serv = book_service

    @staticmethod
    def afiseaza_meniu():
        print("1. Adauga carte la lista")
        print("2. Actualizeaza o carte din lista")
        print("3. Sterge cartea cu un anumit ID")
        print("4. Afiseaza toate cartile care au acelasi autor")
        print("5. Caută o carte după titlu")
        print("D. Adauga carti default")
        print("P. Afiseaza lista carti")
        print("E. Iesire din aplicatie")

    def citeste_info_carte(self) -> tuple:
        id = int(input("Introduceți ID-ul cărții: "))
        titlu = input("Introduceți titlul cărții: ")
        descriere = input("Introduceți descrierea cărții: ")
        autor = input("Introduceți autorul cărții: ")
        return id, titlu, descriere, autor

    def afiseaza_carti(self, lista_carti):
        for carte in lista_carti:
            print(carte)

    def adauga_carte_ui(self):
        id, titlu, descriere, autor = self.citeste_info_carte()
        try:
            self.__serv.adauga_carte(id, titlu, descriere, autor)
            print(Fore.GREEN + "Adaugare realizata cu succes." + Style.RESET_ALL)
        except ValueError as ve:
            print(Fore.RED + str(ve) + Style.RESET_ALL)

    def actualizeaza_carte_ui(self):
        id = int(input("Introduceți ID-ul cărții de actualizat: "))
        titlu_nou = input("Introduceți noul titlu: ")
        descriere_noua = input("Introduceți noua descriere: ")
        autor_nou = input("Introduceți noul autor: ")


        titlu_nou = titlu_nou if titlu_nou else None
        descriere_noua = descriere_noua if descriere_noua else None
        autor_nou = autor_nou if autor_nou else None

        try:
            self.__serv.actualizeaza_carte(id, titlu_nou, descriere_noua, autor_nou)
            print(Fore.GREEN + "Actualizare realizata cu succes." + Style.RESET_ALL)
        except ValueError as ve:
            print(Fore.RED + str(ve) + Style.RESET_ALL)

    def sterge_carte_ui(self):
        id = int(input("Introduceți ID-ul cărții de șters: "))
        try:
            self.__serv.delete_carte(id)
            print(Fore.GREEN + "Ștergerea a fost realizată cu succes." + Style.RESET_ALL)
        except ValueError as ve:
            print(Fore.RED + str(ve) + Style.RESET_ALL)

    def filtreaza_dupa_autor_ui(self):
        autor = input("Introduceți autorul cărților de afișat: ")
        lista_filtrata = self.__serv.filtreaza_dupa_autor(autor)
        
        if lista_filtrata:
            print(f"Toate cărțile scrise de {autor} sunt:")
            self.afiseaza_carti(lista_filtrata)
        else:
            print(Fore.RED + f"Nu există cărți scrise de {autor}." + Style.RESET_ALL)

    def cauta_carte_dupa_titlu_ui(self):
        titlu = input("Introduceți titlul cărții de căutat: ")
        carte_gasita = self.__serv.cauta_carte_dupa_titlu(titlu)
        
        if carte_gasita:
            print("Cartea găsită este:", carte_gasita)
        else:
            print(Fore.RED + "Nu există nicio carte cu titlul specificat." + Style.RESET_ALL)

    def run(self):
        is_running = True
        while is_running:
            self.afiseaza_meniu()
            optiune = input(">>>").upper().strip()
            match optiune:
                case '1':
                    self.adauga_carte_ui()
                case '2':
                    self.actualizeaza_carte_ui()
                case '3':
                    self.sterge_carte_ui()
                case '4':
                    self.filtreaza_dupa_autor_ui()
                case '5':
                    self.cauta_carte_dupa_titlu_ui()

                case 'P':
                    self.afiseaza_carti(self.__serv.get_all())
                case 'D':
                    self.__serv.add_default()
                    print("S-au adaugat cărțile default.")
                case 'E':
                    is_running = False
