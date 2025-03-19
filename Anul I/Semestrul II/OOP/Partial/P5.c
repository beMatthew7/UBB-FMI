#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// Verifică dacă un număr este prim
int prim(int n) {
    if (n < 2) return 0;
    for (int d = 2; d * d <= n; ++d) {
        if (n % d == 0) {
            return 0;
        }
    }
    return 1;
}

// Afiseaza un grup de termeni pentru număr prim
void afiseazaGrupPrim(int p, int* contor, int numarTermeni) {
    for (int i = p; i >= 1 && *contor < numarTermeni; --i) {
        printf("%d ", i);
        (*contor)++;
    }
}

// Afiseaza un grup de termeni pentru număr compus
void afiseazaGrupCompus(int n, int* contor, int numarTermeni) {
    printf("%d ", n);
    (*contor)++;

    for (int d = 2; d < n && *contor < numarTermeni; ++d) {
        if (n % d == 0) {
            for (int j = 0; j < d && *contor < numarTermeni; ++j) {
                printf("%d ", d);
                (*contor)++;
            }
        }
    }
}

// Funcție care generează și afișează sirul cerut
void genereazaSiAfiseazaSir(int numarTermeni) {
    int contor = 0;
    int n = 1;

    while (contor < numarTermeni) {
        if (prim(n)) {
            afiseazaGrupPrim(n, &contor, numarTermeni);
        }
        else {
            afiseazaGrupCompus(n, &contor, numarTermeni);
        }
        n++;
    }
    printf("\n");
}

// Afisare meniu
void afisare_meniu() {
    printf("1. Tipareste un numar precizat de termeni din sir\n");
    printf("2. Iesire\n");
    printf("Introduceti optiunea: ");
}


int main() {
    while (1) {
        afisare_meniu();
        char optiune;
        scanf(" %c", &optiune);

        if (optiune == '1') {
            int numarTermeni;
            printf("Introduceti numarul de termeni: ");
            scanf("%d", &numarTermeni);
            genereazaSiAfiseazaSir(numarTermeni);
        }
        else if (optiune == '2') {
            break;
        }
        else {
            printf("Optiune invalida!\n");
        }
    }

    return 0;
}
