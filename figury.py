import math


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
    wybor = input("1. Pole kwadratu\n"
                "2. Pole prostokata\n"
                 "3. Pole kola\n"
                "4. Pole trojkata\n"
                "5. Pole trapezu\n"
                "6. Koniec\n"
                )
    if wybor == '1':
        a = float(input("Podaj bok: "))
        print("Pole kwadratu =", pole_kwadratu(a))
        continue
    elif wybor == '2':
        a = float(input("Podaj bok: "))
        b = float(input("Podaj drugi bok: "))
        print("Pole prostokąta =", pole_prostokata(a, b))
        continue
    elif wybor == '3':
        r = float(input("Podaj promień: "))
        print("Pole koła =", pole_kola(r))
        continue
    elif wybor == '4':
        a = float(input("Podaj bok trójkąta: "))
        h = float(input("Podaj wysokość: "))
        print("Pole trójkąta =", pole_trojkata(a, h))
        continue
    elif wybor == '5':
        a = float(input("Podaj pierwszą podstawę: "))
        b = float(input("Podaj drugą podstawę: "))
        h = float(input("Podaj wysokość: "))
        print("Pole trapezu =", pole_trapezu(a, b, h))

    elif wybor == '6':
        print("Miłego dnia.")
        break
    else:
        print("cos nie gra")