from datetime import datetime
from verificari import *
def citeste_preferinte_interval_calatorie():
    k = False 
    while(k == False):
        data_de_incepere = input("Introduceti data de inceput a calatoriei: ") 
        data_de_incepere = data_de_incepere.strip()
        k = verificare_data(data_de_incepere)
    k = False 
    data_de_incepere = datetime.strptime(data_de_incepere, "%d/%m/%Y")
    while(k == False):
        data_de_sfarsit = input("Introduceti data de inceput a calatoriei: ") 
        data_de_sfarsit = data_de_sfarsit.strip()
        k = verificare_data(data_de_sfarsit)
    data_de_sfarsit = datetime.strptime(data_de_sfarsit, "%d/%m/%Y")
    return data_de_incepere, data_de_sfarsit  

       

def citeste_preferinte_destinatie_pret_calatorie():
    destinatie = input("Introduceti destinatia preferata: ").capitalize()
    pret = int(input("Introduceti bugetul maxim pe care doriti sa-l alocati: "))
    return destinatie, pret
       

def citeste_info_data_de_final_preferata():
    data_de_final_preferata = input("Introduceti data de sfarsit preferata: ")
    data_de_final_preferata = datetime.strptime(data_de_final_preferata, "%d/%m/%Y")
    return data_de_final_preferata
    
 
      
def citire_numar_pachet():
    numar = int(input())
    return numar