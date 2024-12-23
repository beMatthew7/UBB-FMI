class Piesa:
    def __init__(self, titlu, regizor, gen, durata):
        self.__titlu = titlu
        self.__regizor = regizor
        self.__gen = gen
        self.__durata = durata

    def get_titlu(self):
        return self.__titlu

    def get_regizor(self):
        return self.__regizor

    def get_gen(self):
        return self.__gen

    def get_durata(self):
        return self.__durata

    def set_gen(self, new_value):
        self.__gen = new_value

    def set_durata(self, new_value):
        self.__durata = new_value       