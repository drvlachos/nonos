import sqlite3

conn = sqlite3.connect('nonos.db')

c = conn.cursor()

c.execute("CREATE TABLE routes (driver text,nuplate text, purp text, dest text, r_dates text,r_from text, km_start int, id integer primary key)")
c.execute("CREATE TABLE drivers (name text unique not null, telephone text unique not null)")
c.execute("CREATE TABLE licen (nuplate text unique not null)")
c.execute("CREATE TABLE scop (purp text unique not null)")
c.execute("CREATE TABLE diadromi (dest text unique not null)")

conn.close()
