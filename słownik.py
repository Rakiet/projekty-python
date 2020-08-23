
from enum import IntEnum
dictionary = {'nabab': 'bardzo bogaty czlowiek',
              'nimfomanka': 'chorobliwy stan nadmiernego pobudzenia erotycznego u kobiet',
              'knajak': 'człowiek z marginesu spolecznego'}
Menu_Dictionary = IntEnum("Menu_Dictionary", "Dodaj Wyszukaj Usun Wyswietl_All Koniec")

while(True):


    choice = int(input("1. Dodaj definicje \n"
                    "2. Wyszukac definicje \n"
                    "3. Usunąc definicje\n"
                    "4. Wyświetl wszystko\n"
                    "5. Koniec\n"))





    if choice == Menu_Dictionary.Dodaj:
        word = input("Podaj slowo: ")
        importance = input("Podaj definicje: ")
        if (word != '') and (importance != ''):
            dictionary[word] = importance
            print('Zapisano :)')
        else:
            print('coś poszło nie tak, może sie poprawisz :)')
        continue

    elif choice == Menu_Dictionary.Wyszukaj:
        searches = input("Podaj szukane slowo: ")
        importance = dictionary.get(searches)


        if importance:
            print("Definicja slowa:", searches, "to: '", importance ,"'\n\n\nKONIEC KODU")
        else:
            print("Niestety nie ma jeszcze definicji do słowa:", searches,"\nMoże zechcesz ją dodać :)")
        continue

    elif choice == Menu_Dictionary.Usun:
        delWord = input("Podaj definicje która ma zostać usunięta: ")
        delDictionary = dictionary.get(delWord)

        if delDictionary:
            dictionary.pop(delWord)
            print("usunięto")
        else:
            print("Niestety nie można usunąć, czegoś, czego nie ma")
        continue

    elif choice == Menu_Dictionary.Wyswietl_All:
        for i in dictionary:
            print("Definicja slowa '", i, "' to:\n       ", dictionary[i], '\n')
        continue

    elif choice == Menu_Dictionary.Koniec:
        print("dziekuje, miłego dnia")
        break

    else:
        print("Błąd")
