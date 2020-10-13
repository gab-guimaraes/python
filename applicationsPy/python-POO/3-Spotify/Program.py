import mysql.connector

from Artist import Artist
from Music import Music


a = Artist("3 Doors Down", "EUA")
b = Artist("Blink182", "EUA")
c = Artist("HIM", "Finland")

m = Music("Here without u", a, 3.18)
m2 = Music("Kriptonite", a, 4.10)
m3 = Music("Always", b, 3.00)
m4 = Music("Wickd Game", c, 4.53)

listOfMusic = [m, m2, m3, m4]

for v in listOfMusic:
    v.imprimeTudo()
    print('\n')


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="@blink182",
  database="spotify"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Artist (name, country) VALUES (%s, %s)"
val = (a.nome, a.pais)
mycursor.execute(sql, val)

mydb.commit()

print("record inserted")

