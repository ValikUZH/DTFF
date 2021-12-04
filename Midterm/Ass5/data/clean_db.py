# modules start with put_
# (authentication), regularly happens

from connect import connect

cur = connect().cursor()
cur.execute('SELECT version()')

cur.execute("""SELECT * FROM animals""")
query_results = cur.fetchall()
print(query_results)

cur.execute("""DELETE FROM Animals""")
connect().commit()


cur.execute("""SELECT * FROM animals""")
query_results = cur.fetchall()
print(query_results)

cur.close()
