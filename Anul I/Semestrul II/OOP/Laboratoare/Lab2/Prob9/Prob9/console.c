#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "service.h"
#include "console.h"

void show_menu() {
    printf("1. Adauga oferta noua\n");
    printf("2. Actualizeaza oferta\n");
    printf("3. Sterge oferta\n");
    printf("4. Afiseaza toate ofertele ordonat(crescator/descrescator)\n");
    printf("5. Afiseaza ofertle filtrate dupa un criteriu(destinatie, tip, pret)\n");
	printf("A. Afiseaza toate ofertele\n");
	printf("C. Adaugare oferte default\n");
    printf("E. Exit\n");
    printf("Alegeti o optiune: ");
}

int readOffer(char type[], char destination[], char departure_date[], float* price) {
    printf("Introduceti tipul ofertei: ");
    scanf("%s", type);

    printf("Introduceti destinatia: ");
    scanf("%s", destination);

    printf("Introduceti data plecarii: ");
    scanf("%s", departure_date);

    printf("Introduceti pretul: ");
    scanf("%f", price);

  
}

void show_offers(List* l) {
    if (l == NULL || l->len == 0) {
        printf("Nu exista oferte in lista.\n");
        return;
    }

    for (int i = 0; i < l->len; ++i) {
        printf("  Tip: %s\n", l->array[i].type);
        printf("  Destinatie: %s\n", l->array[i].destination);
        printf("  Data plecarii: %s\n", l->array[i].departure_date);
        printf("  Pret: %d\n", l->array[i].price);
        printf("\n");
    }
}

void show_offers_d(List* l)
{
	if (l == NULL || l->len == 0) {
		printf("Nu exista oferte in lista.\n");
		return;
	}
    offers_d(l);
	show_offers(l);
	
}   
void show_offers_c(List* l)
{
    if (l == NULL || l->len == 0) {
        printf("Nu exista oferte in lista.\n");
        return;
    }
    offers_c(l);
    show_offers(l);

}

void filtrare_lista_ui(List* l) {
    char criteriu[50], valoare[50];
    float pret = -1;
    printf("Introduceti criteriul de filtrare (destinatie, tip, pret): ");
    scanf("%s", criteriu);
    printf("Introduceti valoarea: ");
    if (strcmp(criteriu, "pret") == 0) {
        scanf("%f", &pret);
    } else {
        scanf("%s", valoare);
    }
    List* l2 = filtrare_lista(criteriu, valoare, pret, l);
    show_offers(l2);
    destroyList(l2);
}

void run() {
    List* l = createList(10);
    char type[50], destination[50], departure_date[50];
    float price;
    char optiune, ord;

    while (1) {
        show_menu();
        scanf(" %c", &optiune);

        switch (optiune) {
        case '1':
            readOffer(type, destination, departure_date, &price);
            addOffer(type, destination, departure_date, price, l);
            printf("Oferta adaugata cu succes!\n");
            break;

        case '2':
                readOffer(type, destination, departure_date, &price);
				updateOffer(type, destination, departure_date, price, l);
				printf("Oferta actualizata cu succes!\n");
			
                break;

        case '3':
			    readOffer(type, destination, departure_date, &price);
				deleteOffer(type, destination, departure_date, price, l);
				printf("Oferta stearsa cu succes!\n");
			
            break;

        case '4':
			printf("Introduceti ordinea (crescator/descrescator): ");
			scanf(" %c", &ord);
            switch (ord)
            {
			case 'c':
				show_offers_c(l);
				break;
			case 'd':
				show_offers_d(l);
				break;
			default:
				printf("Optiune invalida!\n");
            }
            break;

        case '5':
            filtrare_lista_ui(l);
            break;
        
		case 'A':
            show_offers(l);
            break;

        case 'C':
            addDefaultOffers(l);
            printf("Ofertele default au fost adaugate cu succes!\n");
            break;

        case 'E':
            destroyList(l);
            return;


        default:
            printf("Optiune invalida!\n");
            break;
        }
    }
}
