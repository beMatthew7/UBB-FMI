#include <iostream>
#include <fstream>
#include <vector>


using namespace std;

void listaToMatriceAdiacenta(int n, vector<int> neighbours[], bool adjacencyMatrix[100][100]) {
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            adjacencyMatrix[i][j] = false;

    for (int i = 1; i <= n; i++) {
        for (int vecin : neighbours[i]) {
            adjacencyMatrix[i][vecin] = true;
        }
    }
    cout << "Lista transformata în matrice de adiacenta:\n";
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++)
            cout << adjacencyMatrix[i][j] << " ";
        cout << '\n';
    }
}

void matriceAdiacentaToLista(int n, bool adjacencyMatrix[100][100], vector<int> neighbours[]) {
    for (int i = 1; i <= n; i++)
        neighbours[i].clear();

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (adjacencyMatrix[i][j]) {
                neighbours[i].push_back(j);
            }
        }
    }
    cout << "Matrice transformata in lista de adiacenta:\n";
    for (int i = 1; i <= n; i++) {
        for (int vecin : neighbours[i])
            cout << vecin << ' ';
        cout << '\n';
    }
}

void listaToMatriceIncidenta(int n, vector<int> neighbours[], bool incidenceMatrix[100][500]) {
    for (int i = 1; i <= n; i++)
        for (int j = 0; j < 500; j++)
            incidenceMatrix[i][j] = false;

    int muchie = 0;
    for (int i = 1; i <= n; i++) {
        for (int vecin : neighbours[i]) {
            if (i < vecin) {
                incidenceMatrix[i][muchie] = true;
                incidenceMatrix[vecin][muchie] = true;
                muchie++;
            }
        }
    }
    cout << "Lista transformata in matrice de incidenta:\n";
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < muchie; j++)
            cout << incidenceMatrix[i][j] << ' ';
        cout << '\n';
    }
}

void matriceIncidentaToLista(int n, int m, bool incidenceMatrix[100][500], vector<int> neighbours[]) {
    for (int i = 1; i <= n; i++)
        neighbours[i].clear();

    for (int j = 0; j < m; j++) {
        int x = -1, y = -1;
        for (int i = 1; i <= n; i++) {
            if (incidenceMatrix[i][j]) {
                if (x == -1) x = i;
                else y = i;
            }
        }

        neighbours[x].push_back(y);
        neighbours[y].push_back(x);
    }
    cout << "Matricea de incidenta transformata în lista de adiacenta:\n";
    for (int i = 1; i <= n; i++) {
        for (int vecin : neighbours[i])
            cout << vecin << ' ';
        cout << '\n';
    }
}
