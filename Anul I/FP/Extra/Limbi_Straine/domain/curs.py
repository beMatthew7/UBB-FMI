class Curs:
    def __init__(self, id_curs, limba_straina, nivel, pret):
        self.__id_curs = id_curs
        self.__limba_straina = limba_straina
        self.__nivel = nivel
        self.__pret = pret

    def get_id_curs(self):
        return self.__id_curs

    def get_limba_straina(self):
        return self.__limba_straina

    def get_nivel(self):
        return self.__nivel

    def get_pret(self):
        return self.__pret

    def __str__(self):
        return f"{self.__id_curs},{self.__limba_straina},{self.__nivel},{self.__pret}"     