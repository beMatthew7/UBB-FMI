from datetime import datetime
from verificare import verificare_data
from pachet import get_data_de_final,get_data_de_inceput,get_destinatia,get_pretul
from list_utils import add_to_list



def adaugare_la_lista(lista_calatorii, pachet_de_calatorie):
    """
    Adaugă un pachet de călătorie la lista de călătorii.

    :param lista_calatorii: lista de călătorii în care se adaugă pachetul.
    :param pachet_de_calatorie: pachetul de călătorie care se adaugă.
    """
    add_to_list(lista_calatorii, pachet_de_calatorie)

    
def calatorii_cautate_date(lista_calatorii, lista_calatorii_eligibile, data_de_incepere, data_de_sfarsit):
    """
    Filtrează pachetele de călătorie care se încadrează într-un interval de date dat.

    :param lista_calatorii: lista de pachete de călătorii disponibile.
    :param lista_calatorii_eligibile: lista de pachete eligibile, care va fi completată cu rezultatele.
    :param data_de_incepere: data de început a intervalului.
    :param data_de_sfârșit: data de sfârșit a intervalului.
    
    :return: lista cu pachetele de călătorie eligibile care se încadrează în intervalul dat.
    """
    for calatorie in lista_calatorii:
        if get_data_de_inceput(calatorie) >= data_de_incepere and get_data_de_final(calatorie) <= data_de_sfarsit:
            lista_calatorii_eligibile.append(calatorie)
    return lista_calatorii_eligibile        

def calatorii_cautate_destinatie_pret(lista_calatorii, lista_calatorii_eligibile, destinatie_preferata, buget):
    """
    Filtrează pachetele de călătorie care au o destinație specificată și un preț mai mic sau egal cu bugetul dat.

    :param lista_calatorii: lista de pachete de călătorii disponibile.
    :param lista_calatorii_eligibile: lista de pachete eligibile, care va fi completată cu rezultatele.
    :param destinatie_preferata: destinația călătoriei specificată de utilizator.
    :param buget: bugetul maxim specificat de utilizator.
    
    :return: lista cu pachetele de călătorie eligibile care se încadrează în destinația și bugetul specificat.
    """
    for calatorie in lista_calatorii:
        if get_destinatia(calatorie) == destinatie_preferata and get_pretul(calatorie) <= buget:
            lista_calatorii_eligibile.append(calatorie)
    return lista_calatorii_eligibile        

def calatorii_cautate_data_final(lista_calatorii, lista_calatorii_eligibile, data_de_final_preferata):
    """
    Filtrează pachetele de călătorie care au data de sfârșit egală cu cea specificată de utilizator.

    :param lista_calatorii: lista de pachete de călătorii disponibile.
    :param lista_calatorii_eligibile: lista de pachete eligibile, care va fi completată cu rezultatele.
    :param data_de_final_preferata: data de sfârșit preferată specificată de utilizator.
    
    :return: lista cu pachetele de călătorie eligibile care se termină la data specificată.
    """
    for calatorie in lista_calatorii:
        if get_data_de_final(calatorie) == data_de_final_preferata:
            lista_calatorii_eligibile.append(calatorie)
    return lista_calatorii_eligibile 

def stergere_pachet_destinatie(lista_noua, lista_calatorii, destinatia_data):
    """
    Ștergerea tuturor pachetelor de călătorie disponibile pentru o destinație dată.
    
    :param lista_noua: listă inițial goală în care se vor păstra rezultatele.
    :param lista_calatorii: lista de pachete de călătorii disponibile.
    :param destinatia_data: destinația introdusă de utilizator.

    :return: lista cu pachetele de călătorii rămase după ștergere.
    """
    for calatorie in lista_calatorii:
        if get_destinatia(calatorie) != destinatia_data:
            lista_noua.append(calatorie)
    return lista_noua

