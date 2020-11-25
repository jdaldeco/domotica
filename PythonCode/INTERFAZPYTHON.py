import tkinter as tk
import serial
from tkinter import Frame, ttk, PhotoImage, Canvas
import conexionBDDOMOTICA as bdd
import pyodbc

# Inserta los datos del Estado de los LED leídos del puerto serie
def insertarEstadoLuces(arduino, lista):
    # Lee el puerto serie. Elimina los dos ultimos caracteres que
    # son el salto de linea
    
    data = arduino.readline()[:-2]
    # Si se leyeron datos del puerto serie
    if data:
        lista.insert(0, data)

# Inserta los datos del Estado de la Alarma leídos del puerto serie
def insertarEstadoAlarma(arduino, lista):
    # Lee el puerto serie. Elimina los dos ultimos caracteres que
    # son el salto de linea
    
    data = arduino.readline()[:-2]
    # Si se leyeron datos del puerto serie
    if data:
        lista.insert(0, data)
        
# Inserta los datos del Estado de la Alarma leídos del puerto serie
def insertarEstadoJardin(arduino, lista):
    # Lee el puerto serie. Elimina los dos ultimos caracteres que
    # son el salto de linea
    
    data = arduino.readline()[:-2]
    # Si se leyeron datos del puerto serie
    if data:
        lista.insert(0, data)

# Inserta los datos del Estado de la Alarma leídos del puerto serie
def insertarEstadoIncendio(arduino, lista):
    # Lee el puerto serie. Elimina los dos ultimos caracteres que
    # son el salto de linea
    
    data = arduino.readline()[:-2]
    # Si se leyeron datos del puerto serie
    if data:
        lista.insert(0, data)
  
def buttonClick(arduino):
   arduino.write(b'\n1on')
    
####################################
#cONEXION A BDD
conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-CRISTINA;"
    "Database=Domotica;"
    "Trusted_Connection=yes;"
)
#####################################

arduino = serial.Serial("COM5", 9600, timeout = 1)
main = tk.Tk()
main.title("Domotica")
main.resizable(False, False)
main.geometry("500x500+650+200")

#canvas = Canvas(main, width=500, height=400, bd=0, highlightthickness=0)
#canvas.pack()

#Se crea el contenedor de pestañas
tabs = ttk.Notebook(main)

###############################################################################

# Se crea Frame para pestaña de secuencia de luces
luces = tk.Frame(tabs, bg = "mint cream",  borderwidth = 3, relief = "ridge")
luces.config(width = "480", height = "480")
luces.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)

# Label título 'Visualización de luces'
lblLucesB = tk.Label(luces, text = "Visualización de luces", font = 40, bg = "mint cream", borderwidth = 3, relief = "ridge")
lblLucesB.pack()
lblLucesB.place(relx = 0.35, rely = 0.02)

# Imagen de la PLANTA BAJA en una label
pBaja = PhotoImage(file = r"C:\Users\crisb\Desktop\verano\empotrados\domotica\pBaja1.png")
lblPBaja = tk.Label(luces, image = pBaja, bg = "mint cream")
lblPBaja.pack()
lblPBaja.place(relx = 0.02, rely = 0.1)

# Imagen de la PLANTA ALTA en una label
pAlta = PhotoImage(file = r"C:\Users\crisb\Desktop\verano\empotrados\domotica\pAlta1.png")
lblPAlta = tk.Label(luces, image = pAlta, bg = "mint cream")
lblPAlta.pack()
lblPAlta.place(relx = 0.5, rely = 0.1)

# Creación del Scrollbar
estadoLuces = tk.Scrollbar(luces)
estadoLuces.pack()

# Se crea una lista para insertarla en el frame 'Jardín'
listaEstadoLuces = tk.Listbox(luces, yscrollcommand = estadoLuces.set)
listaEstadoLuces.place(relx = 0.1, rely = 0.68, relwidth = 0.8, relheight = 0.2)
entry = ttk.Entry(main)
entry = ttk.Entry(main)
# Crear caja de texto.


