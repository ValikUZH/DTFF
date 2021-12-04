# provides a way to establish a connection to the database to be reused in other modules
import psycopg2
#
# conn = psycopg2.connect(
#     host="localhost",
#     port=54320,
#     database="zoo",
#     user="root",
#     password="root")
# cur = conn.cursor()
# cur.execute('SELECT version()')
#
# # display the PostgreSQL database server version
# db_version = cur.fetchone()
# print(db_version)
# cur.execute("""SELECT * FROM animals""")
# query_results = cur.fetchall()
# print(query_results)
# # close the communication with the PostgreSQL
# cur.close()


def connect():
    conn = psycopg2.connect(
    host="localhost",
    port=54320,
    database="zoo",
    user="root",
    password="root")
    conn.set_session(autocommit=True)
    return conn;