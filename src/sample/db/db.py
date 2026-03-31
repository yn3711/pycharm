import os
import psycopg2

def get_connection():

    #dsn = os.environ.get('postgresql://{postgres}:{pwd_kts}@{localhost}:{5432}/{ktsDB}')
    #return psycopg2.connect(dsn)

    #dsn = os.environ.get('postgresql: // postgres: pwd_kts @ localhost:5432 / ktsDB')
    #return psycopg2.connect(dsn)

    #return psycopg2.connect(host="127.0.0.1", dbname="ktsDB", user="postgres", password="pwd_kts", port="5432")

    return psycopg2.connect("host=" + "localhost" +
                           " port=" + "5432" +
                           " dbname=" + "ktsDB" +
                           " user=" + "postgres" +
                           " password=" + "pwd_kts")


conn = get_connection()

cur = conn.cursor()
cur.execute('SELECT * FROM m_system;')
results = cur.fetchall()

#cur = conn.cursor()
#cur.execute('SELECT * FROM m_system;')

print(results)
cur.close()
conn.close()