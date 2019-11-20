#!/usr/bin/env python
# -*- coding: utf-8 -*-
 


def sumuj_liczby():
    """
    Funkcja pobiera liczby od użytkownika i sumuje dopoki suma nie przekroczy wartości 75.
    """
    suma = 0
    while suma < 75:
        liczba = int(input("podaj liczbę:"))
        suma = suma + liczba
    print ("suma liczby:", suma)


def main(args):
    sumuj_liczby()



if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
