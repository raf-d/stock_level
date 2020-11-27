from connection import connect


def get_all_movies(cursor):
    sikorka = f"""
    SELECT * FROM movies;
    """
    cursor.execute(sikorka)
    return cursor.fetchall() # przy fetchone wskaże tylko jedną pozycję

def update_movie(new_title, id, cursor):
    query = f"""
    UPDATE movies SET name = '{new_title}' WHERE id = {id}
    """
    cursor.execute(query)
    return cursor

if __name__ == '__main__':
    connection = connect()
    cursor = connection.cursor()
    filmy = get_all_movies(cursor)
    for film in filmy:
        print(film)
    connection.close()