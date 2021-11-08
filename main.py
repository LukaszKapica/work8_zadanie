uczniowie = []
uczniowie_sl = {}
klasy = {}
wychowawcy = []
wychowawcy_sl = {}
nauczyciele_sl = {}
while True:
    akcja = input()
    if akcja == 'koniec':
        break
    if akcja == 'uczen':
        name = input()
        klasa = input()
        uczniowie_sl[name] = klasa

        if not klasa in klasy.keys():
            # klasy[klasa] = []
            klasy[klasa] = {}
            # if not uczniowie in klasy[klasa].keys(): ??
        # klasy[klasa].append(name)
            klasy[klasa]['uczniowie'] = []
            klasy[klasa]['wychowawca'] = []
        klasy[klasa]['uczniowie'].append(name)
    if akcja == 'wychowawca':
        name = input()
        # wychowawcy.append(name)
        if not name in wychowawcy_sl.keys():
            wychowawcy_sl[name] = []
        while True:
            klasa = input()
            if not klasa:
                break
            wychowawcy_sl[name].append(klasa)
            if not klasa in klasy.keys():
                # klasy[klasa] = []
                klasy[klasa] = {}
                # if not uczniowie in klasy[klasa].keys(): ??
                # klasy[klasa].append(name)
                klasy[klasa]['uczniowie'] = []
                klasy[klasa]['wychowawca'] = []
            klasy[klasa]['wychowawca'].append(name)


    if akcja == 'nauczyciel':
        name = input()
        naucza = input()
        # nauczyciele_sl[naucza] = 'przedmiot'
        nauczyciele_sl[name] = {}
        nauczyciele_sl[name]['klasy'] = []
        nauczyciele_sl[name]['przedmiot'] = naucza
        while True:
            klasa = input()
            if not klasa:
                break
            nauczyciele_sl[name]['klasy'].append(klasa)


# print(uczniowie)
# print(uczniowie_sl)
# print(klasy)
# print(klasy.values())
# print(wychowawcy)
# print(wychowawcy_sl)
# print(wychowawcy_sl.values())
# print(nauczyciele_sl)


import sys
akcja = sys.argv[1]
if len(akcja) <= 2:
    print(klasy[akcja])
elif akcja in wychowawcy_sl.keys():
    klasy_wychowawcy = wychowawcy_sl[akcja]
    for kl in klasy_wychowawcy:
        print(klasy[kl]['uczniowie'])
elif akcja in nauczyciele_sl.keys():
    sl_nauczyciel = nauczyciele_sl[akcja]
    # print(sl_nauczyciel['klasy'])
    for kl in sl_nauczyciel['klasy']:
        print(klasy[kl]['wychowawca'])
elif akcja in uczniowie_sl.keys():
    klasa_ucznia = uczniowie_sl[akcja]
    for klucz, wartosc in nauczyciele_sl.items():
        # print(wartosc)
        for k, v in wartosc.items():
            # print(v)
            if klasa_ucznia in v:
                print(klucz, nauczyciele_sl[klucz]['przedmiot'])
else:
    print('Błędna nazwa')

