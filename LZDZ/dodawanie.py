import time
import json
import datetime


def dodawanie():
    slownik = {}
    data_god_sys = datetime.datetime.now()
    dat_utw = data_god_sys.strftime("%Y-%m-%d")
    god_utw = data_god_sys.strftime("%H:%M")
    nazwa = input("*Podaj nazwę zadania:")
    if len(nazwa) == 0:
        print("\n\tNie podano nazwy, spróbuj ponownie!")
        time.sleep(2)
        return

    dat_rel = input("*Podaj datę realizacji zadania (wpisz brak lub w formacie rrrr-mm-dd):")
    if dat_rel == "brak" or dat_rel == "Brak":
        dat_rel = dat_rel
    else:
        try:
            int(dat_rel[0]+dat_rel[1]+dat_rel[2]+dat_rel[3])
            if len(dat_rel) != 10 or dat_rel[4] != "-" or dat_rel[7] != "-" or (int(dat_rel[5] + dat_rel[6]) > 12) or (
                    int(dat_rel[8] + dat_rel[9]) > 31):
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

    god_rel = input("*Podaj godzinę realizacji zadania (wpisz brak lub w formacie gg:mm)")
    if god_rel == "brak" or god_rel == "Brak":
        god_rel = "brak"
    else:
        try:
            int(god_rel[0] + god_rel[1] + god_rel[3] + god_rel[4])
            if len(god_rel) != 5 or god_rel[2] != ":" or (int(god_rel[0] + god_rel[1]) > 23) or (
                    int(god_rel[3] + god_rel[4]) > 59):
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

    prio = input("*Podaj priorytet zadania (NO - normalny, NI - niski, WY - wysoki)")
    if prio == "NO" or prio == "NI" or prio == "WY":
        prio = prio
    else:
        print("\t\tZły format priorytetu! Spróbuj ponownie\n\n")
        time.sleep(2)
        return

    try:
        stopien = int(input("*Podaj stopień realizacji (Zakres 0-100)"))
        if 0 <= stopien <= 100:
            stopien = stopien
        else:
            print("\n\tZły zakres stopnia! Spróbuj ponownie")
            time.sleep(2)
            return
    except ValueError:
        print("\n\tStopień ma być liczbą w zakresie 0-100! Spróbuj ponownie")
        time.sleep(2)
        return

    kat = input("Podaj kategorie (np. \"praca\" lub \"hobby\")")
    opis = input("Podaj opis zadania:")

    slownik["datUtw"] = dat_utw
    slownik["godUtw"] = god_utw
    slownik["datAkt"] = dat_utw
    slownik["godAkt"] = god_utw
    slownik["nazwa"] = nazwa
    slownik["datRel"] = dat_rel
    slownik["godRel"] = god_rel
    slownik["priorytet"] = prio
    slownik["stopien"] = str(stopien)
    slownik["kategoria"] = kat
    slownik["opis"] = opis
    with open("zadania.csv", "a") as plik:
        plik.write(json.dumps(slownik))
        plik.write("\n")

    print("\n\tPomyslnie dodano nowe zadanie!\n")
    time.sleep(2)
