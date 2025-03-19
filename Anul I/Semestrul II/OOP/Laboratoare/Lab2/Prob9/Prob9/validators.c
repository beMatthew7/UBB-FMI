#include "validators.h"
#include <string.h>

int validateType(char type[])
{
	///	Valideaza tipul ofertei
	/// Parametrii:
	/// type - tipul ofertei
	/// Returneaza 1 daca tipul este valid, 0 altfel
	if (strcmp(type, "city_break") == 0 || strcmp(type, "mare") == 0 || strcmp(type, "munte") == 0)
		return 1;
	return 0;
}

int validateDestination(char destination[])
{
	///	Valideaza destinatia
	/// Parametrii:
	/// destination - destinatia
	/// Returneaza 1 daca destinatia este valida, 0 altfel
	if (strlen(destination) < 3)
		return 0;
	return 1;
}

int validatePrice(float price)
{
	///	Valideaza pretul
	/// Parametrii:
	/// price - pretul
	/// Returneaza 1 daca pretul este valid, 0 altfel
	if (price < 0)
		return 0;
	return 1;
}

int validateDate(char date[]) {
    /// Valideaz? data
    /// Parametrii:
    /// date - data în format dd/mm/yyyy
    /// Returneaz? 1 dac? data este valid?, 0 altfel

    if (strlen(date) != 10) {
        return 0;
    }

    if (date[2] != '/' || date[5] != '/') {
        return 0;
    }

  
    if (date[3] == '0' && (date[4] < '1' || date[4] > '9')) {
        return 0;
    }
    if (date[3] == '1' && (date[4] < '0' || date[4] > '2')) {
        return 0;
    }




    int day = (date[0] - '0') * 10 + (date[1] - '0');
    int month = (date[3] - '0') * 10 + (date[4] - '0');


    int max_days_in_month[] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 }; // lunile de la 01 la 12


    if ((date[6] == '2' && date[7] == '0' && date[8] == '2' && date[9] == '4') || // anul 2024 sau altele bisecte
        (date[6] == '2' && date[7] == '0' && date[8] == '0' && date[9] == '0')) {
        max_days_in_month[1] = 29; 
    }


    if (day < 1 || day > max_days_in_month[month - 1]) {
        return 0;
    }

    return 1;
}
