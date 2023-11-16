import json
import time
import datetime

data_god_sys = datetime.datetime.now()


def zmianaprio():
    with open('zadania.csv') as f:
        lista = []
        lista2 = []
        data = f.readline()
        while data:
            js = json.loads(data)
            lista.append(js)
            data = f.readline()
    dlugosc = len(lista)
    czy_jest = 0
    data_zmien = input("Wpisz date utworzenia zadania którego priorytet chcesz zmienić")
    godzina_zmien = input("Wpisz godzine utworzenia zadania którego priorytet chcesz zmienić")
    nazwa_zmien = input("Wpisz nazwe zadania którego priorytet chcesz zmienić")
    for attr in lista:
        iterator = 0
        if data_zmien in attr["datUtw"]:
            iterator += 1
        if godzina_zmien in attr["godUtw"]:
            iterator += 1
        if nazwa_zmien in attr["nazwa"]:
            iterator += 1
        if iterator == 3:
            nowy_priorytet = input("Podaj wartość priorytetu na jaki chcesz zmienić (NI-niski, NO-normalny, WY-wysoki")
            if nowy_priorytet == "NO" or nowy_priorytet == "NI" or nowy_priorytet == "WY":
                attr["priorytet"] = nowy_priorytet
                attr["datAkt"] = data_god_sys.strftime("%Y-%m-%d")
                attr["godAkt"] = data_god_sys.strftime("%H:%M")
                lista2.append(attr)
            else:
                print("\t\tZły format priorytetu! Spróbuj ponownie\n\n")
                time.sleep(2)
                return
        else:
            lista2.append(attr)
            czy_jest += 1
    if czy_jest == dlugosc:
        print("\n\tNie znaleziono takiego zadania! Spróbuj ponownie")
        time.sleep(2)
    else:
        print("\n\tPrawidłowo zmieniono priorytet zadania!")
        time.sleep(2)
    with open('zadania.csv', "w") as f:
        for i in range(len(lista2)):
            f.write(json.dumps(lista2[i]))
            f.write("\n")