# Posicionamiento del Scrollbar
estadoLuces.place(relx = 0.9, rely = 0.68, relheight = 0.2)
estadoLuces.config(command = listaEstadoLuces.yview)

# Boton para leer puerto serie


# Se añade el Frame creado al contenedor de pestañas
tabs.add(luces, text = "Luces")

###############################################################################

# Se crea Frame para pestaña del estado de la alarma
alarma = tk.Frame(tabs, bg = "light yellow2",  borderwidth = 3, relief = "ridge")
alarma.config(width = "480", height = "480")
alarma.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)

# Label título 'Estado de Alarma'
lblLucesB = tk.Label(alarma, text = "Estado de Alarma Infrarroja", font = 40, bg = "light yellow2", borderwidth = 3, relief = "ridge")
lblLucesB.pack()
lblLucesB.place(relx = 0.3, rely = 0.02)

# Imagen de la PLANTA BAJA en una label
casitaAlarma = PhotoImage(file = r"C:\Users\crisb\Desktop\verano\empotrados\domotica\pBaja1.png")
lblKsitaA = tk.Label(alarma, image = casitaAlarma, bg = "light yellow2")
lblKsitaA.pack()
lblKsitaA.place(relx = 0.2, rely = 0.15, relwidth = 0.6, relheight = 0.5)

# Creación del Scrollbar
estadoAlarma = tk.Scrollbar(alarma)
estadoAlarma.pack()

# Se crea una lista para insertarla en el frame 'Jardín'
listaEstadoAlarma = tk.Listbox(alarma, yscrollcommand = estadoAlarma.set)
listaEstadoAlarma.place(relx = 0.1, rely = 0.68, relwidth = 0.8, relheight = 0.2)

# Posicionamiento del Scrollbar
estadoAlarma.place(relx = 0.9, rely = 0.68, relheight = 0.2)
estadoAlarma.config(command = listaEstadoAlarma.yview)

# Boton para leer puerto serie


tabs.add(alarma, text = "Alarma")

###############################################################################

# Se crea Frame para pestaña del estado del jardín
jardin = tk.Frame(tabs, bg = "#E6FBE0",  borderwidth = 3, relief = "ridge")
jardin.config(width = "480", height = "480")
jardin.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)

# Label título 'Estado del jardín'
lblJardin = tk.Label(jardin, text = "Estado del jardín", font = 40, bg = "#E6FBE0", borderwidth = 3, relief = "ridge")
lblJardin.pack()
lblJardin.place(relx = 0.35, rely = 0.02)

# Imagen de la PLANTA ALTA en una label
casitaJardin = PhotoImage(file = r"C:\Users\crisb\Desktop\verano\empotrados\domotica\pAlta1.png")
lblKsitaJ = tk.Label(jardin, image = casitaJardin, bg = "#E6FBE0")
lblKsitaJ.pack()
lblKsitaJ.place(relx = 0.2, rely = 0.15, relwidth = 0.6, relheight = 0.5)

# Creación del Scrollbar
estadoJardin = tk.Scrollbar(jardin)
estadoJardin.pack()

# Se crea una lista para insertarla en el frame 'Jardín'
listaEstadoJardin = tk.Listbox(jardin, yscrollcommand = estadoJardin.set)
listaEstadoJardin.place(relx = 0.1, rely = 0.68, relwidth = 0.8, relheight = 0.2)

# Posicionamiento del Scrollbar
estadoJardin.place(relx = 0.9, rely = 0.68, relheight = 0.2)
estadoJardin.config(command = listaEstadoJardin.yview)

# Boton para leer puerto serie

btnAlarma = tk.Button(jardin, text = "Leer puerto serie", command = lambda: insertarEstadoAlarma(arduino, listaEstadoJardin))
btnAlarma.pack()
btnAlarma.place(relx = 0.38, rely = 0.9, relwidth = 0.2)

tabs.add(jardin, text = "Jardín")

###############################################################################

llamitas = tk.Frame(tabs, bg = "#FFA9A6", borderwidth = 3, relief = "ridge")
llamitas.config(width = "480", height = "480")
llamitas.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)

