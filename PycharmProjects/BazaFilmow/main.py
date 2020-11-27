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


def wyswietl_wszystkie_filmy():
    connection = connect()
    cursor = connection.cursor()
    filmy = get_all_movies(cursor)
    for film in filmy:
        print(film)
    connection.close()


def dodaj_film(title, description):
    connection = connect()
    cursor = connection.cursor()
    film = add_movie(title, desription, cursor)

connection = connect()
cursor = connection.cursor()

while True:
    rozkaz = int(input(menu))
    if rozkaz == WYSWIETL:
        wyswietl_wszystkie_filmy()
    elif rozkaz == DODAJ:
        tytul = input
        dodaj_film()
    elif rozkaz == ZMIEN:
        id = input('Podaj id filmu do zmiany tutulu')
        new_title = input("Podaj nowy tytul filmu")
        update_movie(new_title, id, cursor)
    elif rozkaz == KONEC:
        print("ide spać")
        break
    else:
        print(rozkaz)