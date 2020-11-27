import psycopg2

connection_info = {
    'HOST': 'localhost',
    'PORT': '5432',
    'USERNAME': 'postgres',
    'PASSWORD': 'coderslab',
    'DATABASE': 'cinemas_db'
}


def connect(connection=connection_info):
    connection = psycopg2.connect(
        user = connection['USERNAME'],
        password = connection['PASSWORD'],
        host = connection['HOST'],
        port = connection['PORT'],
        dbname = connection['DATABASE']
    )
    connection.autocommit = True
    return connection


if __name__ == '__main__':
    connect()