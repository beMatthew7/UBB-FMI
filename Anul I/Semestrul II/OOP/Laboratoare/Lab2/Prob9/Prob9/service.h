#pragma once
#ifndef SERVICE_H
#define SERVICE_H
#include "repository.h"
#define SERVICE_H


void addOffer(char type[], char destination[], char departure_date[], float price, List* l);
///	Adauga oferta la lista
/// Parametrii: type - tipul ofertei, destination - destinatia, departure_date - data plecarii, price - pretul, l - lista de oferte
/// return: -

void deleteOffer(char type[], char destination[], char departure_date[], float price, List* l);
///	Actualizeaza oferta din lista
/// Parametrii: type - tipul ofertei, destination - destinatia, departure_date - data plecarii, price - pretul, l - lista de oferte
/// return: -

void updateOffer(char type[], char destination[], char departure_date[], float price, List* l);
///	Sterge oferta din lista
/// Parametrii: type - tipul ofertei, destination - destinatia, departure_date - data plecarii, price - pretul, l - lista de oferte
/// return: -

void addDefaultOffers(List* l);
///	Adauga oferte default in lista
/// Parametrii: lista l
/// Lista - lista de oferte

void offers_d(List* l);
///	Afiseaza ofertele din lista
/// Parametrii: lista l
/// Lista - lista de oferte

void offers_c(List* l);
///	Afiseaza ofertele din lista
/// Parametrii: lista l
/// Lista - lista de oferte

List* filtrare_lista(char criteriu[], char valoare[], float pret, List* l);
///	Filtreaza lista de oferte dupa un criteriu si o valoare data
/// Parametrii: criteriu - criteriul de filtrare, valoare - valoarea de filtrare, pret - pretul de filtrare, l - lista de oferte
/// return: lista filtrata

#endif // SERVICE_H