def zmianadaty():
    with open('zadania.csv') as f:
        lista = []
        lista2 = []
        data = f.readline()
        while data:
            js = json.loads(data)
            lista.append(js)
            data = f.readline()
    dlugosc = len(lista)
    czy_jest = 0
    data_zmien = input("Wpisz date utworzenia zadania którego date i godzine realizacji chcesz zmienić")
    godzina_zmien = input("Wpisz godzine utworzenia zadania którego date i godzine realizacji chcesz zmienić")
    nazwa_zmien = input("Wpisz nazwe zadania którego date i godzine chcesz zmienić")
    for attr in lista:
        iterator = 0
        if data_zmien in attr["datUtw"]:
            iterator += 1
        if godzina_zmien in attr["godUtw"]:
            iterator += 1
        if nazwa_zmien in attr["nazwa"]:
            iterator += 1
        if iterator == 3:

            dat_rel_nowa = input("*Podaj nową datę realizacji zadania (wpisz brak lub w formacie rrrr-mm-dd):")
            if dat_rel_nowa == "brak" or dat_rel_nowa == "Brak":
                dat_rel_nowa = dat_rel_nowa
            else:
                try:
                    int(dat_rel_nowa[0] + dat_rel_nowa[1] + dat_rel_nowa[2] + dat_rel_nowa[3])
                    if len(dat_rel_nowa) != 10 or dat_rel_nowa[4] != "-" or dat_rel_nowa[7] != "-" or (
                            int(dat_rel_nowa[5] + dat_rel_nowa[6]) > 12) or (
                            int(dat_rel_nowa[8] + dat_rel_nowa[9]) > 31):
                        print("\n\tData w złym formacie, spróbuj ponownie! \n\t\t(prawidłowy format: rrrr-mm-dd)")
                        time.sleep(2)
                        return
                except ValueError:
                    print("\n\tData w złym formacie, spróbuj ponownie! \n\t\t(prawidłowy format: rrrr-mm-dd)")
                    time.sleep(2)
                    return
                except IndexError:
                    print("\n\tData w złym formacie, spróbuj ponownie! \n\t\t (prawidłowy format: rrrr-mm-dd)")
                    time.sleep(2)
                    return

            god_rel_n = input("*Podaj godzinę realizacji zadania (wpisz brak lub w formacie gg:mm)")
            if god_rel_n == "brak" or god_rel_n == "Brak":
                god_rel_n = "brak"
            else:
                try:
                    int(god_rel_n[0] + god_rel_n[1] + god_rel_n[3] + god_rel_n[4])
                    if len(god_rel_n) != 5 or god_rel_n[2] != ":" or (int(god_rel_n[0] + god_rel_n[1]) > 23) or (
                            int(god_rel_n[3] + god_rel_n[4]) > 59):
                        print("\n\tGodzina w złym formacie, spróbuj ponownie! \n\t\t(prawidłowy format: gg:mm)")
                        time.sleep(2)
                        return
                except ValueError:
                    print("\n\tGodzina w złym formacie, spróbuj ponownie! \n\t\t(prawidłowy format: gg:mm)")
                    time.sleep(2)
                    return
                except IndexError:
                    print("\n\tGodzina w złym formacie, spróbuj ponownie! \n\t\t (prawidłowy format: gg:mm)")
                    time.sleep(2)
                    return

            attr["datRel"] = dat_rel_nowa
            attr["godRel"] = god_rel_n
            attr["datAkt"] = data_god_sys.strftime("%Y-%m-%d")
            attr["godAkt"] = data_god_sys.strftime("%H:%M")
            lista2.append(attr)
        else:
            lista2.append(attr)
            czy_jest += 1
    if czy_jest == dlugosc:
        print("\n\tNie znaleziono takiego zadania! Spróbuj ponownie")
        time.sleep(2)
    else:
        print("\n\tPrawidłowo zmieniono date zadania!")
        time.sleep(2)

    with open('zadania.csv', "w") as f:
        for i in range(len(lista2)):
            f.write(json.dumps(lista2[i]))
            f.write("\n")


def zmianastopien():
    with open('zadania.csv') as f:
        lista = []
        lista2 = []
        data = f.readline()
        while data:
            js = json.loads(data)
            lista.append(js)
            data = f.readline()

    dlugosc = len(lista)
    czy_jest = 0
    data_zmien = input("Wpisz date utworzenia zadania którego stopień chcesz zmienić")
    godzina_zmien = input("Wpisz godzine utworzenia zadania którego stopień chcesz zmienić")
    nazwa_zmien = input("Wpisz nazwe zadania którego stopień chcesz zmienić")
    for attr in lista:
        iterator = 0
        if data_zmien in attr["datUtw"]:
            iterator += 1
        if godzina_zmien in attr["godUtw"]:
            iterator += 1
        if nazwa_zmien in attr["nazwa"]:
            iterator += 1
        if iterator == 3:
            stopien_nowa = int(input("Wpisz nowy stopień zadania (zakres 0-100)"))
            if 0 <= stopien_nowa <= 100:
                stopien_nowa = stopien_nowa
            else:
                print("\n\tZły zakres stopnia! Spróbuj ponownie")
                time.sleep(2)
                return
            attr["stopien"] = str(stopien_nowa)
            attr["datAkt"] = data_god_sys.strftime("%Y-%m-%d")
            attr["godAkt"] = data_god_sys.strftime("%H:%M")
            lista2.append(attr)
        else:
            lista2.append(attr)
            czy_jest += 1

    if czy_jest == dlugosc:
        print("\n\tNie znaleziono takiego zadania! Spróbuj ponownie")
        time.sleep(2)
    else:
        print("\n\tPrawidłowo zmieniono stopień zadania!")
        time.sleep(2)

    with open('zadania.csv', "w") as f:
        for i in range(len(lista2)):
            f.write(json.dumps(lista2[i]))
            f.write("\n")
