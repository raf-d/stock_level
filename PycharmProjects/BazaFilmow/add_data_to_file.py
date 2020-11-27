from connection import connect


def add_movie(title, description, cursor):
    skowronek = f"""
    INSERT INTO movie (title, description) VALUES 
    ('{title}', '{description}') returning Id;
    """
    cursor.execute(skowronek)
    return cursor.fetchone()


if __name__ == '__main__':
    connection = connect()
    cursor = connection.cursor()
    a = add_movie("Old Hope", 'Magia w Bigosie', cursor)
    print(a)
    connection.close()