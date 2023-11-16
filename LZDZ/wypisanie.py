import time
import json


def wypisanie():
    with open('zadania.csv') as plik:
        data = plik.readline()
        numer = 1
        while data:
            js = json.loads(data)
            print(f'Zadanie: {js["nazwa"]}')
            print(f'Data i godzina utworzenia: {js["datUtw"]} {js["godUtw"]}')
            print(f'Data i godzina ostatniej aktualizacji: {js["datAkt"]} {js["godAkt"]}')
            print(f'Termin (data): {js["datRel"]}, Termin(godzina) {js["godRel"]}, Priorytet:'
                  f' {js["priorytet"]}, Stopien wykonania: {js["stopien"]}, Kategoria: {js["kategoria"]}, '
                  f'Opis: {js["opis"]} \n')
            data = plik.readline()
            numer += 1
    time.sleep(2)
