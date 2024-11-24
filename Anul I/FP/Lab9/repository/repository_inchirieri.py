from domain.inchiriere import Inchiriere

class RepoInchirieri:
    def __init__(self):
        self.__inchirieri = []

    def adauga_inchiriere(self, inchiriere):
        self.__inchirieri.append(inchiriere)

    def get_all(self):
        return self.__inchirieri

    def sterge_inchiriere(self, inchiriere):
        self.__inchirieri.remove(inchiriere)

