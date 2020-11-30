import tkinter as t

class perroFeo:
    def __init__(self, base, mensaje):
        self.button = t.Button(
            base,
            text = mensaje,
            command = self.gato,
        )
        self.button.pack(
            padx = 10,
            pady = 10,
        )
    
    def gato (self):
        print("Gato")

#Hacer la ventana(?

root = t.Tk()
root.geometry('200x200')

#Div ventana
div = t.Frame(root)
div.pack()

#button in the div

label = t.Label(div, text='Perro')
button = perroFeo(root, "HOLA")
label.pack()

#event loop?

root.mainloop()
