#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int prim(int n) {
    // Verific? dac? un num?r este prim
    /*
      Verific? dac? un num?r este prim.

      :param: int n - num?rul care trebuie verificat.
      :return: 1 dac? num?rul este prim, 0 altfel.
    */

    if (n < 2) return 0;
    for (int d = 2; d * d <= n; ++d) {
        if (n % d == 0) {
            return 0;
        }
    }
    return 1;
}

void afiseazaGrupPrim(int p, int* contor, int nr_termeni) {
    // Tip?re?te numerele de la `p` pân? la 1, dac? num?rul `p` este prim, într-un grup.
    /*
      Tip?re?te numerele de la `p` pân? la 1, dac? num?rul `p` este prim, într-un grup.

      :param: int p - num?rul prim care va fi procesat.
      :param: int* contor - un pointer care ?ine eviden?a num?rului de termeni afi?a?i.
      :param: int nr_termeni - num?rul total de termeni ce trebuie afi?a?i.
      :return: Nu returneaz? nimic, doar tip?re?te numerele.
    */
    for (int i = p; i >= 1 && *contor < nr_termeni; --i) {
        printf("%d ", i);
        (*contor)++;
    }
}


void afiseazaGrupCompus(int n, int* contor, int nr_termeni) {
    // Tip?re?te num?rul `n` ?i factorii s?i primi în grupuri, dac? `n` nu este prim.
    /*
      Tip?re?te num?rul `n` ?i factorii s?i primi în grupuri, dac? `n` nu este prim.

      :param: int n - num?rul compus care va fi procesat.
      :param: int* contor - un pointer care ?ine eviden?a num?rului de termeni afi?a?i.
      :param: int nr_termeni - num?rul total de termeni ce trebuie afi?a?i.
      :return: Nu returneaz? nimic, doar tip?re?te numerele.
    */
    printf("%d ", n);
    (*contor)++;

    for (int d = 2; d < n && *contor < nr_termeni; ++d) {
        if (n % d == 0) {
            for (int j = 0; j < d && *contor < nr_termeni; ++j) {
                printf("%d ", d);
                (*contor)++;
            }
        }
    }
}


void genereazaSiAfiseazaSir(int nr_termeni) {
    // Genereaz? ?i afi?eaz? un ?ir de numere pân? la un num?r de termeni specificat.
    /*
      Genereaz? ?i afi?eaz? un ?ir de numere pân? la un num?r de termeni specificat.
      Fiecare num?r este procesat în func?ie de faptul c? este prim sau compus.

      :param: int nr_termeni - num?rul de termeni care trebuie genera?i ?i afi?a?i.
      :return: -
    */
    int contor = 0;
    int n = 1;

    while (contor < nr_termeni) {
        if (prim(n)) {
            afiseazaGrupPrim(n, &contor, nr_termeni);
        }
        else {
            afiseazaGrupCompus(n, &contor, nr_termeni);
        }
        n++;
    }
    printf("\n");
}


void afisare_meniu() {
    // Afi?eaz? meniul cu op?iuni pentru utilizator.
    /*
      Afi?eaz? meniul cu op?iuni pentru utilizator.


      :return: -
    */
    

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
            int nr_termeni;
            printf("Introduceti numarul de termeni: ");
            scanf("%d", &nr_termeni);
            genereazaSiAfiseazaSir(nr_termeni);
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
