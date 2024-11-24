from datetime import datetime
from ui import *
from pachet_calatorie import *
from list_manager import *


def test_creare_pachet():
    pachet_de_calatorie1 = creare_pachet('13/09/2024', '20/09/2024', 'Praga', 500)
    assert (get_data_de_inceput(pachet_de_calatorie1) == datetime(2024, 9, 13))
    assert (get_data_de_final(pachet_de_calatorie1) == datetime(2024, 9, 20))
    assert (get_destinatia(pachet_de_calatorie1) == "Praga")
    assert (get_pretul(pachet_de_calatorie1) == 500)

def test_adaugare_la_lista():
    test_list = []
    assert(len(test_list) == 0)
    adaugare_la_lista(test_list, creare_pachet('22/09/2024', '29/09/2024', 'Barcelona', 450))
    assert(len(test_list) == 1)
    adaugare_la_lista(test_list, creare_pachet('10/10/2024', '12/10/2024', 'Monaco', 300))
    assert(len(test_list) == 2)

def test_calatorii_cautate_date():
    test_list = []
    test_list_eligibile = []
    adaugare_la_lista(test_list, creare_pachet('22/09/2024', '29/09/2024', 'Barcelona', 450))
    adaugare_la_lista(test_list, creare_pachet('10/10/2024', '12/10/2024', 'Monaco', 300))
    assert(calatorii_cautate_date(test_list, test_list_eligibile, datetime(2024, 11, 1), datetime(2024, 11, 15)) == [])
    assert(calatorii_cautate_date(test_list, test_list_eligibile, datetime(2024, 9, 20), datetime(2024, 9, 30)) == [{'data_de_inceput': datetime(2024, 9, 22), 'data_de_final': datetime(2024, 9, 29),  'destinatia': 'Barcelona', 'pretul': 450}])

def test_calatorii_cautate_destinatie_pret():
    test_list = []
    test_list_eligibile = []
    adaugare_la_lista(test_list, creare_pachet('22/09/2024', '29/09/2024', 'Barcelona', 450))
    adaugare_la_lista(test_list, creare_pachet('10/10/2024', '12/10/2024', 'Monaco', 300))
    assert(calatorii_cautate_destinatie_pret(test_list, test_list_eligibile, 'Barcelona', 500) == [{'data_de_inceput': datetime(2024, 9, 22), 'data_de_final': datetime(2024, 9, 29), 'destinatia': 'Barcelona', 'pretul': 450}])
    assert(calatorii_cautate_destinatie_pret(test_list, test_list_eligibile, 'Monaco', 350) == [{'data_de_inceput': datetime(2024, 10, 10), 'data_de_final': datetime(2024, 10, 12), 'destinatia': 'Monaco', 'pretul': 300}])

def test_calatorii_cautate_data_final():
    test_list = []
    test_list_eligibile = []
    adaugare_la_lista(test_list, creare_pachet('22/09/2024', '29/09/2024', 'Barcelona', 450))
    adaugare_la_lista(test_list, creare_pachet('10/10/2024', '12/10/2024', 'Monaco', 300))
    adaugare_la_lista(test_list, creare_pachet('05/11/2024', '10/11/2024', 'Paris', 600))
    assert(calatorii_cautate_data_final(test_list, test_list_eligibile, datetime(2024, 10, 12) ) == [{'data_de_inceput': datetime(2024, 10, 10), 'data_de_final': datetime(2024, 10, 12), 'destinatia': 'Monaco', 'pretul': 300}])
    assert(calatorii_cautate_data_final(test_list, test_list_eligibile, datetime(2024, 10, 12)) == [{'data_de_inceput': datetime(2024, 10, 10), 'data_de_final': datetime(2024, 10, 12), 'destinatia': 'Monaco', 'pretul': 300}])


def test_verificare_data():
    assert verificare_data("29/02/2024") == True
    assert verificare_data("28/02/2023") == True
    assert verificare_data("31/12/2023") == True
    
    assert verificare_data("32/01/2024") == False
    assert verificare_data("29/02/2023") == False
    assert verificare_data("15/13/2024") == False 
    assert verificare_data("12/12/20") == False
    assert verificare_data("12-12-2024") == False  

def test_eliminare_oferte_pret():
    test_list = []
    test_list_2 = []
    adaugare_la_lista(test_list, creare_pachet('22/09/2024', '29/09/2024', 'Barcelona', 450))
    adaugare_la_lista(test_list, creare_pachet('10/10/2024', '12/10/2024', 'Monaco', 300))
    adaugare_la_lista(test_list, creare_pachet('05/11/2024', '10/11/2024', 'Paris', 600))
    test_list_2 = eliminare_oferte_pret(test_list, 400, "Berlin")
    assert(len(test_list_2))






def ruleaza_teste():
    test_creare_pachet()
    test_adaugare_la_lista()
    test_calatorii_cautate_date()
    test_verificare_data()
    test_eliminare_oferte_pret()



 









               




                


ruleaza_teste()
run()