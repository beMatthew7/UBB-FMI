#ifndef CONSOLE_H
#define CONSOLE_H
#include "console.h"
#include "service.h"


//Functiile din consola
void show_menu();
int readOffer(char type[], char destination[], char departure_date[], float* price);
void show_offers(List* l);
void show_offers_d(List* l);
void show_offers_c(List* l);
void filtrare_lista_ui(List* l);
void run();

#endif 
