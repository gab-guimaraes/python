import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')'
               )

#cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Gabriel", 75.0)')
#conexao.commit()

cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?,?)', ('Maria', 50))
conexao.commit()

cursor.execute('SELECT * FROM clientes')
for linha in cursor.fetchall():
    identifier, nome, peso = linha
    print(identifier, nome, peso)



cursor.close()


conexao.close()
