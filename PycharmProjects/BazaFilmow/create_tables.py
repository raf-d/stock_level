from connection import connect

def execute_query(query):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
    connection.close()


def create_movie_table():

    query = """CREATE TABLE movie (
                id serial primary key,
                title varchar(100),
                description varchar(100)
                )
    """
    execute_query(query)

def create_cinema_table():

    query = """CREATE TABLE cinema2 (
                    id serial primary key,
                    title varchar(100),
                    description varchar(100)
                    )
        """
    execute_query(query)


if __name__ == '__main__':
    # create_movie_table()
    create_cinema_table()