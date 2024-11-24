
from domain.carte import Carte
from domain.validation_carte import ValidatorCarte
from colorama import Fore, Style

def test_carte():
    carte = Carte(1, "Micul Print", "O poveste filozofică pentru copii și adulți.", "Antoine de Saint-Exupery", 20)
    assert carte.get_titlu() == "Micul Print"
    assert carte.get_descriere() == "O poveste filozofică pentru copii și adulți."
    assert carte.get_autor() == "Antoine de Saint-Exupery"

    carte.set_titlu("Lupul de mare")
    assert carte.get_titlu() == "Lupul de mare"

    carte.set_autor("Jack London")
    assert carte.get_autor() == "Jack London"

def test_validare_carte():
    validator = ValidatorCarte()
    
    
    carte_invalida1 = Carte(1, "A", "O descriere valida.", "Autor Valid", 20)
    try:
        validator.validate(carte_invalida1)
        assert False
    except ValueError:
        assert True




