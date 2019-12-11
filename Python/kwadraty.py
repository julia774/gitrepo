#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# kwadraty.py
import turtle 


def kwadrat(bok):
    for i in range(4):
        turtle.forward(bok)
        turtle.left(90)
    # ~turtle.forward(200)
    # ~turtle.left(90)
    # ~turtle.forward(200)
    # ~turtle.left(90)
    # ~turtle.forward(200)
    # ~turtle.left(90)


def gwiazda(bok):
    for i in range(5):
        turtle.forward(bok)
        turtle.right(144)


def gwiazdy(ile, bok, krok):

    for i in range(ile):
        print(i)
        gwiazda(bok + krok * i)


def kolo(r, ile):
    turtle.penup()
    turtle.setpos(0, -100)
    turtle.pendown()
    turtle.circle(100)
    
def kola(ile, r, krok):
    
    for i in range(ile):
        print(i)
        kolo(r, + krok * i)

def kwadraty(ile, bok, krok):

    for i in range(ile):
        print(i)
        kwadrat(bok + krok * i)

def main(args):
    turtle.setup(800, 600)
    turtle.color("green")
    turtle.pensize(2)
    # kwadraty(4, 100, 20)
    # gwiazdy(5, 100, 20)
    kola(100, 5, 20)
    turtle.done()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