# Label título 'Estado de alarma de incendios'
lblIncendios = tk.Label(llamitas, text = "Estado de alarma de incendios", font = 40, bg = "#FFA9A6", borderwidth = 3, relief = "ridge")
lblIncendios.pack()
lblIncendios.place(relx = 0.3, rely = 0.02)

# Imagen de la PLANTA BAJA en una label
casitaIncendio = PhotoImage(file = r"C:\Users\crisb\Desktop\verano\empotrados\domotica\pBaja1.png")
lblKsitaI = tk.Label(llamitas, image = casitaIncendio, bg = "#FFA9A6")
lblKsitaI.pack()
lblKsitaI.place(relx = 0.2, rely = 0.15, relwidth = 0.6, relheight = 0.5)

# Creación del Scrollbar
estadoIncendio = tk.Scrollbar(llamitas)
estadoIncendio.pack()

# Se crea una lista para insertarla en el frame 'Jardín'
listaEstadoIncendio = tk.Listbox(llamitas, yscrollcommand = estadoAlarma.set)
listaEstadoIncendio.place(relx = 0.1, rely = 0.68, relwidth = 0.8, relheight = 0.2)

# Posicionamiento del Scrollbar
estadoIncendio.place(relx = 0.9, rely = 0.68, relheight = 0.2)
estadoIncendio.config(command = listaEstadoIncendio.yview)

# Boton para leer puerto serie


tabs.add(llamitas, text = "Incendios")

###############################################################################

tabs.pack(expand = 1, fill = "both")
while True:    
    data = arduino.readline()[:-2]
    data2=data.decode('utf-8')

    if data2=="LED1ON":
        bdd.insertLuz(conn,"LED1","ON")
        listaEstadoLuces.insert(0, "Habitacion 1: ON")
    elif data2=="LED1OFF":
         bdd.insertLuz(conn,"LED1","OFF")
         listaEstadoLuces.insert(0, "Habitacion 1: OFF")
    elif data2=="LED2ON":
         bdd.insertLuz(conn,"LED2","ON")
         listaEstadoLuces.insert(0, "Habitacion2: ON")
    elif data2=="LED2OFF":
         bdd.insertLuz(conn,"LED2","OFF")
         listaEstadoLuces.insert(0, "Habitacion 2: OFF")
    elif data2=="LED3ON":
         bdd.insertLuz(conn,"LED3","ON")
         listaEstadoLuces.insert(0, "Habitacion 3: ON")
    elif data2=="LED3OFF":
         bdd.insertLuz(conn,"LED3","OFF")
         listaEstadoLuces.insert(0, "Habitacion 3: OFF")
    elif data2=="LED4ON":
         bdd.insertLuz(conn,"LED4","ON")
         listaEstadoLuces.insert(0, "Habitacion 4: ON")
    elif data2=="LED4OFF":
         bdd.insertLuz(conn,"LED4","OFF")
         listaEstadoLuces.insert(0, "Habitacion 4: OFF")
    elif data2=="PIRON":
         bdd.insertAlarma(conn,"ON")
         listaEstadoAlarma.insert(0,"Alarma Activada")
    elif data2=="PIROFF":
         bdd.insertAlarma(conn,"OFF")
         listaEstadoAlarma.insert(0,"Alarma DESActivada")
    elif data2=="fon":
         bdd.insertFuego(conn,"Incendio Detectado")
         listaEstadoIncendio.insert(0,"Incendio Detectado")
    elif data2.startswith(":"):
        ##if data2.startswith("Humedad"):
          ##  
            ##humedad=data2;
        ##if data2.startswith("Temperatura"):
            ##temperatura=data2;
        ##if data2.startswith("Indice"):
            ##indice=data2;
        listaEstadoJardin.delete(0,'end')
        d = data2.split(":")
        humedad = d[1]
        temperatura = d[2]
        indice = d[3]
        imp = "Humedad:" + humedad + "__Temperatura:" + temperatura + "__IndiceCalor:" + indice
        listaEstadoJardin.insert(0, imp)  
        bdd.insertTemperatura(conn,humedad,temperatura,indice)
        
    main.update_idletasks();
    main.update();