
from domain.carte import Carte
from domain.validation import ValidatorCarte
from colorama import Fore, Style

def test_carte():
    carte = Carte(1, "Micul Print", "O poveste filozofică pentru copii și adulți.", "Antoine de Saint-Exupery")
    assert carte.get_titlu() == "Micul Print"
    assert carte.get_descriere() == "O poveste filozofică pentru copii și adulți."
    assert carte.get_autor() == "Antoine de Saint-Exupery"

    carte.set_titlu("Lupul de mare")
    assert carte.get_titlu() == "Lupul de mare"

    carte.set_autor("Jack London")
    assert carte.get_autor() == "Jack London"

def test_validare_carte():
    validator = ValidatorCarte()
    
    # Test cu titlu scurt
    carte_invalida1 = Carte(1, "A", "O descriere valida.", "Autor Valid")
    try:
        validator.validate(carte_invalida1)
        assert False
    except ValueError:
        assert True

    # Test cu autor lipsă
    carte_invalida2 = Carte(2, "Titlu Valid", "O descriere valida.", "")
    try:
        validator.validate(carte_invalida2)
        assert False
    except ValueError:
        assert True


