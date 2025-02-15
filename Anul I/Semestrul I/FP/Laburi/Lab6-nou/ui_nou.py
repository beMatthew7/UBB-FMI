from verificare import verificare_data, verificare_luna
from datetime import datetime
from pachet import get_data_de_final, get_data_de_inceput,get_destinatia, get_pretul
from prelucrare_lista import adaugare_la_lista, calatorii_cautate_data_final, calatorii_cautate_date, calatorii_cautate_destinatie_pret, eliminare_oferte_pret, stergere_pachet_destinatie, stergere_pachet_durata, stergere_pachet_pret, eliminare_oferte_luna, rapoarte_numar_destinatie, rapoarte_pret_mediu_destinatie, rapoarte_perioada_crescator_pret, creeaza_calatorii_manager, get_lista_calatorii, undo, set_lista_curenta, adauga_la_lista_undo, copy_list_of_lists
from pachet import creare_pachet, set_data_de_final, set_data_de_inceput, set_destinatia, set_pretul
from colorama import Fore, Style

from colorama import Fore, Style




def undo_ui(calatorii_manager):
    try:
        undo(calatorii_manager)
    except ValueError as e:
        # coloram textul de eroare in rosu
        # necesita modulul colorama
        # https://pypi.org/project/colorama/
        print(Fore.RED + str(e) + Style.RESET_ALL)




def citeste_info_pachet():
    while True:
        try:
            data_de_inceput = input("Data de început (dd/mm/yyyy): ")
            if not verificare_data(data_de_inceput):
                raise ValueError("Data de început invalidă! Reîncercați.")
            break  
        except ValueError as e:
            print(Fore.RED + str(e) + Style.RESET_ALL)

    while True:
        try:
            data_de_final = input("Data de final (dd/mm/yyyy): ")
            if not verificare_data(data_de_final):
                raise ValueError("Data de final invalidă! Reîncercați.")
            break  
        except ValueError as e:
            print(Fore.RED + str(e) + Style.RESET_ALL)

    destinatia = input("Destinație: ").capitalize()
    
    while True:
        try:
            pretul = int(input("Preț: "))
            break  
        except ValueError as e:
            print(Fore.RED + "Preț invalid! Introduceți un număr întreg." + Style.RESET_ALL)

    return data_de_inceput, data_de_final, destinatia, pretul


    
def afisare_liste(liste):
    print('\n')
    print("Pachetele de călătorii eligibile sunt:")
    for pachet in liste:
        data_inceput = get_data_de_inceput(pachet).strftime('%d/%m/%Y')  
        data_final = get_data_de_final(pachet).strftime('%d/%m/%Y')      
        destinatia = get_destinatia(pachet)                
        pretul = get_pretul(pachet)
        print(f" - Destinația: {destinatia}")
        print(f"   Data de început: {data_inceput}")
        print(f"   Data de final: {data_final}")
        print(f"   Preț: {pretul} EURO\n") 

def run_interactiv(calatorii_manager):
    while True:
        print("Meniu principal")
        print("1. Adaugare pachet de calatorie")
        print("2. Filtrare pachete de calatorie care au loc intr-o luna dorita")
        print("3. Ștergerea tuturor pachetelor care au prețul mai mare decât o sumă dată")
        print("4. Afisare pachete de calatorie")
        print("5. Undo")
        print("E. Exit")

        optiune = input("Alegeti o optiune: ").strip()  

        match optiune:
            case '1':
                data_de_inceput, data_de_final, destinatia, pretul = citeste_info_pachet()
                pachet_de_calatorie = creare_pachet(data_de_inceput, data_de_final, destinatia, pretul)
                adaugare_la_lista(calatorii_manager, pachet_de_calatorie)

            case '2':
                while True:
                    try:
                        luna_dorita = int(input('Introduceti luna dorita sub forma de numar (1-12): '))
                        
                        if not verificare_luna(luna_dorita):
                            raise ValueError("Luna introdusă este invalidă! Trebuie să fie între 1 și 12.")
                        
                        break
                        
                    except ValueError as e:
                        print(Fore.RED + str(e) + Style.RESET_ALL)

                lista_filtrare_luna_dorita = []
                lista_filtrare_luna_dorita =  eliminare_oferte_luna(get_lista_calatorii(calatorii_manager), luna_dorita)
                afisare_liste(lista_filtrare_luna_dorita)

            case '3':
                lista_noua = []
                try:
                    pret_dat = int(input("Preț: "))
                    break  
                except ValueError as e:
                    print(Fore.RED + "Preț invalid! Introduceți un număr întreg." + Style.RESET_ALL)
                adauga_la_lista_undo(calatorii_manager, copy_list_of_lists(calatorii_manager['lista_curenta']))
                lista_calatorii = stergere_pachet_pret(lista_noua, get_lista_calatorii(calatorii_manager), pret_dat)
                set_lista_curenta(calatorii_manager, lista_calatorii)
                afisare_liste(get_lista_calatorii(calatorii_manager))

            case '4':
                afisare_liste(get_lista_calatorii(calatorii_manager))      

            case '5':
                undo_ui(calatorii_manager)  

            case 'E':
                print("Exiting....")   
                break   


