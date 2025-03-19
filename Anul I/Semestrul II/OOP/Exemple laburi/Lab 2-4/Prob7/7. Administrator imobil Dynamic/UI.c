#include "UI.h"
#include <stdio.h>
#include <stdlib.h>
#include "Validators.h"

void printMenu() {
    printf("\n");
    printf("1. Adauga cheltuiala\n");
    printf("2. Modifica cheltuiala\n");
    printf("3. Sterge cheltuiala\n");
    printf("4. Filtreaza cheltuieli\n");
    printf("5. Sorteaza cheltuieli\n");
    printf("6. Afiseaza toate cheltuielile\n");
    printf("0. Iesire\n");
    printf("Optiune: ");
}

cheltuiala readCheltuiala() {
    cheltuiala c;
    printf("ID: ");
    scanf_s("%d", &c.id);
    printf("Suma: ");
    scanf_s("%d", &c.suma);
    printf("Tip: ");
    scanf_s("%s", c.tip, 20);
    return c;
}

void printList(Lista* l) {
    if (l->len == 0) {
        printf("Lista este goala!\n");
        return;
    }
    
    printf("Lista de cheltuieli:\n");
    for (int i = 0; i < l->len; i++) {
        printf("ID: %d, Suma: %d, Tip: %s\n", l->array[i].id, l->array[i].suma, l->array[i].tip);
    }
}

void testAll() {
    test_Adauga();
    test_Modifica();
    test_Sterge();
    test_cmp1();
    test_cmp2();
    
    test_addCheltuiala();
    test_updateCheltuiala();
    test_deleteCheltuiala();
    test_filterCheltuiala();
    test_sortCheltuiala();
    
    test_isType();
    test_not_negative();
    
    printf("All tests passed!\n");
}

void run() {
    Lista* l = createList(10);
    int running = 1;
    int option;
    
    testAll();
    
    while (running) {
        printMenu();
        scanf_s("%d", &option);
        
        switch (option) {
            case 1: {
                // Add expense
                cheltuiala c = readCheltuiala();
                addCheltuiala(c.id, c.suma, c.tip, l);
                printf("Cheltuiala adaugata cu succes!\n");
                break;
            }
            case 2: {
                // Modify expense
                cheltuiala c = readCheltuiala();
                updateCheltuiala(c.id, c.suma, c.tip, l);
                printf("Cheltuiala modificata cu succes!\n");
                break;
            }
            case 3: {
                // Delete expense
                int id;
                printf("ID: ");
                scanf_s("%d", &id);
                deleteCheltuiala(id, l);
                printf("Cheltuiala stearsa cu succes!\n");
                break;
            }
            case 4: {
                // Filter expenses
                int criteriu, valoare;
                char tip[21] = "";
                
                printf("Criteriu (1-ID, 2-Suma, 3-Tip): ");
                scanf_s("%d", &criteriu);
                
                if (criteriu == 1 || criteriu == 2) {
                    printf("Valoare: ");
                    scanf_s("%d", &valoare);
                } else if (criteriu == 3) {
                    printf("Tip: ");
                    scanf_s("%s", tip, 20);
                    valoare = 0;
                } else {
                    printf("Criteriu invalid!\n");
                    break;
                }
                
                Lista* result = filterCheltuiala(criteriu, valoare, tip, l);
                printList(result);
                destroyList(result);
                break;
            }
            case 5: {
                // Sort expenses
                int criteriu, mod;
                
                printf("Criteriu (1-Suma, 2-Tip): ");
                scanf_s("%d", &criteriu);
                
                printf("Mod (1-Crescator, 0-Descrescator): ");
                scanf_s("%d", &mod);
                
                if (criteriu != 1 && criteriu != 2) {
                    printf("Criteriu invalid!\n");
                    break;
                }
                
                Lista* result = sortCheltuiala(criteriu, mod, l);
                printList(result);
                destroyList(result);
                break;
            }
            case 6: {
                // Show all expenses
                printList(l);
                break;
            }
            case 0: {
                // Exit
                running = 0;
                break;
            }
            default: {
                printf("Optiune invalida!\n");
                break;
            }
        }
    }
    
    // Free memory
    destroyList(l);
}
