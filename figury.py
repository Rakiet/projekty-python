import math
from enum import IntEnum

def pole_kwadratu(a):
    return a * a


def pole_prostokata(a, b):
    return a * b


def pole_kola(r):
    return math.pi * r ** 2


def pole_trojkata(a, h):
    return 0.5 * a * h


def pole_trapezu(a, b, h):
    return (a + b) / 2 * h

while(True):

    Menu_Figury = IntEnum("Menu_Figury", "Kwadrat Prostokat Kolo Trojkat Trapez Koniec")
    wybor = int(input("""1. Pole kwadratu
2. Pole prostokata
3. Pole kola
4. Pole trojkata
5. Pole trapezu
6. Koniec
"""))
    if wybor == Menu_Figury.Kwadrat:
        a = float(input("Podaj bok: "))
        print("Pole kwadratu =", pole_kwadratu(a))
        continue
    elif wybor == Menu_Figury.Prostokat:
        a = float(input("Podaj bok: "))
        b = float(input("Podaj drugi bok: "))
        print("Pole prostokąta =", pole_prostokata(a, b))
        continue
    elif wybor == Menu_Figury.Kolo:
        r = float(input("Podaj promień: "))
        print("Pole koła =", pole_kola(r))
        continue
    elif wybor == Menu_Figury.Trojkat:
        a = float(input("Podaj bok trójkąta: "))
        h = float(input("Podaj wysokość: "))
        print("Pole trójkąta =", pole_trojkata(a, h))
        continue
    elif wybor == Menu_Figury.Trapez:
        a = float(input("Podaj pierwszą podstawę: "))
        b = float(input("Podaj drugą podstawę: "))
        h = float(input("Podaj wysokość: "))
        print("Pole trapezu =", pole_trapezu(a, b, h))

    elif wybor == Menu_Figury.Koniec:
        print("Miłego dnia.")
        break
    else:
        print("cos nie gra")