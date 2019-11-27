#!/usr/bin/env python
# -*- coding: utf-8 -*-

#równanie.py

#Rozwiąż równaie liniowe: a + b + x = 0

#1) Pobierz wartości współczynnika a i b
#2) Jeśli a = b
        #jeśli b =0, wyprowadż "nieskończenie wiele rozwiązańń"
        #w przeciwnym wypadku wyprowadż: "równanie sprzeczne"
    #w przeciwnym wypadku oblicz x = -b / a i wyprowadż x
    
    
def main(args):
    a = int(input("Podaj a: "))
    b = int(input("Podaj b: "))
    if a == 0
        if b == 0:
            print("niekończenie wiele rozwiązań")
        else
            print("rówananie sprzeczne")
        else
            x = -b / a
            print(x)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
