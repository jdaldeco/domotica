import pyodbc

def mostrarTodos(conn):
    cursor = conn.cursor()
    cursor.execute("select * from Temperatura")
    for row in cursor:
        print(f'row = {row}')
    print()

def insertLuz(conn,luz,estado):
    cursor = conn.cursor()
    cursor.execute(
        'insert into Luces(Luz,Estado) values(?,?);',
        (luz, estado)
    )
    conn.commit()

def insertAlarma(conn, estado):
    cursor = conn.cursor()
    cursor.execute(
        'insert into Alarma(Estado) values(?);',
        (estado)
    )
    conn.commit()
 
def insertFuego(conn, estado):
    cursor = conn.cursor()
    cursor.execute(
        'insert into Fuego(Estado) values(?);',
        (estado)
    )
    conn.commit()

def insertTemperatura(conn,Humedad,Temperatura,Calor):
    cursor = conn.cursor()
    cursor.execute(
        'insert into Temperatura(Humedad,Temperatura,IndiceCalor) values(?,?,?);',
        (Humedad,Temperatura,Calor)
    )
    conn.commit()

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-CRISTINA;"
    "Database=Domotica;"
    "Trusted_Connection=yes;"
)

conn.close()
