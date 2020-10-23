
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from time import sleep
from tkinter import *

# URL clave.json
cred = credentials.Certificate('C:/Users/diana/haiko/proyectoOctubre/firebase_python/clave_Json/clave.json')
# URL Fire Base       
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://proyecto-haiko-base-de-datos.firebaseio.com/'
})

ref = db.reference("mensajes")
    
ventana = Tk()
ventana.geometry('1366x768')
ventana.configure(bg = '#eeffff')
ventana.title("Be Ele Cuatro Ka Ye Ciento Trece")
texto = Label(ventana, text="CHAT HAIKO", bg='#00eeff', font=("Georgia", 20), fg="#bb00ee")
texto.place(x=300, y=10)

def entrada(input):
    content = dato.get()
    dato.delete(0, END)#borro la información del entry
    ref.update({
        'men': content

    })

    men = db.reference(men)
    ent = Label(ventana, text=content, bg='#eecc00')
    ent.place(x = 100, y = 80)
    
    """
    if int(content)== 1:
        ref.update({
                    'mensaje1': 'hola',
         }) 
    if int(content)== 2:
        print("PRueba1")  
    if int(content)== 3:
        print("prueba2")
    print(content)  
    """
    
Label(ventana, text="Input: ",font =("Georgia",15),fg ="#bb00ee").place(x=20, y=60)
dato = Entry(ventana)
dato.bind('<Return>', entrada) 
dato.place(x=90, y=60)

ventana.mainloop()
