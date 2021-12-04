# modules start with get_
# can be time consuming -> memoization
from connect import connect

cur = connect().cursor()
cur.execute('SELECT version()')

cur.execute("""SELECT * FROM animals""")
query_results = cur.fetchall()
print(query_results)
cur.close()
