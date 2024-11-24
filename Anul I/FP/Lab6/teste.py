from prelucrare_lista import calatorii_cautate_data_final,calatorii_cautate_date,calatorii_cautate_destinatie_pret,adaugare_la_lista, eliminare_oferte_pret, stergere_pachet_destinatie, stergere_pachet_durata, stergere_pachet_pret, eliminare_oferte_luna, rapoarte_numar_destinatie, rapoarte_perioada_crescator_pret, rapoarte_pret_mediu_destinatie, creeaza_calatorii_manager, get_lista_calatorii
from pachet import creare_pachet, get_data_de_final,get_data_de_inceput,get_destinatia,get_pretul
from datetime import datetime
from verificare import verificare_data
from ui import citeste_info_pachet, citeste_info_data_de_final_preferata, citeste_preferinte_destinatie_pret_calatorie, citeste_preferinte_interval_calatorie,citire_numar_pachet


def test_creare_pachet():
    pachet_de_calatorie1 = creare_pachet('13/09/2024', '20/09/2024', 'Praga', 500)
    assert get_data_de_inceput(pachet_de_calatorie1) == datetime(2024, 9, 13)
    assert get_data_de_final(pachet_de_calatorie1) == datetime(2024, 9, 20)
    assert get_destinatia(pachet_de_calatorie1) == "Praga"
    assert get_pretul(pachet_de_calatorie1) == 500

def test_adaugare_la_lista():
    calatorii_manager = creeaza_calatorii_manager()
    assert len(get_lista_calatorii(calatorii_manager)) == 0
    pachet1 = creare_pachet('22/09/2024', '29/09/2024', 'Barcelona', 450)
    adaugare_la_lista(calatorii_manager, pachet1)
    assert len(get_lista_calatorii(calatorii_manager)) == 1
    assert get_destinatia(get_lista_calatorii(calatorii_manager)[0]) == "Barcelona"
    
    pachet2 = creare_pachet('10/10/2024', '12/10/2024', 'Monaco', 300)
    adaugare_la_lista(calatorii_manager, pachet2)
    assert len(get_lista_calatorii(calatorii_manager)) == 2
    assert get_destinatia(get_lista_calatorii(calatorii_manager)[1]) == "Monaco"

def test_calatorii_cautate_date():
    calatorii_manager = creeaza_calatorii_manager()
    test_list_eligibile = []
    pachet1 = creare_pachet('22/09/2024', '29/09/2024', 'Barcelona', 450)
    pachet2 = creare_pachet('10/10/2024', '12/10/2024', 'Monaco', 300)
    adaugare_la_lista(calatorii_manager, pachet1)
    adaugare_la_lista(calatorii_manager, pachet2)
    
    rezultat1 = calatorii_cautate_date(get_lista_calatorii(calatorii_manager), test_list_eligibile, datetime(2024, 11, 1), datetime(2024, 11, 15))
    assert len(rezultat1) == 0
    
    rezultat2 = calatorii_cautate_date(get_lista_calatorii(calatorii_manager), test_list_eligibile, datetime(2024, 9, 20), datetime(2024, 9, 30))
    assert len(rezultat2) == 1
    assert get_destinatia(rezultat2[0]) == "Barcelona"
    assert get_pretul(rezultat2[0]) == 450

def test_calatorii_cautate_destinatie_pret():
    calatorii_manager = creeaza_calatorii_manager()
    test_list_eligibile = []
    pachet1 = creare_pachet('22/09/2024', '29/09/2024', 'Barcelona', 450)
    pachet2 = creare_pachet('10/10/2024', '12/10/2024', 'Monaco', 300)
    adaugare_la_lista(calatorii_manager, pachet1)
    adaugare_la_lista(calatorii_manager, pachet2)

    rezultat1 = calatorii_cautate_destinatie_pret(get_lista_calatorii(calatorii_manager), test_list_eligibile, 'Barcelona', 500)
    assert len(rezultat1) == 1
    assert get_destinatia(rezultat1[0]) == "Barcelona"
    assert get_pretul(rezultat1[0]) == 450

