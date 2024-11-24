import math

from domain.carte import Carte


class ValidatorCarte:
    def validate(self, carte: Carte):
        """
         Valideaza o carte data
         :param carte: cartea de validat
         :return: -
         :raises: ValueError cu mesajele de eroare daca cartea nu este valida
         """
        errors = []
        if len(carte.get_titlu()) < 2:
            errors.append("Titlul cartii trebuie sa aiba cel putin un caracter.")
        if len(carte.get_descriere()) < 1:
            errors.append("Descriere cartii trebuie sa aiba cel putin un caracter.")
        if len(carte.get_autor()) < 2:
            errors.append("Autorul cartii trebuie sa aiba cel putin un caracter.")
        

        if len(errors) > 0:
            error_message = '\n'.join(errors)
            raise ValueError(error_message)