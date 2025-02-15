import random
from colorama import Fore, Style

class Console:
    def __init__(self, book_service, client_service, rental_service):
        self.__book_service = book_service
        self.__client_service = client_service
        self.__rental_service = rental_service

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
        print("B1. Inchiriere carte")
        print("B2. Returnare carte")
        print("S. Sortare mixta carti")
        print("R1. Adaugă carti random")
        print("R2. Cele mai închiriate cărți")
        print("R3. Clienți ordonați după numărul de cărți închiriate")
        print("R4. Primii 20% cei mai activi clienți")
        print("R5. Clientul cu cele mai multe inchirieri")
        print("C. Adaugă cărți și clienți implicite")
        print("A1. Afișează lista cărților")
        print("A2. Afiseaza lista de clienti")
        print("E. Ieșire din aplicație")

    def clientul_cu_cele_mai_multe_inchirieri_ui(self):
        
        clienti = self.__rental_service.clienti_ord_desch_numar_carti()
        print("Clientul cu cele mai multe carti inchiriate este")
        for client, nr_inchirieri in clienti:
            print(f"{client} - {nr_inchirieri} cărți")
            return
    def cele_mai_inchiriate_carti_ui(self):
        statistici = self.__rental_service.cele_mai_inchiriate_carti()
        print("Cele mai închiriate cărți sunt:")
        for carte, nr_inchirieri in statistici:
            print(f"{carte} - {nr_inchirieri} închirieri")

    def clienti_ordonati_ui(self):
        clienti = self.__rental_service.clienti_ord_desch_numar_carti()
        print("Clienți ordonați după numărul de cărți închiriate:")
        for client, nr_inchirieri in clienti:
            print(f"{client} - {nr_inchirieri} cărți")

    def primii_20_proc_ui(self):
        top_clienti = self.__rental_service.primii_20_proc_activi()
        print("Primii 20% cei mai activi clienți:")
        for client, nr_inchirieri in top_clienti:
            print(f"{client} - {nr_inchirieri} cărți")


    def genereaza_x_carti_random_ui(self):
        
        x = int(input("Introduceți numărul de cărți random de generat: "))
        self.__book_service.genereaza_carti_random(x)
        print(Fore.GREEN + f"{x} cărți random au fost generate și adăugate cu succes!" + Style.RESET_ALL)

    def returneaza_carte_ui(self):
        titlu = input("Introduceți titlul cărții de returnat: ").strip()
        autor = input("Introduceți autorul cărții: ").strip()

        carte = self.__book_service.cauta_carte_dupa_titlu_si_autor(titlu, autor)
        if not carte:
            print(Fore.RED + "Cartea specificată nu există în sistem." + Style.RESET_ALL)
            return

        id_client = input("Introduceți ID-ul clientului (lăsați gol dacă nu îl știți): ").strip()
        client = None

        if id_client:
            try:
                client = self.__client_service.cauta_client_dupa_id(int(id_client))
            except ValueError:
                print(Fore.RED + "ID-ul introdus nu este valid." + Style.RESET_ALL)
                return
        else:
            cnp = input("Introduceți CNP-ul clientului: ").strip()
            client = self.__client_service.cauta_client_pe_baza_cnp(cnp)

        if not client:
            print(Fore.RED + "Clientul specificat nu există." + Style.RESET_ALL)
            return

        inchiriere = self.__rental_service.cauta_inchiriere_dupa_carte_si_client(carte, client)
        if not inchiriere:
            print(Fore.RED + "Clientul nu a închiriat această carte." + Style.RESET_ALL)
            return

        try:
            nr_bucati_nou = carte.get_nr_bucati() + 1
            carte.set_nr_bucati(nr_bucati_nou)
            carte.set_rental(False) 


            print(Fore.GREEN + "Cartea a fost returnată cu succes." + Style.RESET_ALL)
        except ValueError as ve:
            print(Fore.RED + str(ve) + Style.RESET_ALL)




    def citeste_info_carte(self) -> tuple:
        id = int(input("Introduceți ID-ul cărții: "))
        titlu = input("Introduceți titlul cărții: ")
        descriere = input("Introduceți descrierea cărții: ")
        autor = input("Introduceți autorul cărții: ")
        nr_bucati = int(input("Introduceti numarul de bucati valabile: "))
        return id, titlu, descriere, autor, nr_bucati

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
        id, titlu, descriere, autor, nr_bucati = self.citeste_info_carte()
        try:
            self.__book_service.adauga_carte(id, titlu, descriere, autor, nr_bucati)
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
        nr_bucati_nou = int(input("Introduceți noul număr de bucati: "))

        titlu_nou = titlu_nou if titlu_nou else None
        descriere_noua = descriere_noua if descriere_noua else None
        autor_nou = autor_nou if autor_nou else None

        try:
            self.__book_service.actualizeaza_carte(id, titlu_nou, descriere_noua, autor_nou, nr_bucati_nou)
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
        client = self.__client_service.cauta_client_dupa_id(id)
        try:
            self.__rental_service.sterge_inchirieri_dupa_client(client)
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


    def inchiriaza_carte_ui(self):
        titlu = input("Introduceți titlul cărții de închiriat: ").strip()
        autor = input("Introduceți autorul cărții: ").strip()
        
        carte = self.__book_service.cauta_carte_dupa_titlu_si_autor(titlu, autor)
        if not carte:
            print(Fore.RED + "Cartea specificată nu există în sistem." + Style.RESET_ALL)
            return
        
        id_client = input("Introduceți ID-ul clientului (lăsați gol dacă nu îl știți): ").strip()
        client = None

        if id_client:
            try:
                client = self.__client_service.cauta_client_dupa_id(int(id_client))
            except ValueError:
                print(Fore.RED + "ID-ul introdus nu este valid." + Style.RESET_ALL)
                return
        else:
            cnp = input("Introduceți CNP-ul clientului: ").strip()
            client = self.__client_service.cauta_client_pe_baza_cnp(cnp)

        if not client:
            print(Fore.RED + "Clientul specificat nu există." + Style.RESET_ALL)
            return
        


        inchiriat = self.__book_service.verificare_inchiriere(carte)
        if inchiriat:
            print(Fore.RED + "Cartea nu mai este disponibila." + Style.RESET_ALL)
        else:
            try:
                nr_bucati_nou = carte.get_nr_bucati() - 1
                carte.set_nr_bucati(nr_bucati_nou)
                if(nr_bucati_nou == 0):
                    carte.set_rental(True)
                self.__rental_service.adauga_inchiriere(carte, client) 
                print(Fore.GREEN + "Cartea a fost închiriată cu succes." + Style.RESET_ALL)
            except ValueError as ve:
                print(Fore.RED + str(ve) + Style.RESET_ALL)
       

    def __sortare_mixta_ui(self):
        lista_sortata = self.__book_service.sortare_mixta()
        for carte in lista_sortata:
            print(carte)
    
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
                case 'R2':
                    self.cele_mai_inchiriate_carti_ui()
                case 'R3':
                    self.clienti_ordonati_ui()
                case 'R4':
                    self.primii_20_proc_ui()  
                case 'R5':
                    self.clientul_cu_cele_mai_multe_inchirieri_ui()      
                case 'B1':
                    self.inchiriaza_carte_ui()    
                case 'B2':
                    self.returneaza_carte_ui()  
                case 'S':
                    self.__sortare_mixta_ui()          
                case 'C':
                    self.add_default_ui()
                case 'A1':
                    self.afiseaza_carti(self.__book_service.get_all_books())
                case 'E':
                    is_running = False
