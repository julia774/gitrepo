#!/usr/bin/env python
# -*- coding: utf-8 -*-





    # if a < 0 or b < 0 or >= b:
    #   print("błędne dane!")
    #   return
    # if a < b or a == b :
    # if a <= b:
    #   print("błędne dane!")
    #   return 




def sumuj_parzyste(a, b):
    suma = 0
    for liczba in range(a, b + 1):
        if liczba %  2 == 0:
            suma = suma + liczba
    print(suma)


def sumuj_nieparzyste(a, b):
    suma = 0
    for liczba in range(a, b + 1):
        if liczba %  2 == 1:
            suma = suma + liczba
    print(suma)


def main(args):
    a = b = -1
    while a < 0:
        a = int(input("podaj 1 liczbę:"))

    while a >= b:
        b = int(input("podaj 2 liczbę:"))

    sumuj_parzyste(a, b)
    sumuj_nieparzyste(a, b)

    return 0




if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