def test_calatorii_cautate_data_final():
    calatorii_manager = creeaza_calatorii_manager()
    test_list_eligibile = []
    pachet1 = creare_pachet('22/09/2024', '29/09/2024', 'Barcelona', 450)
    pachet2 = creare_pachet('10/10/2024', '12/10/2024', 'Monaco', 300)
    pachet3 = creare_pachet('05/11/2024', '10/11/2024', 'Paris', 600)
    adaugare_la_lista(calatorii_manager, pachet1)
    adaugare_la_lista(calatorii_manager, pachet2)
    adaugare_la_lista(calatorii_manager, pachet3)

    rezultat = calatorii_cautate_data_final(get_lista_calatorii(calatorii_manager), test_list_eligibile, datetime(2024, 10, 12))
    assert len(rezultat) == 1
    assert get_destinatia(rezultat[0]) == "Monaco"
    assert get_pretul(rezultat[0]) == 300

def test_stergere_pachet_destinatie():
    calatorii_manager = creeaza_calatorii_manager()
    pachet1 = creare_pachet('22/09/2024', '29/09/2024', 'Barcelona', 450)
    pachet2 = creare_pachet('10/10/2024', '12/10/2024', 'Monaco', 300)
    pachet3 = creare_pachet('05/11/2024', '10/11/2024', 'Barcelona', 600)
    adaugare_la_lista(calatorii_manager, pachet1)
    adaugare_la_lista(calatorii_manager, pachet2)
    adaugare_la_lista(calatorii_manager, pachet3)

    assert len(get_lista_calatorii(calatorii_manager)) == 3
    
    lista_noua = stergere_pachet_destinatie([], get_lista_calatorii(calatorii_manager), 'Barcelona')
    
    assert len(lista_noua) == 1
    assert get_destinatia(lista_noua[0]) == "Monaco"

def test_stergere_pachet_durata():
    calatorii_manager = creeaza_calatorii_manager()
    pachet1 = creare_pachet('01/09/2024', '10/09/2024', 'Barcelona', 450)
    pachet2 = creare_pachet('05/10/2024', '12/10/2024', 'Monaco', 300)
    pachet3 = creare_pachet('15/10/2024', '20/10/2024', 'Paris', 600)
    adaugare_la_lista(calatorii_manager, pachet1)
    adaugare_la_lista(calatorii_manager, pachet2)
    adaugare_la_lista(calatorii_manager, pachet3)

    assert len(get_lista_calatorii(calatorii_manager)) == 3
    
    lista_noua = stergere_pachet_durata([], get_lista_calatorii(calatorii_manager), 6)
    
    assert len(lista_noua) == 2
    assert get_destinatia(lista_noua[0]) == "Barcelona"
    assert get_destinatia(lista_noua[1]) == "Monaco"

def test_stergere_pachet_pret():
    calatorii_manager = creeaza_calatorii_manager()
    pachet1 = creare_pachet('22/09/2024', '29/09/2024', 'Barcelona', 450)
    pachet2 = creare_pachet('10/10/2024', '12/10/2024', 'Monaco', 300)
    pachet3 = creare_pachet('05/11/2024', '10/11/2024', 'Paris', 600)
    adaugare_la_lista(calatorii_manager, pachet1)
    adaugare_la_lista(calatorii_manager, pachet2)
    adaugare_la_lista(calatorii_manager, pachet3)

    assert len(get_lista_calatorii(calatorii_manager)) == 3
    
    lista_noua = stergere_pachet_pret([], get_lista_calatorii(calatorii_manager), 350)
    
    assert len(lista_noua) == 2
    assert get_destinatia(lista_noua[0]) == "Barcelona"
    assert get_destinatia(lista_noua[1]) == "Paris"


def test_eliminare_oferte_pret():
    calatorii_manager = creeaza_calatorii_manager()
    pachet1 = creare_pachet('22/09/2024', '29/09/2024', 'Barcelona', 450)
    pachet2 = creare_pachet('10/10/2024', '12/10/2024', 'Monaco', 300)
    pachet3 = creare_pachet('05/11/2024', '10/11/2024', 'Paris', 600)
    
    adaugare_la_lista(calatorii_manager, pachet1)
    adaugare_la_lista(calatorii_manager, pachet2)
    adaugare_la_lista(calatorii_manager, pachet3)

    test_list_eligibile = eliminare_oferte_pret(get_lista_calatorii(calatorii_manager), 400, "Berlin")
    assert len(test_list_eligibile) == 1


