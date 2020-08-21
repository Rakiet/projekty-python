

dictionary = {'nabab': 'bardzo bogaty czlowiek',
              'nimfomanka': 'chorobliwy stan nadmiernego pobudzenia erotycznego u kobiet',
              'knajak': 'człowiek z marginesu spolecznego'}

def start(firstTorF):

    if firstTorF:
        choiceInput = input("Witam w słowniku, co chcesz dzisiaj robić?\n"
                    "1. Dodaj definicje \n"
                    "2. Wyszukac definicje \n"
                    "3. Usunąc definicje\n"
                    "4. Wyświetl wszystko\n"
                    "5. Koniec\n")
    else:
        choiceInput = input("Witam ponownie, dokonaj wyboru.\n"
                    "1. Dodaj definicje \n"
                    "2. Wyszukac definicje \n"
                    "3. Usunąc definicje\n"
                    "4. Wyświetl wszystko\n"
                    "5. Koniec\n")
    choice(choiceInput)

def choice(choice):
    if choice == '1':
        word = input("Podaj slowo: ")
        importance = input("Podaj definicje: ")
        if (word != '') and (importance != ''):
            dictionary[word] = importance
            print('Zapisano :)')
        else:
            print('coś poszło nie tak, może sie poprawisz :)')
        start(False)

    elif choice == '2':
        searches = input("Podaj szukane slowo: ")
        importance = dictionary.get(searches)


        if importance:
            print("Definicja slowa:", searches, "to: '", importance ,"'\n\n\nKONIEC KODU")
        else:
            print("Niestety nie ma jeszcze definicji do słowa:", searches,"\nMoże zechcesz ją dodać :)")
        start(False)

    elif choice == '3':
        delWord = input("Podaj definicje która ma zostać usunięta: ")
        delDictionary = dictionary.get(delWord)

        if delDictionary:
            dictionary.pop(delWord)
            print("usunięto")
        else:
            print("Niestety nie można usunąć, czegoś, czego nie ma")
        start(False)

    elif choice == '4':
        for i in dictionary:
            print("Definicja slowa '", i, "' to:\n       ", dictionary[i], '\n')
        start(False)

    elif choice == '5':
        print("dziekuje, miłego dnia")

    else:
        print("Błąd")
        start(False)



start(True)
