#Program ma za za danie gromadzić informacje o pojazdach
programMenu = {'1': ('add', 'Dodaj samochód'), '2': ('det', 'Przeglądaj szczegóły pojazdu'),
               '3': ('del', 'Usuń pojazd'), '4': ('end', 'Zakończ program')}
#Musi zawierać:
# - element przechowujący pojazdy


# - pojazdy powinny być podzielone na typ: jednośladowe, osobowe, dostawcze, ciężarowe
vehicles = {"onetrack": [], "personal": [], "van": [], "tir": []}
# vehicle prototype:
# {"plate" :"", "color": "blue", "distancemeter": 245000}
vehicles["onetrack"].append({"plate": "AM1212", "color": "blue", "distancemeter": 245000})
vehicles["onetrack"].append({"plate": "AE1212", "color": "lightPink", "distancemeter": 75000})
vehicles["personal"].append({"plate": "DF9867", "color": "blue", "distancemeter": 430000})
vehicles["personal"].append({"plate": "ZD9878", "color": "white", "distancemeter": 100000})
vehicles["van"].append({"plate": "DR1456", "color": "green", "distancemeter": 164000})
vehicles["van"].append({"plate": "ED1221", "color": "imperial", "distancemeter": 500000})
vehicles["tir"].append({"plate": "IA6767", "color": "orange", "distancemeter": 35000})
vehicles["tir"].append({"plate": "DZ1667", "color": "violet", "distancemeter": 80000})
vehicles["van"].append({"plate": "ON1221", "color": "yellow", "distancemeter": 500000})
vehicles["onetrack"].append({"plate": "AL1212", "color": "Salomon", "distancemeter": 75000})
vehicles["tir"].append({"plate": "EL6767", "color": "salomon", "distancemeter": 35000})
print(vehicles)
# - każdy pojazd ma posiadać informacje takie jak: numer pojazdu (tablica), kolor, przebieg







# - użytkownik programu powinien mieć możliwość co najmniej dodawania przeglądania oraz usuwania pojazdu
# - program powinien działać do momentu, kiedy użytkownik nie wybierze odpowiedniej opcji w menu
zmienna = 1


def search(q, delete = False):
    retSet = set()
    while True:
        for i in vehicles:
            if i.find(q) != -1:
                if delete:
                    del vehicles[i]
                    break #ta linia "łamie pierwszą pętle, czyli FOR
                for j in vehicles[i]:
                    retSet.add(f"Pojazd typu {i}, posiadający rejestrację {j['plate']}, posiada przebieg {j['distancemeter']} i jest koloru {j['color']}")
            for j in vehicles[i]:
                for k in j:
                    if str(j[k]).lower().find(q.lower()) != -1:
                        if delete:
                            vehicles[i].remove(j)
                            break
                        retSet.add(f"Pojazd typu {i}, posiadający rejestrację {j['plate']}, posiada przebieg {j['distancemeter']} i jest koloru {j['color']}")
        else: #jeżeli w pętli for nie została wywołana instrukcja BREAK to wykona się poniższy kod
            break #ten BREAK kończy działanie pętli while
    return retSet


def delete(q):
    search(q, True)


while True:
    print('Ewidencja pojazdów')
    print('Wybierz jedną z opcji: ')
    dictKeys = list(programMenu.keys())
    dictKeys.sort()
    for i in dictKeys:
        print(f'{i}. {programMenu[i][1]}')
    match(programMenu[input('Twój wybór: ')][0]):
        case 'end': break
        case 'det':
            print(search("on"))
        case 'del':
            search("on", True)
        case other: print('Błędna opcja, wybierz jeszcze raz')
