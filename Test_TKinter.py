from tkinter import *

#Hacer la ventana(?

root = Tk()
root.geometry('200x200')

#Div ventana
div = Frame(root)
div.pack()

#button in the div

label = Label(div, text='Perro')
button = Button(root, text = 'a', bd = '5', command = root.destroy)
button.pack()
label.pack()

#event loop?

root.mainloop()
