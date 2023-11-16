import json
import wypisanie


def sort_datutw_ros():
    with open('zadania.csv') as f:
        lista = []
        data = f.readline()
        while data:
            js = json.loads(data)
            lista.append(js)
            data = f.readline()
    posortowane = sorted(lista, key=lambda d: (d["datUtw"], d["godUtw"]))
    with open('zadania.csv', "w") as f:
        for i in range(len(posortowane)):
            f.write(json.dumps(posortowane[i]))
            f.write("\n")
    wypisanie.wypisanie()


def sort_datutw_mal():
    with open('zadania.csv') as f:
        lista = []
        data = f.readline()
        while data:
            js = json.loads(data)
            lista.append(js)
            data = f.readline()
    posortowane = sorted(lista, key=lambda d: (d["datUtw"], d["godUtw"]), reverse=True)
    with open('zadania.csv', "w") as f:
        for i in range(len(posortowane)):
            f.write(json.dumps(posortowane[i]))
            f.write("\n")
    wypisanie.wypisanie()


def sort_datakt_ros():
    with open('zadania.csv') as f:
        lista = []
        data = f.readline()
        while data:
            js = json.loads(data)
            lista.append(js)
            data = f.readline()
    posortowane = sorted(lista, key=lambda d: (d["datAkt"], d["godAkt"]))
    with open('zadania.csv', "w") as f:
        for i in range(len(posortowane)):
            f.write(json.dumps(posortowane[i]))
            f.write("\n")
    wypisanie.wypisanie()


def sort_datakt_mal():
    with open('zadania.csv') as f:
        lista = []
        data = f.readline()
        while data:
            js = json.loads(data)
            lista.append(js)
            data = f.readline()
    posortowane = sorted(lista, key=lambda d: (d["datAkt"], d["godAkt"]), reverse=True)
    with open('zadania.csv', "w") as f:
        for i in range(len(posortowane)):
            f.write(json.dumps(posortowane[i]))
            f.write("\n")
    wypisanie.wypisanie()
