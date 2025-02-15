from verificare import *
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
    return[data_de_inceput,data_de_final,destinatia,pretul]

def get_data_de_inceput(pachet_de_calatorie):
    """
    Returnează data de început a unui pachet de călătorie.
    :param pachet_de_calatorie: pachetul de călătorie
    :return: data de început
    """
    return pachet_de_calatorie[0]

def get_data_de_final(pachet_de_calatorie):
    """
    Returnează data de final a unui pachet de călătorie.
    :param pachet_de_calatorie: pachetul de călătorie
    :return: data de final
    """
    return pachet_de_calatorie[1]

def get_destinatia(pachet_de_calatorie):
    """
    Returnează destinația unui pachet de călătorie.
    :param pachet_de_calatorie: pachetul de călătorie
    :return: destinația
    """
    return pachet_de_calatorie[2]

def get_pretul(pachet_de_calatorie):
    """
    Returnează prețul unui pachet de călătorie.
    :param pachet_de_calatorie: pachetul de călătorie
    :return: prețul
    """
    return pachet_de_calatorie[3]

from datetime import datetime

def set_data_de_inceput(pachet: list, data_de_inceput_noua: str):
    """Setează data de început pentru un pachet."""
    pachet[0] = datetime.strptime(data_de_inceput_noua, "%d/%m/%Y")

def set_data_de_final(pachet: list, data_de_final_noua: str):
    """Setează data de final pentru un pachet."""
    pachet[1] = datetime.strptime(data_de_final_noua, "%d/%m/%Y")

def set_destinatia(pachet: list, destinatie_noua: str):
    """Setează destinația pentru un pachet."""
    pachet[2] = destinatie_noua

def set_pretul(pachet: list, pret_nou: float):
    """Setează prețul pentru un pachet."""
    pachet[3] = pret_nou
