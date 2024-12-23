from domain.piesa import Piesa

class ValidationException(Exception):
    def __init__(self, message):
        super().__init__(message)

class PiesaValidator:
    def validate(self, piesa):
        errors = []
        if(piesa.get_titlu() == ""):
            errors.append("Titlul nu poate fi vid.")
        if(piesa.get_regizor() == ""):
            errors.append("Regizorul nu poate fi vid.")    
        if piesa.get_gen() not in ["Comedie", "Drama", "Satira", "Altele"]:
            errors.append("Genul trebuie sa fie unul dintre: comedy, drama, satire, altele.")
        if piesa.get_durata() < 0:
            errors.append("Durata trebuie sa fie un numar pozitiv.")
        if len(errors) > 0:
            errors_str = '\n'.join(errors)
            raise ValidationException(errors_str)

        
    