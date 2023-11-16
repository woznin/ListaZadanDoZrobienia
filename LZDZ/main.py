import time
import menu
import wypisanie
import dodawanie
import usuwanie
import operacje1_3
import sortowanie


# wybor uzytkownika
def main():
    menu.wyswietl_menu()
    wybor = input()
    if wybor == "1":
        wypisanie.wypisanie()
        main()
    elif wybor == "2":
        print("Podaj informacje o nowym zadaniu (* - dane obowiązkowe)")
        dodawanie.dodawanie()
        main()
    elif wybor == "3":
        usuwanie.usuwanie()
        main()
    elif wybor == "4":
        menu.wyswietl_menu2()
        wybor2 = input()
        if wybor2 == "1":
            operacje1_3.zmianaprio()
        elif wybor2 == "2":
            operacje1_3.zmianadaty()
        elif wybor2 == "3":
            operacje1_3.zmianastopien()
        elif wybor2 == "4":
            sortowanie.sort_datutw_ros()
        elif wybor2 == "5":
            sortowanie.sort_datutw_mal()
        elif wybor2 == "6":
            sortowanie.sort_datakt_ros()
        elif wybor2 == "7":
            sortowanie.sort_datakt_mal()
        elif wybor2 == "8":
            main()
            return
        else:
            print("\tWybrano nieprawidłową opcje menu")
            time.sleep(1)
            main()
            return
        main()
    elif wybor == "5":
        print("Pomyślnie zakończono działanie programu")
        exit(0)
    else:
        print("\tWybrano nieprawidłową opcje menu")
        time.sleep(1)
        main()


main()