def run_batch(calatorii_manager, comenzi):
    for comanda in comenzi.split(";"):
        comanda = comanda.strip()
        match comanda.split():
            case ["Add", data_inceput, data_final, destinatie, pret]:
                try:
                    if not verificare_data(data_inceput):
                        raise ValueError("Data de început invalidă! Formatul trebuie să fie dd/mm/yyyy.")
                    if not verificare_data(data_final):
                        raise ValueError("Data de final invalidă! Formatul trebuie să fie dd/mm/yyyy.")
                    pret = int(pret)
                    if pret <= 0:
                        raise ValueError("Prețul trebuie să fie un număr pozitiv.")
                    pachet = creare_pachet(data_inceput, data_final, destinatie.capitalize(), pret)
                    adaugare_la_lista(calatorii_manager, pachet)
                    print("Pachet adăugat cu succes.")
                except ValueError as e:
                    print(Fore.RED + f"Eroare la comanda '{comanda}': {str(e)}" + Style.RESET_ALL)
                    print(Fore.RED + "Formatul corect trebuie să fie 'Add data_inceput data_final destinatie pret'." + Style.RESET_ALL)

            case ["Filter", luna_dorita]:
                try:
                    luna_dorita = int(luna_dorita)  

                    if not verificare_luna(luna_dorita):
                        raise ValueError("Luna introdusă este invalidă! Trebuie să fie între 1 și 12.")

                    lista_filtrare_luna_dorita = eliminare_oferte_luna(get_lista_calatorii(calatorii_manager), luna_dorita)
                    afisare_liste(lista_filtrare_luna_dorita)
                
                except ValueError as e:
                    print(Fore.RED + str(e) + Style.RESET_ALL)

                except Exception:
                    print(Fore.RED + f"Eroare la comanda '{comanda}'. Formatul trebuie să fie 'Filter luna dorita'." + Style.RESET_ALL)

            case ["Delete", pret_dat]:
                try:
                    pret_dat = int(pret_dat)
                    adauga_la_lista_undo(calatorii_manager, copy_list_of_lists(calatorii_manager['lista_curenta']))
                    lista_noua = []
                    lista_calatorii = stergere_pachet_pret(lista_noua, get_lista_calatorii(calatorii_manager), pret_dat)
                    set_lista_curenta(calatorii_manager, lista_calatorii)
                    afisare_liste(get_lista_calatorii(calatorii_manager))


                except Exception as e:
                    print(Fore.RED + f"Eroare la comanda '{comanda}': {str(e)}" + Style.RESET_ALL)
                    print(Fore.RED + "Formatul corect trebuie să fie 'Delete pret'." + Style.RESET_ALL)


            case ["Undo"]:
                try:
                    undo_ui(calatorii_manager)  
                    afisare_liste(get_lista_calatorii(calatorii_manager))  #

                except Exception as e:
                    print(Fore.RED + f"Eroare la comanda '{comanda}': {str(e)}" + Style.RESET_ALL)
            case ["Print"]:
                afisare_liste(get_lista_calatorii(calatorii_manager))



                


  

def run():
    calatorii_manager = creeaza_calatorii_manager()
    print("Selectati modul de rulare:")
    print("1. Modul interactiv")
    print("2. Modul batch")

    optiune_mod = input("Introduceti optiunea dorita: ").strip()

    match optiune_mod:
        case '1':
            run_interactiv(calatorii_manager)
        case '2':
            comenzi = input("Introduceti comenzile dorite separate prin ';' ")
            run_batch(calatorii_manager, comenzi)   

