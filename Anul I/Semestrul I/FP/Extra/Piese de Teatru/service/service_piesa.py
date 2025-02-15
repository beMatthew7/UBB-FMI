from domain.piesa import Piesa
from random import choice, randint, random

class ControllerPiesa:
    def __init__(self, repo, validator):
        self.__repo = repo
        self.__validator = validator

    def adauga_piesa(self, titlu, regizor, gen, durata):
        """
        Adauga o piesa de teatru
        :param titlu: titlul piesei
        :param regizor: regizorul piesei
        :param gen: genul piesei
        :param durata: durata piesei
        :return: -
        """
        piesa = Piesa(titlu, regizor, gen, durata)
        self.__validator.validate(piesa)
        self.__repo.store(piesa)

    def modifica_piesa(self, tiltu, regizor, new_gen, new_durata):
        """
        Modifica genul si durata piesei
        :param tiltu: titlul piesei
        :param regizor: regizorul piesei
        :param new_gen: noul gen
        :param new_durata: noua durata
        :return: -
        """
        piesa = Piesa(tiltu, regizor, new_gen, new_durata)
        self.__validator.validate(piesa)
        self.__repo.update(piesa)

    def genereaza_nume_random(self):
        """
        Generează un nume aleatoriu pentru regizor sau orice altă entitate.
        Alternanță între vocale și consoane, și poate conține un spațiu.
        :return: un string care reprezintă numele generat
        """
        vocale = "aeiou"
        consoane = "bcdfghjklmnpqrstvwxyz"
        
       
        lungime = randint(7, 10)
        
        nume = []
        
        
        for i in range(lungime):
            if i % 2 == 0:
                nume.append(choice(consoane))
            else:
                nume.append(choice(vocale))
        
       
        pozitie_spatiu = randint(1, lungime - 1)
        nume.insert(pozitie_spatiu, ' ')
        
       
        return ''.join(nume)
    def creeaza_piese_random(self, numar):
        """
        Creeaza piese random
        :param numar: numarul de piese
        :return: -
        """
        while(numar > 0):
            titlu = self.genereaza_nume_random()  
            regizor = self.genereaza_nume_random()
            gen = choice(["Comedie", "Drama", "Satira", "Altele"])  
            durata = randint(60, 180)
            piesa = Piesa(titlu, regizor, gen, durata)
            try:
                self.__repo.store(piesa)
                numar -= 1
            except:
                continue    

    def exporta_piese(self, filename):
        """
        Exporta piesele in fisierul dat
        :param filename: numele fisierului
        :return: -
        """
        lista_piese = []
        for piese in self.__repo.get_all():
            lista_piese.append(piese)
        lista_piese.sort(key=lambda x: x.get_titlu() + x.get_regizor())
        with open(filename, 'w') as f:
            for piesa in lista_piese:
                f.write(f"{piesa.get_titlu()},{piesa.get_regizor()},{piesa.get_gen()},{piesa.get_durata()}\n")        