def stergere_pachet_durata(lista_noua, lista_calatorii, durata_data):
    """
    Ștergerea tuturor pachetelor de călătorie care au o durată mai scurtă decât un număr de zile dat.
    
    :param lista_noua: listă inițial goală în care se vor păstra rezultatele.
    :param lista_calatorii: lista de pachete de călătorii disponibile.
    :param durata_data: numărul de zile minim specificat.

    :return: lista cu pachetele de călătorii rămase după ștergere.
    """
    for calatorie in lista_calatorii:
        if (get_data_de_final(calatorie) - get_data_de_inceput(calatorie)).days > durata_data:
            lista_noua.append(calatorie)
    return lista_noua

def stergere_pachet_pret(lista_noua, lista_calatorii, pret_data):
    """
    Ștergerea tuturor pachetelor de călătorie care au un preț mai mic decât valoarea specificată.
    
    :param lista_noua: listă inițial goală în care se vor păstra rezultatele.
    :param lista_calatorii: lista de pachete de călătorii disponibile.
    :param pret_data: prețul minim specificat.

    :return: lista cu pachetele de călătorii rămase după ștergere.
    """
    for calatorie in lista_calatorii:
        if get_pretul(calatorie) >= pret_data:
            lista_noua.append(calatorie)
    return lista_noua

def eliminare_oferte_pret(lista_p, pret_maxim, destinatia_n):
    """
    Selectează pachetele cu un preț mai mic sau egal cu valoarea specificată și o destinație diferită de cea dată.

    :param lista_p: lista de pachete de călătorii disponibile.
    :param pret_maxim: bugetul maxim specificat de utilizator.
    :param destinatia_n: destinația care nu este dorită.

    :return: lista cu pachetele de călătorie filtrate.
    """
    lista_filtrata = []
    for calatorie in lista_p:
        if get_pretul(calatorie) <= pret_maxim and get_destinatia(calatorie) != destinatia_n:
            lista_filtrata.append(calatorie)
    return lista_filtrata

def eliminare_oferte_luna(lista_p, luna_dorita):
    """
    Selectează pachetele care au loc în luna dorită specificată.

    :param lista_p: lista de pachete de călătorii disponibile.
    :param luna_dorita: luna dorită specificată de utilizator.

    :return: lista cu pachetele de călătorie filtrate.
    """
    lista_filtrata = []
    for calatorie in lista_p:
        if get_data_de_final(calatorie).month == luna_dorita and get_data_de_inceput(calatorie).month == luna_dorita:
            lista_filtrata.append(calatorie)
    return lista_filtrata

def rapoarte_numar_destinatie(lista_calatorii, destinatia):
    """
    Tipărirea numărului de oferte pentru o destinație dată
    :param lista_calatorii: lista de pachete de calatorii disponibile
    :param destinatia: destinatia dorita

    return: numar calatorii eligibile
    """
    numar = 0
    for calatorie in lista_calatorii:
        if get_destinatia(calatorie) == destinatia:
            numar += 1

    return numar

def rapoarte_perioada_crescator_pret(lista_calatorii, data_de_inceput, data_de_final):
    """
    Tipărirea tuturor pachetelor disponibile într-o anumită perioadă citită de la tastatură în ordinea crescătoare a prețului
    :param lista_calatorii: lista de pachete de calatorii disponibile
    :param data_de_inceput: data de inceput dorita
    :param data_de final: data de final dorita

    returneaza lista ordonata dupa pret cu datele cuprinse in intervalul data
    """
    lista_noua = []
    for calatorie in lista_calatorii:
        if get_data_de_inceput(calatorie) >= data_de_inceput and get_data_de_final(calatorie) <= data_de_final:
            lista_noua.append(calatorie)
    
    lista_noua = sorted(lista_noua, key = lambda x: x[3])        
    return lista_noua

def rapoarte_pret_mediu_destinatie(lista_calatorii, destinatia):

    """
    Tipărirea mediei de preț pentru o destinație dată 
    :param lista_calatorii: lista de pachete de calatorii disponibile
    :param destinatia: destinatia dorita

    return media de pret pentru destinatia data
    """
    suma = 0.0
    numar = 0.0

    for calatorie in lista_calatorii:
        if get_destinatia(calatorie) == destinatia:
            suma += get_pretul(calatorie)
            numar += 1

    return (suma / numar)            


    