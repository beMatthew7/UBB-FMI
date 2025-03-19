#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

ifstream fin("in.txt");
bool adjacencyMatrix[100][100];
bool incidenceMatrix[100][500];
vector <int> neighbours[100];
int n, m = 0;
void readListaAdiacenta() {
    fin >> n;
    int x, y;
    while (fin >> x >> y) {
        neighbours[x].push_back(y);
        neighbours[y].push_back(x);
        m++;   
    }
    cout << "Lista adiacenta: \n";
    for (int i=1; i <= n; i++) {
        for (auto vecin : neighbours[i]) {
            cout << vecin << ' ';
        }
        cout << '\n';
    }
    fin.close();
}
void listaToMatriceAdiacenta(int n) {

    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            adjacencyMatrix[i][j] = false;

    for (int i = 1; i <= n; i++) {
        for (int vecin : neighbours[i]) {
            adjacencyMatrix[i][vecin] = true;
        }
    }
    cout << "Lista transformată în matrice de adiacență:\n";
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++)
            cout << adjacencyMatrix[i][j] << " ";
        cout << '\n';
    }
}

void matriceAdiacentaToLista(int n) {
    for (int i = 1; i <= n; i++)
        neighbours[i].clear();

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (adjacencyMatrix[i][j]) {
                neighbours[i].push_back(j);
            }
        }
    }
    cout << "Matrice transformată în lista de adiacență:\n";
    for (int i = 1; i <= n; i++) {
        for (int vecin : neighbours[i])
            cout << vecin << ' ';
        cout << '\n';
    }
}
void listaToMatriceIncidenta(int n) {
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
    cout << "Lista transformată în matrice de incidență:\n";
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < muchie; j++)
            cout << incidenceMatrix[i][j] << ' ';
        cout << '\n';
    }
}
void matriceIncidentaToLista(int n, int m) {
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
    cout << "Matricea de incidență transformată în lista de adiacență:\n";
    for (int i = 1; i <= n; i++) {
        for (int vecin : neighbours[i])
            cout << vecin << ' ';
        cout << '\n';
    }
}





int main()
{
    readListaAdiacenta();
    listaToMatriceAdiacenta(n);
    matriceAdiacentaToLista(n);
    listaToMatriceIncidenta(n);
    matriceIncidentaToLista(n,m);
    return 0;


}