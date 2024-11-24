def adaugare_la_lista(lista_calatorii, pachet_de_calatorie):
    """
    Adauga pachet_de_calatorie lista de calatorii
    :param lista_calatorii: lista de calatorii
    :param pachet_de_calatorie: pachetul care se adauga
    """
    lista_calatorii.append(pachet_de_calatorie)

def calatorii_cautate_date(lista_calatorii, lista_calatorii_eligibile, data_de_incepere, data_de_sfarsit):
    """
    Filtrează pachetele de călătorie care se încadrează într-un interval de date dat.

    :param lista_calatorii: lista de pachete de călătorii disponibile.
    :param lista_calatorii_eligibile: lista de pachete eligibile, care va fi completată cu rezultatele.
    :param data_de_incepere: data de început a intervalului.
    :param data_de_sfarsit: data de sfârșit a intervalului.
    
    :return: lista cu pachetele de călătorie eligibile care se încadrează în intervalul dat.
    """
    for calatorie in lista_calatorii:
        if(calatorie['data_de_inceput'] >= data_de_incepere and calatorie['data_de_final'] <= data_de_sfarsit):
            lista_calatorii_eligibile.append(calatorie)
    return lista_calatorii_eligibile 

def calatorii_cautate_destinatie_pret(lista_calatorii,lista_calatorii_eligibile, destinatie_preferata, buget):
    """
    Filtrează pachetele de călătorie care au o destinație specificată și un preț mai mic sau egal cu bugetul dat.

    :param lista_calatorii: lista de pachete de călătorii disponibile.
    :param lista_calatorii_eligibile: lista de pachete eligibile, care va fi completată cu rezultatele.
    :param destinatie_preferata: destinația călătoriei specificată de utilizator.
    :param buget: bugetul maxim specificat de utilizator.
    
    :return: lista cu pachetele de călătorie eligibile care se încadrează în destinația și bugetul specificat.
    """
    for calatorie in lista_calatorii:
        if(calatorie['destinatia'] == destinatie_preferata and calatorie['pretul'] <= buget):
            lista_calatorii_eligibile.append(calatorie)
    return lista_calatorii_eligibile 

def calatorii_cautate_data_final(lista_calatorii,lista_calatorii_eligibile, data_de_final_preferata):
    """
    Filtrează pachetele de călătorie care au data de sfârșit egală cu cea specificată de utilizator.

    :param lista_calatorii: lista de pachete de călătorii disponibile.
    :param lista_calatorii_eligibile: lista de pachete eligibile, care va fi completată cu rezultatele.
    :param data_de_final_preferata: data de sfârșit preferată specificată de utilizator.
    
    :return: lista cu pachetele de călătorie eligibile care se termină la data specificată.
    """
    for calatorie in lista_calatorii:
        if(calatorie['data_de_final'] == data_de_final_preferata):
            lista_calatorii_eligibile.append(calatorie)
    return lista_calatorii_eligibile

def eliminare_oferte_pret(lista_p, pret_maxim, destinatia_n):
    """
    Selecteaza pachetele cu un pret <= fat de cel dat si cu o locatie diferita de cea data

    :param lista_p: lista de pachete de călătorii disponibile:
    :param pret_maxxim: bugetul maxim alocat:
    :param destinatia_n: destinatia unde nu se doreste sa se mearga:
    
    :return: lista cu pachetele de călătorii filtrate
    """
    lista_filtrata = []
    for calatorie in lista_p:
        if(calatorie['pretul'] <= pret_maxim and calatorie['destinatia'] != destinatia_n):
            lista_filtrata.append(calatorie)
    return lista_filtrata    