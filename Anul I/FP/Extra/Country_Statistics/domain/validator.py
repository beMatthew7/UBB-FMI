from domain.tara import Tara

class ValidatorException(Exception):
    def __init__(self, message_list = ''):
        self.message_list = message_list

class Validator(self):
    def __init__(self):
        pass

    def validate(self, tara):
        errors = []
        if tara.get_nume_tara() == '':
            errors.append('Numele tarii nu poate fi vid')
        if tara.get_capitala() == '':
            errors.append('Capitala nu poate fi vida')
        if tara.get_litera_tarii() == '':
            errors.append('Litera tarii nu poate fi vida')
        if tara.get_populatie() < 0:
            errors.append('Populatia nu poate fi negativa')
        if tara.get_suprafata() < 0:
            errors.append('Suprafata nu poate fi negativa')
        if len(errors) > 0:
            raise ValidatorException(errors)