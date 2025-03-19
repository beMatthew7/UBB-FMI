#pragma once
#include "Repo.h"

// Add a new expense
void addCheltuiala(int id, int suma, char tip[21], Lista* l);

// Modify an existing expense
void updateCheltuiala(int id, int suma, char tip[21], Lista* l);

// Delete an expense
void deleteCheltuiala(int id, Lista* l);

// Filter expenses
Lista* filterCheltuiala(int criteriu, int valoare, char tip[21], Lista* l);

// Sort expenses
Lista* sortCheltuiala(int criteriu, int mod, Lista* l);

// Test functions
void test_addCheltuiala();
void test_updateCheltuiala();
void test_deleteCheltuiala();
void test_filterCheltuiala();
void test_sortCheltuiala();
