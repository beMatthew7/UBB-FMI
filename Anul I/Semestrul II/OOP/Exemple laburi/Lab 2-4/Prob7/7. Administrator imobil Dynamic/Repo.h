#pragma once
#include "Lista.h"

// Add a new expense to the list
void Adauga(cheltuiala c, Lista* l);

// Modify an existing expense in the list
void Modifica(cheltuiala c, Lista* l);

// Delete an expense from the list by id
void Sterge(int id, Lista* l);

// Filter list by id
Lista* Filtrare1(int id, Lista* l);

// Filter list by amount
Lista* Filtrare2(int suma, Lista* l);

// Filter list by type
Lista* Filtrare3(char tip[21], Lista* l);

// Compare two expenses by amount
int cmp1(cheltuiala c1, cheltuiala c2, int mod);

// Sort list by amount
Lista* Sortare1(Lista* l, int mod);

// Compare two expenses by type
int cmp2(cheltuiala c1, cheltuiala c2, int mod);

// Sort list by type
Lista* Sortare2(Lista* l, int mod);

// Test functions
void test_Adauga();
void test_Modifica();
void test_Sterge();
void test_cmp1();
void test_cmp2();
