import random
from colorama import Fore, Style

class Console:
    def __init__(self, book_service, client_service):
        self.__book_service = book_service
        self.__client_service = client_service

    @staticmethod
    def afiseaza_meniu():
        print("1. Adaugă carte la listă")
        print("2. Actualizează o carte din listă")
        print("3. Șterge cartea cu un anumit ID")
        print("4. Afișează toate cărțile care au același autor")
        print("5. Caută o carte după titlu")
        print("6. Adaugă client la listă")
        print("7. Actualizează un client din listă")
        print("8. Șterge clientul cu un anumit ID")
        print("9. Caută client după ID")
        print("10. Caută client după CNP")
        print("B. Inchiriere carte")
        print("R1. Adaugă carti random")
        print("C. Adaugă cărți și clienți implicite")
        print("A1. Afișează lista cărților")
        print("A2. Afiseaza lista de clienti")
        print("E. Ieșire din aplicație")

    def genereaza_x_carti_random_ui(self):
        
        x = int(input("Introduceți numărul de cărți random de generat: "))
        self.__book_service.genereaza_carti_random(x)
        print(Fore.GREEN + f"{x} cărți random au fost generate și adăugate cu succes!" + Style.RESET_ALL)





    def citeste_info_carte(self) -> tuple:
        id = int(input("Introduceți ID-ul cărții: "))
        titlu = input("Introduceți titlul cărții: ")
        descriere = input("Introduceți descrierea cărții: ")
        autor = input("Introduceți autorul cărții: ")
        return id, titlu, descriere, autor

    def citeste_info_client(self) -> tuple:
        id = int(input("Introduceți ID-ul clientului: "))
        nume = input("Introduceți numele clientului: ")
        cnp = input("Introduceți CNP-ul clientului: ")
        return id, nume, cnp

    def afiseaza_carti(self, lista_carti):
        for carte in lista_carti:
            print(carte)

    def afiseaza_clienti(self, lista_clienti):
        for client in lista_clienti:
            print(client)

    def adauga_carte_ui(self):
        id, titlu, descriere, autor = self.citeste_info_carte()
        try:
            self.__book_service.adauga_carte(id, titlu, descriere, autor)
            print(Fore.GREEN + "Adăugare realizată cu succes." + Style.RESET_ALL)
        except ValueError as ve:
            print(Fore.RED + str(ve) + Style.RESET_ALL)

    def adauga_client_ui(self):
        id, nume, cnp = self.citeste_info_client()
        try:
            self.__client_service.adauga_client_nou(id, nume, cnp)
            print(Fore.GREEN + "Clientul a fost adăugat cu succes." + Style.RESET_ALL)
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
            self.__book_service.actualizeaza_carte(id, titlu_nou, descriere_noua, autor_nou)
            print(Fore.GREEN + "Actualizare realizată cu succes." + Style.RESET_ALL)
        except ValueError as ve:
            print(Fore.RED + str(ve) + Style.RESET_ALL)

    def actualizeaza_client_ui(self):
        id = int(input("Introduceți ID-ul clientului de actualizat: "))
        nume_nou = input("Introduceți noul nume: ")
        cnp_nou = input("Introduceți noul CNP: ")

        nume_nou = nume_nou if nume_nou else None
        cnp_nou = cnp_nou if cnp_nou else None

        try:
            self.__client_service.actualizeaza_date_client(id, nume_nou, cnp_nou)
            print(Fore.GREEN + "Clientul a fost actualizat cu succes." + Style.RESET_ALL)
        except ValueError as ve:
            print(Fore.RED + str(ve) + Style.RESET_ALL)

    def sterge_carte_ui(self):
        id = int(input("Introduceți ID-ul cărții de șters: "))
        try:
            self.__book_service.delete_carte(id)
            print(Fore.GREEN + "Ștergerea cărții a fost realizată cu succes." + Style.RESET_ALL)
        except ValueError as ve:
            print(Fore.RED + str(ve) + Style.RESET_ALL)

    def sterge_client_ui(self):
        id = int(input("Introduceți ID-ul clientului de șters: "))
        try:
            self.__client_service.sterge_client_dupa_id(id)
            print(Fore.GREEN + "Ștergerea clientului a fost realizată cu succes." + Style.RESET_ALL)
        except ValueError as ve:
            print(Fore.RED + str(ve) + Style.RESET_ALL)

    def cauta_client_dupa_id_ui(self):
        id = int(input("Introduceți ID-ul clientului de căutat: "))
        client_gasit = self.__client_service.cauta_client_dupa_id(id)
        if client_gasit:
            print("Clientul găsit este:", client_gasit)
        else:
            print(Fore.RED + "Nu există client cu acest ID." + Style.RESET_ALL)

    def cauta_client_dupa_cnp_ui(self):
        cnp = input("Introduceți CNP-ul clientului de căutat: ")
        client_gasit = self.__client_service.cauta_client_pe_baza_cnp(cnp)
        if client_gasit:
            print("Clientul găsit este:", client_gasit)
        else:
            print(Fore.RED + "Nu există client cu acest CNP." + Style.RESET_ALL)

    def add_default_ui(self):
        self.__book_service.add_default()
        print(Fore.GREEN + "Cărțile implicite au fost adăugate cu succes." + Style.RESET_ALL)

        self.__client_service.populeaza_clienti_impliciti()
        print(Fore.GREEN + "Clienții implicați au fost adăugați cu succes." + Style.RESET_ALL)

    def filtreaza_dupa_autor_ui(self):
        autor = input("Introduceți autorul cărților de afișat: ")
        lista_filtrata = self.__book_service.filtreaza_dupa_autor(autor)
        
        if lista_filtrata:
            print(f"Toate cărțile scrise de {autor} sunt:")
            self.afiseaza_carti(lista_filtrata)
        else:
            print(Fore.RED + f"Nu există cărți scrise de {autor}." + Style.RESET_ALL)

    def cauta_carte_dupa_titlu_ui(self):
        titlu = input("Introduceți titlul cărții de căutat: ")
        carte_gasita = self.__book_service.cauta_carte_dupa_titlu(titlu)
        
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
                case '6':
                    self.adauga_client_ui()
                case '7':
                    self.actualizeaza_client_ui()
                case '8':
                    self.sterge_client_ui()
                case 'A2':
                    self.afiseaza_clienti(self.__client_service.obtine_toti_clientii())
                case '9':
                    self.cauta_client_dupa_id_ui()
                case '10':
                    self.cauta_client_dupa_cnp_ui() 
                case 'R1':
                    self.genereaza_x_carti_random_ui()
                case 'B':
                    self.inchiriaza_carte_ui()        
                case 'C':
                    self.add_default_ui()
                case 'A1':
                    self.afiseaza_carti(self.__book_service.get_all_books())
                case 'E':
                    is_running = False
