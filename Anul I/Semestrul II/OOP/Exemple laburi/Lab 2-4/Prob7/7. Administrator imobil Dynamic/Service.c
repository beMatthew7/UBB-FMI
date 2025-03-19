#include "Service.h"
#include <assert.h>

void addCheltuiala(int id, int suma, char tip[21], Lista* l) {
    cheltuiala c;
    c.id = id;
    c.suma = suma;
    strcpy_s(c.tip, 20, tip);
    Adauga(c, l);
}

void updateCheltuiala(int id, int suma, char tip[21], Lista* l) {
    cheltuiala c;
    c.id = id;
    c.suma = suma;
    strcpy_s(c.tip, 20, tip);
    Modifica(c, l);
}

void deleteCheltuiala(int id, Lista* l) {
    Sterge(id, l);
}

Lista* filterCheltuiala(int criteriu, int valoare, char tip[21], Lista* l) {
    if (criteriu == 1)
        return Filtrare1(valoare, l);
    if (criteriu == 2)
        return Filtrare2(valoare, l);
    if (criteriu == 3)
        return Filtrare3(tip, l);
    return NULL;
}

Lista* sortCheltuiala(int criteriu, int mod, Lista* l) {
    if (criteriu == 1)
        return Sortare1(l, mod);
    if (criteriu == 2)
        return Sortare2(l, mod);
    return NULL;
}

void test_addCheltuiala() {
    Lista* l = createList(10);
    addCheltuiala(1, 100, "apa", l);
    assert(l->len == 1);
    assert(l->array[0].id == 1);
    assert(l->array[0].suma == 100);
    assert(strcmp(l->array[0].tip, "apa") == 0);
    destroyList(l);
}

void test_updateCheltuiala() {
    Lista* l = createList(10);
    addCheltuiala(1, 100, "apa", l);
    updateCheltuiala(1, 200, "gaz", l);
    assert(l->len == 1);
    assert(l->array[0].id == 1);
    assert(l->array[0].suma == 200);
    assert(strcmp(l->array[0].tip, "gaz") == 0);
    destroyList(l);
}

void test_deleteCheltuiala() {
    Lista* l = createList(10);
    addCheltuiala(1, 100, "apa", l);
    deleteCheltuiala(1, l);
    assert(l->len == 0);
    destroyList(l);
}

void test_filterCheltuiala() {
    Lista* l = createList(10);
    addCheltuiala(1, 100, "apa", l);
    addCheltuiala(2, 200, "gaz", l);
    addCheltuiala(3, 100, "internet", l);
    
    // Filter by id
    Lista* result1 = filterCheltuiala(1, 1, "", l);
    assert(result1->len == 1);
    assert(result1->array[0].id == 1);
    destroyList(result1);
    
    // Filter by suma
    Lista* result2 = filterCheltuiala(2, 100, "", l);
    assert(result2->len == 2);
    destroyList(result2);
    
    // Filter by tip
    Lista* result3 = filterCheltuiala(3, 0, "apa", l);
    assert(result3->len == 1);
    assert(strcmp(result3->array[0].tip, "apa") == 0);
    destroyList(result3);
    
    destroyList(l);
}

void test_sortCheltuiala() {
    Lista* l = createList(10);
    addCheltuiala(1, 300, "apa", l);
    addCheltuiala(2, 100, "gaz", l);
    addCheltuiala(3, 200, "internet", l);
    
    // Sort by suma ascending
    Lista* result1 = sortCheltuiala(1, 1, l);
    assert(result1->array[0].suma == 100);
    assert(result1->array[1].suma == 200);
    assert(result1->array[2].suma == 300);
    destroyList(result1);
    
    // Sort by tip ascending
    Lista* result2 = sortCheltuiala(2, 1, l);
    assert(strcmp(result2->array[0].tip, "apa") == 0);
    assert(strcmp(result2->array[1].tip, "gaz") == 0);
    assert(strcmp(result2->array[2].tip, "internet") == 0);
    destroyList(result2);
    
    destroyList(l);
}
