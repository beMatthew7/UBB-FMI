#include "Matrice.h"
#include <exception>

using namespace std;

/// Teta(1)
Matrice::Matrice(int m, int n) {
    ///
    /// Constructor pentru Matrice
    ///  - verificam ca numarul de linii si coloane sa fie > 0 
    /// daca este atunci modificam daca nu ridicam o eroare

    if (m <= 0 || n <= 0)
    {
        throw "Matricea nu poate fi vida";
    }

    this->nr_Linii = m;
    this->nr_Coloane = n;

    // Initializam indicii de inceput pentru fiecare linie cu -1 (linie goala)
    for (int i = 0; i < m; i++) {
        this->linii.Adauga(-1);
    }
}


// Teta(1)
int Matrice::nrLinii() const {
    /* returneaza numarul de linii(int) */
    return this->nr_Linii;
}

// Teta(1)
int Matrice::nrColoane() const {
    /* returneaza numarul de coloane(int) */
    return this->nr_Coloane;
}

/// Caz Favorabil : Teta(1)
/// Caz Defavorabil : Teta(n)
/// Caz Mediu : Teta(n)
/// Caz Total : O(n)
TElem Matrice::element(int i, int j) const {
    /* cautam elementul daca exista ii returnam valoarea altfel returnam valoarea 0
    se arunca exceptie daca (i,j) nu e pozitie valida in Matrice  */
    if (i < 0 || j < 0 || j >= this->nrColoane() || i >= this->nrLinii())
    {
        throw exception();
    }

    // Gasim inceputul liniei i
    int start = this->linii.v[i];
    if (start == -1) {
        return NULL_TELEMENT;  // Linia nu contine elemente nenule
    }

    // Cautam elementul in linia i
    int k = start;
    while (k < this->coloane.getLen() &&
        (k == start || (k > 0 && this->coloane.v[k - 1] < this->coloane.v[k]))) {
        if (this->coloane.v[k] == j) {
            return this->valori.v[k];
        }
        if (this->coloane.v[k] > j) {
            break;  // Am trecut de pozitia posibila
        }
        k++;
    }

    return NULL_TELEMENT;
}


/// Caz Favorabil : Teta(1)
/// Caz Defavorabil : Teta(n)
/// Caz Mediu : Teta(n)
/// Caz Total : O(n)
TElem Matrice::modifica(int i, int j, TElem e) {
    /*
    ! se arunca exceptie daca (i,j) nu e pozitie valida in Matrice

    Cautam elementul e de pe linia i , coloana j in vectorii nostri daca exista
    il modificam si ii returnam vechea valoare

    Altfel

    Adaugam cate un element nou la finalul fiecaruia dintre cei 3 vectori
    apoi ii cautam pozitia corecta, mutam toate elementele la dreapta pentru a
    ii face loc.

    */
    if (i < 0 || j < 0 || j >= this->nrColoane() || i >= this->nrLinii())
    {
        throw exception();
    }

    // Gasim inceputul liniei i
    int start = this->linii.v[i];

    // Daca linia e goala si elementul e 0, nu facem nimic
    if (start == -1 && e == NULL_TELEMENT) {
        return NULL_TELEMENT;
    }

    // Daca linia e goala si elementul e nenul, cream o noua intrare
    if (start == -1) {
        this->coloane.Adauga(j);
        this->valori.Adauga(e);
        this->linii.v[i] = this->coloane.getLen() - 1;
        return NULL_TELEMENT;
    }

    // Cautam elementul in linia i
    int k = start;
    while (k < this->coloane.getLen() &&
        (k == start || (k > 0 && this->coloane.v[k - 1] < this->coloane.v[k]))) {
        if (this->coloane.v[k] == j) {
            // Am gasit elementul, il actualizam
            TElem vechi = this->valori.v[k];
            if (e == NULL_TELEMENT) {
                // Stergem elementul daca noua valoare e 0
                for (int p = k; p < this->coloane.getLen() - 1; p++) {
                    this->coloane.v[p] = this->coloane.v[p + 1];
                    this->valori.v[p] = this->valori.v[p + 1];
                }
                this->coloane.Sterge(this->coloane.getLen() - 1);
                this->valori.Sterge(this->valori.getLen() - 1);

                // Actualizam indicii de inceput pentru liniile afectate
                if (k == start) {
                    this->linii.v[i] = -1;
                }
            }
            else {
                this->valori.v[k] = e;
            }
            return vechi;
        }
        if (this->coloane.v[k] > j) {
            break;  // Inseram aici
        }
        k++;
    }

    // Inseram noul element daca e nenul
    if (e != NULL_TELEMENT) {
        // Facem loc pentru noul element
        this->coloane.Adauga(0);  // temporar
        this->valori.Adauga(0);   // temporar
        for (int p = this->coloane.getLen() - 1; p > k; p--) {
            this->coloane.v[p] = this->coloane.v[p - 1];
            this->valori.v[p] = this->valori.v[p - 1];
        }

        // Inseram noul element
        this->coloane.v[k] = j;
        this->valori.v[k] = e;

        // Actualizam indicele de inceput pentru linia i daca e necesar
        if (k <= start) {
            this->linii.v[i] = k;
        }
    }

    return NULL_TELEMENT;
}