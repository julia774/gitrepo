/*
 * zliczanie.cxx
 * 
 */
#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	int a;
    int licz5 = 0;
    int licz7 = 0;
    cout <<"podaj liczbę:" << endl;
    cin >> a;
    while(a != 0) { 
        if (a % 5 == 0) {
            licz5 = licz5 + 1;
        }
        
        if (a % 7 == 0) {
            licz7 = licz7 + 1;
        }
        
        cout <<"podaj liczbę:" << endl;
        cin >> a;
    }
    cout << "podzielnych przez 5: " << licz5 << endl;
    cout << "podzielnych przez 7: " << licz7 << endl;
	return 0;
}

