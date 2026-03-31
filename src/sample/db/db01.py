# connect postgreSQL

import psycopg2

users = 'postgres'
dbnames = 'ktsDB'
passwords = 'pwd_kts'
conn = psycopg2.connect(" user=" + users + " dbname=" + dbnames + ' password=' + passwords)

# excexute sql
cur = conn.cursor()
cur.execute('SELECT * FROM m_system;')
results = cur.fetchall()

# output result
print(results)

cur.close()
conn.close()
