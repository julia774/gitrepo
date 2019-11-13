#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
def suma_parzystych():
    wynik = 0
    for i in range(0,101,2):
        print (i)
        wynik = wynik + i
    print(wynik)


def suma_nieparzystych():
    wynik = 0
    for i in range(1,100,2):
        print (i)
        wynik = wynik + i
    print(wynik)


def sumuj_wprowadzone():
    ile = int(input("ile podasz liczb?"))
    wynik = 0
    
    for i in range(ile):
        liczba = int(input("podaj liczbę:"))
        wynik = wynik + liczba
    print (wynik)


def main(args):
    # suma_parzystych():
    # suma_nieparzystych():
    sumuj_wprowadzone()



if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
