from citiri import *
from list_manager import *
from pachet_calatorie import *
def afiseaza_meniul_principal():
    print("1. Adăugare")
    print("2. Ștergere")
    print("3. Căutare")
    print("4. Rapoarte")
    print("5. Filtrare")
    print("6. Undo")
    print("E. Ieșire")

def afiseaza_submeniul_adaugare():
    print("1. Adaugă pachet de călătorie")
    print("2. Modifică pachet de călătorie")
    print("0. Înapoi")

def afiseaza_submeniul_stergere():
    print("1. Ștergerea tuturor pachetelor pentru o destinație dată")
    print("2. Ștergerea tuturor pachetelor care au o durată mai scurtă decât un număr de zile dat")
    print("3. Ștergerea tuturor pachetelor care au prețul mai mare decât o sumă dată")
    print("0. Înapoi")

def afiseaza_submeniul_cautare():
    print("1. Tipărirea pachetelor într-un interval dat")
    print("2. Tipărirea pachetelor cu o destinație dată și preț mai mic decât o sumă dată")
    print("3. Tipărirea pachetelor cu o anumită dată de sfârșit")
    print("0. Înapoi")

def afiseaza_submeniul_rapoarte():
    print("1. Tipărirea numărului de oferte pentru o destinație dată")
    print("2. Tipărirea pachetelor disponibile într-o perioadă, ordonate crescător după preț")
    print("3. Tipărirea mediei de preț pentru o destinație dată")
    print("0. Înapoi")

def afiseaza_submeniul_filtrare():
    print("1. Eliminarea ofertelor cu preț mai mare și destinație diferită")
    print("2. Eliminarea ofertelor care includ zile dintr-o anumită lună")
    print("0. Înapoi")



def citeste_info_pachet():
    k = False 
    while not k:
        data_de_inceput = input("Introduceti data de inceput a calatoriei: ") 
        data_de_inceput = data_de_inceput.strip()
        k = verificare_data(data_de_inceput)
        if(k == False):
            print("Data a fost introdusa gresit")
    k = False 
    while not k:
        data_de_final = input("Introduceti data de sfarsit a calatoriei: ") 
        data_de_final = data_de_final.strip()
        k = verificare_data(data_de_final)
        if(k == False):
            print("Data a fost introdusa gresit")   
        if(data_de_final < data_de_inceput and k == True):
            k = False
            print("Data de final trebuie sa fie dupa data de inceput") 
    destinatia = input("Introduceti numele destinatiei: ").capitalize()
    pretul = int(input("Introduceti pretul pachetului: ")) 
    return data_de_inceput, data_de_final, destinatia, pretul  

def afisare_liste(liste):
    print('\n')
    print("Pachetele de călătorii eligibile sunt:")
    for pachet in liste:
        data_inceput = pachet['data_de_inceput'].strftime('%d/%m/%Y')  
        data_final = pachet['data_de_final'].strftime('%d/%m/%Y')      
        destinatia = pachet['destinatia']                
        pretul = pachet['pretul']
        print(f" - Destinația: {destinatia}")
        print(f"   Data de început: {data_inceput}")
        print(f"   Data de final: {data_final}")
        print(f"   Preț: {pretul} EURO\n") 


def run():
    lista_calatorii = []
    is_running = True 
    while is_running:
        afiseaza_meniul_principal()
        optiune_principala = input(">>>> ").upper().strip()
        match optiune_principala:
            case '1':
                afiseaza_submeniul_adaugare()
                optiune_adaugare = input("Alegeți o opțiune pentru adăugare: ").strip()
                match optiune_adaugare:
                    case '1':
                        data_de_inceput, data_de_final, destinatia, pretul = citeste_info_pachet()
                        pachet_de_calatorie = creare_pachet(data_de_inceput, data_de_final, destinatia, pretul)
                        adaugare_la_lista(lista_calatorii, pachet_de_calatorie)
                    case '2':
                        print("Al catelea pachet ati dori sa-l modificati? ")
                        afisare_liste(lista_calatorii)   
                        numar = citire_numar_pachet()
                        numar = numar - 1
                        data_de_inceput, data_de_final, destinatia, pretul = citeste_info_pachet()
                        pachet_de_calatorie = creare_pachet(data_de_inceput, data_de_final, destinatia, pretul)
                        del lista_calatorii[numar]
                        lista_calatorii.insert(numar, pachet_de_calatorie)



            case '2':
                afiseaza_submeniul_stergere()
                optiune_stergere = input("Alegeți o opțiune pentru ștergere: ").strip()
                match optiune_stergere:
                    case '1':
                        pass
                    case '2':
                        pass
                    case '3':
                        pass
            case '3':
                afiseaza_submeniul_cautare()
                optiune_cautare = input("Alegeți o opțiune pentru căutare: ").strip()
                match optiune_cautare:
                    case '1':
                        data_de_incepere, data_de_sfarsit = citeste_preferinte_interval_calatorie()   
                        lista_calatorii_eligibile = []
                        lista_calatorii_eligibile = calatorii_cautate_date(lista_calatorii, lista_calatorii_eligibile, data_de_incepere, data_de_sfarsit)
                        afisare_liste(lista_calatorii_eligibile)
                    case '2':
                        lista_calatorii_eligibile = []
                        destinatie_preferata, buget = citeste_preferinte_destinatie_pret_calatorie()
                        lista_calatorii_eligibile = calatorii_cautate_destinatie_pret(lista_calatorii, lista_calatorii_eligibile, destinatie_preferata, buget)
                        afisare_liste(lista_calatorii_eligibile)
                    case '3':
                        lista_calatorii_eligibile = []
                        data_de_final_preferata = citeste_info_data_de_final_preferata() 
                        lista_calatorii_eligibile = calatorii_cautate_data_final(lista_calatorii, lista_calatorii_eligibile, data_de_final_preferata)
                        afisare_liste(lista_calatorii_eligibile)
            case '4':
                afiseaza_submeniul_rapoarte()
                optiune_rapoarte = input("Alegeți o opțiune pentru rapoarte: ").strip()
                match optiune_rapoarte:
                    case '1':
                        pass
                     
                    case '2':
                        pass
                    case '3':
                        pass
            case '5':
                lista_filtrare_pret_maxim = []
                afiseaza_submeniul_filtrare()
                optiune_filtrare = input("Alegeți o opțiune pentru filtrare: ").strip()
                match optiune_filtrare:
                    case '1':
                        lista_filtrare_pret_maxim = []
                        pretul_maxim = int(input('Introduceti bugetul maxim: '))
                        destinatia_nedorita = input("Introduceti detinatia unde nu doriti sa mergeti: ")
                        lista_filtrare_pret_maxim =  eliminare_oferte_pret(lista_calatorii, pretul_maxim, destinatia_nedorita)
                        afisare_liste(lista_filtrare_pret_maxim)
                    case '2':
                        pass
            case '6':
                pass
            case 'E':
                print("Exiting....")
                is_running = False   