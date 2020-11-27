from connection import connect
from get_data import get_all_movies, update_movie
from add_data_to_file import add_movie


DODAJ = 1
WYSWIETL = 2
WYSZUKAJ = 3
ZMIEN = 4
USUN = 5
KONEC = 6


menu = """
1 - dodaj film
2 - wyświetl filmy
3 - wyszukaj filmy
4 - zmien podany film
5 - usun podany film
6 - koniec pracy
"""

connection = connect()
cursor = connection.cursor()

while True:
    rozkaz = int(input(menu))
    if rozkaz == WYSWIETL:
        filmy = get_all_movies(cursor)
        for film in filmy:
            print(film)
    elif rozkaz == DODAJ:
        tytul = input("podaj tytul\n")
        opis = input("podaj opis\n")
        id = add_movie(tytul, opis, cursor)
        print(f"dodałeś film o {tytul} otrzymał id ={id[0]}")
    elif rozkaz == ZMIEN:
        id = input('Podaj id filmu do zmiany tutulu')
        new_title = input("Podaj nowy tytul filmu")
        update_movie(new_title, id, cursor)
    elif rozkaz == KONEC:
        print("ide spać")
        break
    else:
        print(rozkaz)
connection.close()