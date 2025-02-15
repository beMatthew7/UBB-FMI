
from domain.carte import Carte
from repository.repository_nou import RepositoryCarti
from colorama import Fore, Style

def test_store_repo():
    repo = RepositoryCarti()
    assert repo.get_size() == 0

    carte = Carte(1, "Micul Print", "O poveste clasică pentru toate vârstele.", "Antoine de Saint-Exupery")
    repo.store(carte)
    assert repo.get_size() == 1

    try:
        repo.store(carte)
        assert False
    except ValueError:
        assert True

def test_find_repo():
    repo = RepositoryCarti()
    carte = Carte(1, "Micul Print", "O poveste clasică pentru toate vârstele.", "Antoine de Saint-Exupery")
    repo.store(carte)

    found_carte = repo.find(1)
    assert found_carte.get_titlu() == "Micul Print"

    missing_carte = repo.find(2)
    assert missing_carte is None