def test_eliminare_oferte_luna():
    calatorii_manager = creeaza_calatorii_manager()
    pachet1 = creare_pachet('01/09/2024', '10/09/2024', 'Barcelona', 450)
    pachet2 = creare_pachet('05/10/2024', '12/10/2024', 'Monaco', 300)
    pachet3 = creare_pachet('15/10/2024', '20/10/2024', 'Paris', 600)
    pachet4 = creare_pachet('01/10/2024', '05/10/2024', 'Roma', 400)
    adaugare_la_lista(calatorii_manager, pachet1)
    adaugare_la_lista(calatorii_manager, pachet2)
    adaugare_la_lista(calatorii_manager, pachet3)
    adaugare_la_lista(calatorii_manager, pachet4)

    assert len(get_lista_calatorii(calatorii_manager)) == 4
    
    lista_filtrata = eliminare_oferte_luna(get_lista_calatorii(calatorii_manager), 10)
    
    assert len(lista_filtrata) == 3


def test_rapoarte_numar_destinatie():
    calatorii_manager = creeaza_calatorii_manager()
    pachet1 = creare_pachet('22/09/2024', '29/09/2024', 'Barcelona', 450)
    pachet2 = creare_pachet('10/10/2024', '12/10/2024', 'Barcelona', 300)
    pachet3 = creare_pachet('05/11/2024', '10/11/2024', 'Paris', 600)
    adaugare_la_lista(calatorii_manager, pachet1)
    adaugare_la_lista(calatorii_manager, pachet2)
    adaugare_la_lista(calatorii_manager, pachet3)

    assert rapoarte_numar_destinatie(get_lista_calatorii(calatorii_manager), 'Barcelona') == 2
    assert rapoarte_numar_destinatie(get_lista_calatorii(calatorii_manager), 'Paris') == 1
    assert rapoarte_numar_destinatie(get_lista_calatorii(calatorii_manager), 'Roma') == 0

def test_rapoarte_perioada_crescator_pret():
    calatorii_manager = creeaza_calatorii_manager()
    pachet1 = creare_pachet('01/09/2024', '10/09/2024', 'Barcelona', 450)
    pachet2 = creare_pachet('05/10/2024', '12/10/2024', 'Monaco', 300)
    pachet3 = creare_pachet('15/10/2024', '20/10/2024', 'Paris', 600)
    
    adaugare_la_lista(calatorii_manager, pachet1)
    adaugare_la_lista(calatorii_manager, pachet2)
    adaugare_la_lista(calatorii_manager, pachet3)

    rezultate = rapoarte_perioada_crescator_pret(get_lista_calatorii(calatorii_manager), datetime(2024, 9, 1), datetime(2024, 10, 31))
    assert len(rezultate) == 3

def test_rapoarte_pret_mediu_destinatie():
    calatorii_manager = creeaza_calatorii_manager()
    pachet1 = creare_pachet('01/09/2024', '10/09/2024', 'Barcelona', 450)
    pachet2 = creare_pachet('05/10/2024', '12/10/2024', 'Barcelona', 300)
    pachet3 = creare_pachet('15/10/2024', '20/10/2024', 'Paris', 600)
    
    adaugare_la_lista(calatorii_manager, pachet1)
    adaugare_la_lista(calatorii_manager, pachet2)
    adaugare_la_lista(calatorii_manager, pachet3)

    mediu = rapoarte_pret_mediu_destinatie(get_lista_calatorii(calatorii_manager), 'Barcelona')
    assert mediu == 375



def test_verificare_data():
    assert verificare_data("29/02/2024") == True
    assert verificare_data("28/02/2023") == True
    assert verificare_data("31/12/2023") == True

    assert verificare_data("32/01/2024") == False
    assert verificare_data("29/02/2023") == False
    assert verificare_data("15/13/2024") == False 
    assert verificare_data("12/12/20") == False
    assert verificare_data("12-12-2024") == False


def ruleaza_teste():
    test_creare_pachet()
    test_adaugare_la_lista()
    test_calatorii_cautate_date()
    test_calatorii_cautate_destinatie_pret()
    test_calatorii_cautate_data_final()
    test_stergere_pachet_destinatie()
    test_stergere_pachet_durata()
    test_stergere_pachet_pret()
    test_rapoarte_numar_destinatie()
    test_rapoarte_perioada_crescator_pret()
    test_rapoarte_pret_mediu_destinatie()
    test_eliminare_oferte_pret()
    test_eliminare_oferte_luna()


