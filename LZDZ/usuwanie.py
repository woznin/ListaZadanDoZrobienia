import time
import json


def usuwanie():
    with open('zadania.csv') as f:
        lista = []
        lista2 = []
        lista3 = []
        data = f.readline()
        while data:
            js = json.loads(data)
            lista.append(js)
            data = f.readline()
    # print(lista)
    print("Wpisz date utworzenia zadania które chcesz usunąć")
    data_usun = input()
    print("Wpisz godzine utworzenia zadania które chcesz usunąć")
    godzina_usun = input()
    print("Wpisz nazwe zadania które chcesz usunąć")
    nazwa_usun = input()

    for attr in lista:
        iterator = 0
        if data_usun in attr["datUtw"]:
            iterator += 1
        if godzina_usun in attr["godUtw"]:
            iterator += 1
        if nazwa_usun in attr["nazwa"]:
            iterator += 1
        if iterator == 3:
            lista2.append(attr)
        else:
            lista3.append(attr)

    if lista3 == lista:
        print("\tNie znaleziono takiego wydarzenia! Upewnij się że format daty i godziny jest odpowiedni "
              "(rrrr-mm-dd, hh:mm)")
        print("\tAby sprawdzić nazwe zadania oraz date i godzine utworzenia sprawdź opcję 1 w menu")
        time.sleep(3)
    else:
        print(f"Usunięto zadanie {nazwa_usun} pomyślnie!")
    with open('zadania.csv', "w") as f:
        for i in range(len(lista3)):
            f.write(json.dumps(lista3[i]))
            f.write("\n")
