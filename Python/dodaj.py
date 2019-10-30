#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


def main(args):
    a = input("podaj liczbę:")
    b = input("podaj liczbę:")
    print("Suma:", int(a) + int(b))
    print("Witaj python!")
    

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
