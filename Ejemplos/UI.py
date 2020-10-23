
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from time import sleep
from tkinter import *
datos =[]

# Fetch the service account key JSON file contents
cred = credentials.Certificate('C:/Users/Camilo/haiko/proyecto_BD_2/clave/clave.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://fir-haiko.firebaseio.com//'
})

ref = db.reference("mensajes")
    
ventana = Tk()
ventana.geometry('850x850')
ventana.configure(bg = 'white')
ventana.title("Bienvenidos a las UI")
texto = Label(ventana, text="CHAT HAIKO", bg='cadet blue1', font=("Arial Bold", 14), fg="white")
texto.place(x=20, y=20)

def entrada(input):
    content = dato.get()
    dato.delete(0, END)#borro la información del entry
    
    if int(content)== 1:
        ref.update({
                    'mensaje1': 'hola',
         }) 
    if int(content)== 2:
        print("PRueba1")  
    if int(content)== 3:
        print("prueba2")
    print(content)  
    
Label(ventana, text="Input: ").place(x=20, y=60)
dato = Entry(ventana)
dato.bind('<Return>', entrada) 
dato.place(x=90, y=60)


ventana.mainloop()







    



    
    
