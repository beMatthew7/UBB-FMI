#pragma once
#ifndef VALIDATORS_H
#define VALIDATORS_H
#include "holiday_offer.h"

int validateType(char type[]);
///	Valideaza tipul ofertei
/// Parametrii:
/// type - tipul ofertei
/// Returneaza 1 daca tipul este valid, 0 altfel

int validateDestination(char destination[]);
///	Valideaza destinatia
/// Parametrii:
/// destination - destinatia
/// Returneaza 1 daca destinatia este valida, 0 altfel

int validatePrice(float price);
///	Valideaza pretul
/// Parametrii:
/// price - pretul
/// Returneaza 1 daca pretul este valid, 0 altfel

int validateDate(char date[]);
///	Valideaza data
/// Parametrii:
/// date - data
/// Returneaza 1 daca data este valida, 0 altfel

#endif // VALIDATORS_H