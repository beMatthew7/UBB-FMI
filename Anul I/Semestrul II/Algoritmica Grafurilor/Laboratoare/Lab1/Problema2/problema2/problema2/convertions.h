#pragma once
#ifndef CONVERSIONS_H
#define CONVERSIONS_H

#include <vector>

void listaToMatriceAdiacenta(int n, std::vector<int> neighbours[], bool adjacencyMatrix[100][100]);
void matriceAdiacentaToLista(int n, bool adjacencyMatrix[100][100], std::vector<int> neighbours[]);
void listaToMatriceIncidenta(int n, std::vector<int> neighbours[], bool incidenceMatrix[100][500]);
void matriceIncidentaToLista(int n, int m, bool incidenceMatrix[100][500], std::vector<int> neighbours[]);

#endif // CONVERSIONS_H
