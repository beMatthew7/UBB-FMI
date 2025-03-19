#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


typedef struct {
    // Definim structura List
    int data[11];
    int lg;
} List;


int cmmdc(int a, int b) {
    // Calculează CMMDC (Cel Mai Mare Divizor Comun) dintre două numere
    /*
    Calculează Cel Mai Mare Divizor Comun (CMMDC) între două numere.
    
    :param: int a - primul număr.
    :param: int b - al doilea număr.
    :return: CMMDC dintre `a` și `b`.
    */
    while (a != b) {
        if (a > b)
            a = a - b;
        else
            b = b - a;
    }
    return a;
}


int prim(int n) {
    // Verifică dacă un număr este prim
    /*
    Verifică dacă un număr este prim.
    
    :param: int n - numărul care trebuie verificat.
    :return: 1 dacă numărul este prim, 0 altfel.
    */
    if (n < 2)
        return 0;
    for (int i = 2; i <= n / 2; ++i)
        if (n % i == 0)
            return 0;
    return 1;
}


void creeaza_lista_elemente(List* lista) {
    // Creează lista de elemente cu anumite proprietăți
    /*
    Creează o listă de numere care respectă anumite proprietăți: sunt numere pentru care
    fiecare număr mai mic decât ele este prim și este relativ prim față de ele.
    
    :param: List* lista - structura de tip List care va conține numerele.
    :return: -
    */
    lista->lg = 0;  
    int n = 3;
    while (lista->lg < 8) {
        int ok = 1;
        for (int i = 2; i < n; ++i) {
            if (cmmdc(n, i) == 1) {
                if (!prim(i)) { 
                    ok = 0;
                    break;
                }
            }
        }
        if (ok) {
            lista->data[lista->lg] = n;  
            lista->lg++;                   
        }
        n++;
    }
}


void afisare_meniu() {
    // Afișează meniul cu opțiuni pentru utilizator
    /*
    Afișează meniul cu opțiuni pentru utilizator, permițând alegerea între
    determinarea numerelor cu proprietatea specificată sau ieșirea din program.
    
    :param: N/A
    :return: -
    */
    printf("1. Determinarea celor 10 numere cu proprietatea data\n");
    printf("2. Iesire\n");
    printf("Introduceti optiunea: ");
}

int main() {
    List lista;
    while (1) {
        afisare_meniu();
        char optiune;
        scanf(" %c", &optiune);  
        if (optiune == '1') {
            creeaza_lista_elemente(&lista);
            for (int i = 0; i < lista.lg; ++i) {
                printf("%d ", lista.data[i]);
            }
            printf("\n");
        }
        else if (optiune == '2') {
            break;
        }
    }
    return 0;
}
