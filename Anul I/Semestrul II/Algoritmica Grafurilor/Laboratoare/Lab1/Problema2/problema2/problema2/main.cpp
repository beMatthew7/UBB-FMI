#include <fstream>
#include <vector>
#include <iostream>
#include <stack>
#include "convertions.h"

using namespace std;
bool adjacencyMatrix[100][100];
bool incidenceMatrix[100][500];
int dist[100][100];
vector <int> neighbours[100];
int n, m = 0;

void readAdiacenta() {
    ifstream fin("graph.txt");
    fin >> n;
    int x, y;
    while (fin >> x >> y) {
        adjacencyMatrix[x][y] = true;
        adjacencyMatrix[y][x] = true;
    }
    cout << "Matrice adiacenta: \n";
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cout << adjacencyMatrix[i][j];
        }
        cout << '\n';
    }
    fin.close();
}

void readIncidenta() {
    ifstream fin("graph.txt");
    fin >> n;
    int x, y;
    int muchie = 0;
    while (fin >> x >> y) {
        incidenceMatrix[x][muchie] = incidenceMatrix[y][muchie] = true;
        muchie++;
    }
    cout << "Matrice incidenta: \n";
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < muchie; j++) {
            cout << incidenceMatrix[i][j];
        }
        cout << '\n';
    }
    fin.close();
}

void readListaAdiacenta() {
    ifstream fin("graph.txt");
    fin >> n;
    int x, y;
    while (fin >> x >> y) {
        neighbours[x].push_back(y);
        neighbours[y].push_back(x);
        m++;
    }
    cout << "Lista adiacenta: \n";
    for (int i = 1; i <= n; i++) {
        for (auto vecin : neighbours[i]) {
            cout << vecin << ' ';
        }
        cout << '\n';
    }
    fin.close();
}

void noduriIsolate() {
    ///gasirea nodurilor izolate in graf
    /// return: -
    bool foundIsolated = false;
    for (int i = 1; i <= n; i++) {
        if (neighbours[i].empty()) {
            cout << "Nodul " << i << " este izolat\n";
            foundIsolated = true;
        }
    }
    if (!foundIsolated) {
        cout << "Nu exista noduri izolate\n";
    }
    cout << '\n';
}

void grafRegular() {
    ///verificare daca graful este regular
    ///return: -
    int degree = neighbours[1].size();
    bool regular = true;
    for (int i = 2; i <= n; i++) {
        if (neighbours[i].size() != degree) {
            regular = false;
            break;
        }
    }
    if (regular) {
        cout << "Graful este regular\n";
    }
    else {
        cout << "Graful nu este regular\n";
    }
}

void matriceaDistantelor()
{
    //Initializarea matricei distantelor
    for (int i = 1; i <= n; i++)
    {
        for(int j = 1; j<= n; j++)
        {
			if (i == j)
			{
				dist[i][j] = 0;
			}
			else if (adjacencyMatrix[i][j] == true)
			{
				dist[i][j] = 1;
			}
			else
			{
				dist[i][j] = 99999;
			}
        }
    }
    //Algoritmul Floyd-Warshall
    for (int k = 1; k <= n; k++)
    {
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                if (dist[i][k] + dist[k][j] < dist[i][j])
                {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }

	//Afisarea matricei distantelor
    cout << "Matricea distantelor este: \n";
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (dist[i][j] == 99999) {
                std::cout << "INF ";
            }
            else {
                std::cout << dist[i][j] << " ";
            }
        }
        std::cout << '\n';
    }
}

void isConex() {
    // Verificăm dacă graful este conex folosind DFS
    vector<bool> visited(n + 1, false);
    stack<int> s;
    s.push(1);
    visited[1] = true;
    int count = 1;

    while (!s.empty()) {
        int node = s.top();
        s.pop();
        for (int i = 1; i <= n; i++) {
            if (adjacencyMatrix[node][i] && !visited[i]) {
                visited[i] = true;
                s.push(i);
                count++;
            }
        }
    }

    if (count == n) {
        cout << "Graful este conex\n";
    }
    else {
        cout << "Graful nu este conex\n";
    }
}


int main() {

    //readAdiacenta();
    //readIncidenta();
    readListaAdiacenta();
	noduriIsolate();
	grafRegular();

    //transformare lista de adiacenta in matrice de adiacenta
    listaToMatriceAdiacenta(n, neighbours, adjacencyMatrix);

    // Calcularea matricei distanțelor folosind algoritmul Floyd-Warshall
    matriceaDistantelor();

    // Verificarea dacă graful este conex
    isConex();





    return 0;
}