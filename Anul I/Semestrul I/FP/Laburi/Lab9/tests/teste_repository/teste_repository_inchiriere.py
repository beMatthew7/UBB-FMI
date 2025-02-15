from domain.inchiriere import Inchiriere
from repository.repository_inchirieri import RepoInchirieri

def test_adauga_inchiriere():
    repo = RepoInchirieri()
    assert len(repo.get_all()) == 0  

    inchiriere = Inchiriere(1, "Ion", "Micul Prinț", 5)  
    repo.adauga_inchiriere(inchiriere)
    assert len(repo.get_all()) == 1  


def test_sterge_inchiriere():
    repo = RepoInchirieri()
    inchiriere1 = Inchiriere(1, "Ion", "Micul Prinț", 5)
    inchiriere2 = Inchiriere(2, "Maria", "Moromeții", 3)

    repo.adauga_inchiriere(inchiriere1)
    repo.adauga_inchiriere(inchiriere2)
    assert len(repo.get_all()) == 2

    
    repo.sterge_inchiriere(inchiriere1)
    assert len(repo.get_all()) == 1  


def test_get_all():
    repo = RepoInchirieri()
    inchiriere1 = Inchiriere(1, "Ion", "Micul Prinț", 5)
    inchiriere2 = Inchiriere(2, "Maria", "Moromeții", 3)

    repo.adauga_inchiriere(inchiriere1)
    repo.adauga_inchiriere(inchiriere2)
    all_inchirieri = repo.get_all()

    assert len(all_inchirieri) == 2 



