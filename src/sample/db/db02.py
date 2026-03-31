import psycopg2

connection = psycopg2.connect(
  database='ktsDB',
  user='postgres',
  password='pwd_kts',
  host='127.0.0.1',
  port=5432)

cur = connection.cursor()
cur.execute('SELECT * FROM m_system;')
results = cur.fetchall()

# output result
print(results)

cur.close()
connection.close()