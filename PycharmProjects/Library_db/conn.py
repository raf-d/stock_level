import psycopg2

conn_info = {
    'HOST': 'localhost',
    'PORT': '5432',
    'USERNAME': 'postgres',
    'PASSWORD': 'coderslab',
    'DATABASE': 'library_db'
}

def connect(conn = conn_info):
    conn = psycopg2.connect(
        user=conn['USERNAME'],
        password=conn['PASSWORD'],
        host=conn['HOST'],
        port=conn['PORT'],
        dbname=['DATABASE']
    )
    conn.autocommit = True
    return conn