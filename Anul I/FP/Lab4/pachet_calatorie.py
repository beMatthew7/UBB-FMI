from datetime import datetime
def creare_pachet(data_de_inceput, data_de_final, destinatia, pretul):
    """
    Creeaza pachetul de calatorie pe baza informatiilor date
    :param data_de_inceput: data_de_inceput a calatoriei
    :param data_de_sfarsit: data_de_sfarsit a calatoriei
    :param destinatia: destinatia calatoriei
    :param pretul: pretul calatoriei
    :return: un dictionar care reprezinta pachetul de calatorie
    """
    data_de_inceput = datetime.strptime(data_de_inceput, "%d/%m/%Y")
    data_de_final = datetime.strptime(data_de_final, "%d/%m/%Y")
    return{'data_de_inceput':data_de_inceput, 'data_de_final':data_de_final, 'destinatia':destinatia, 'pretul':pretul}
def get_data_de_inceput(pachet_de_calatorie):
    """
    Returnează data de început a unui pachet de călătorie.
    :param pachet_de_calatorie: pachetul de călătorie
    :return: data de început
    """
    return pachet_de_calatorie['data_de_inceput']

def get_data_de_final(pachet_de_calatorie):
    """
    Returnează data de final a unui pachet de călătorie.
    :param pachet_de_calatorie: pachetul de călătorie
    :return: data de final
    """
    return pachet_de_calatorie['data_de_final']

def get_destinatia(pachet_de_calatorie):
    """
    Returnează destinația unui pachet de călătorie.
    :param pachet_de_calatorie: pachetul de călătorie
    :return: destinația
    """
    return pachet_de_calatorie['destinatia']

def get_pretul(pachet_de_calatorie):
    """
    Returnează prețul unui pachet de călătorie.
    :param pachet_de_calatorie: pachetul de călătorie
    :return: prețul
    """
    return pachet_de_calatorie['pretul']