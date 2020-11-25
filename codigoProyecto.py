#Made By Bl4ky113 & XicXac

#Librerias Firebase

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#Librerias tkinter

import tkinter as t

#Otras librerias

from numpy import random
from time import sleep

# Fetch the service account key JSON file contents
cred = credentials.Certificate('C:/Users/diana/OneDrive/Documentos/Haiko/proyecto/clave_Json/clave.json')
# Initialize the app with a service account, granting admin privileges       
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://bankdatabase-haiko.firebaseio.com/'
})

"""  Variables  """

ref = db.reference("usuarios")
usuarios = ref.get()

"""  Functions  """

def checkUserInfo (opcion, nombreU):
    # Opción 1: Check Nombre
    if opcion == 1:
        if nombreU in usuarios:
            return True
        else:
            return False

def ventanaError (opcion):
    #Var de contexto del error
    mensajeError = "Error no especificado"

    #Base de Error (ventana emergente)
    baseError = t.Toplevel()
    baseError.title("Error")
    baseError.geometry('400x100')

    #Titulo
    divTitulo = t.Frame(baseError,
        #Border
        borderwidth = 2,
        relief = "solid",
    )

    labelTitulo = t.Label(divTitulo,
        #Texto
        text = "Error",
        font = ("Aria", 16),

        #Padding
        padx = 10,
        pady = 10,
    )

    divTitulo.pack()

    labelTitulo.pack()

    #Texto especificacion del Error
    divTexto = t.Frame(baseError)

    labelTexto = t.Label(divTexto,
        #Texto
        text = mensajeError,
        font = ("Arial", 12),

        #Padding
        padx = 10,
        pady = 10,
    )

    divTexto.pack()
    labelTexto.pack()

    #Opcion 1: 
    if opcion == 1:
        mensajeError = "El nombre de la Cuenta ya esta ocupado.\nIntente otro nombre."

        labelTexto.config(text = mensajeError)


"""  Menu de inicio """

#Base del Menu Inicio (Ventana)
baseMenuInicio = t.Tk()
baseMenuInicio.title("Banco Virtual Haiko")
baseMenuInicio.geometry('1000x500')

#Titulo
divTitulo = t.Frame(baseMenuInicio,
    #Border
    borderwidth = 3,
    relief = "solid",
)

labelTitulo = t.Label(divTitulo,
    #Texto
    text = 'Banco Virtual Haiko.',
    font = ("Arial Bold", 30),

    #Padding
    padx = 5,
    pady = 5,
)

divTitulo.pack(
    #Margin
    padx = 10,
    pady = 10,
)

labelTitulo.pack()


#Saludo
divSaludo = t.Frame(baseMenuInicio,
    #Border
    borderwidth = 1,
    relief = "solid",
)

labelSaludo = t.Label(divSaludo,
    #Texto
    text = "¡¡Bienvenido a El Banco Virtual de Haiko!!",
    font = ("Arial Bold", 20),

    #Padding
    padx = 5,
    pady = 5,
)

divSaludo .pack(
    #Margin
    padx = 10,
    pady = 10,
)

labelSaludo.pack()

#Texto o Introduccion
divTexto = t.Frame(baseMenuInicio)

labelTexto = t.Label(divTexto,
    #Texto
    text = "Ingrese que acción quiere realizar.",
    font = ("Arial Bold", 14),
)

divTexto.pack(
    #Margin
    padx = 5,
    pady = 5,
)

labelTexto.pack()

#Opciones    

def menuCrearCuenta ():

    #Functions Crear nueva cuenta en FireBase

    #Check de nombre en data Base
    def nombreCheck (info):
        nombreNuevaCuenta = inputNombre.get()
        if checkUserInfo(1, nombreNuevaCuenta) == False:
            print(nombreNuevaCuenta)
            divBasePassword.pack()

        else:
            ventanaError(1)

    #Hacer el código del usuario
    def codigoUsuario (numDigitos):
        baseCodigo = []
        sumaCodigo = 0
        codigoFinal = ""
        for i in range(numDigitos):
            baseCodigo.append(random.randint(9))
            sumaCodigo += baseCodigo[i]
            codigoFinal += str(baseCodigo[i])
            
        codigoFinal += str(sumaCodigo)

        return codigoFinal

    #Crear la cuenta
    def crearCuenta (info):
        nombre = inputNombre.get()
        password = inputPassword.get()
        codigo = codigoUsuario(6)

        print("Nombre: ", nombre)
        print("Password: ", password)
        print("Código: ", codigo)

    #Base Crear & Nueva Cuenta
    baseCrearCuenta = t.Toplevel()
    baseCrearCuenta.title("Crear Nueva Cuenta")
    baseCrearCuenta.geometry('1000x500')

    #Titulo
    divTitulo = t.Frame(baseCrearCuenta,
        #border
        borderwidth = 2,
        relief = "solid",
    )

    labelTitulo = t.Label(divTitulo,
        #Texto
        text = "Crear una Nueva Cuenta",
        font = ("Arial Bold", 20),

        #Padding
        padx = 5,
        pady = 5,
    )
    
    divTitulo.pack(
        #Margin
        padx = 10,
        pady = 10,
    )

    labelTitulo.pack()

    #Div Base Nombre

    divBaseNombre = t.Frame(baseCrearCuenta)

    divBaseNombre.pack()

    #Label de Input Nombre

    divTextoNombre = t.Frame(divBaseNombre,
        #Border
        borderwidth = 1,
        relief = "solid",
    )

    labelTextoNombre = t.Label(divTextoNombre,
        #Texto
        text = "Ingrese el nombre de su nueva Cuenta:",
        font = ("Arial", 14),

        #Padding
        padx = 5,
        pady = 5,
    )

    divTextoNombre.pack(
        #Margin
        padx = 30,
        pady = 10,

        #Align
        side = "left"
    )

    labelTextoNombre.pack()

    #Input Nombre

    divNombre = t.Frame(divBaseNombre,
        #Border
        borderwidth = 1,
        relief = "solid",
    )

    inputNombre = t.Entry(divNombre)
    inputNombre.bind('<Return>', nombreCheck)
    
    divNombre.pack(
        #Align
        side = "left",
    )

    inputNombre.pack(
        #Align
        side = "right",
    )

    #Div Base Password (hidden)

    divBasePassword = t.Frame(baseCrearCuenta)

    #divBasePassword.pack()

    #Label Password

    divTextoPassword = t.Frame(divBasePassword,
        #Border
        borderwidth = 1,
        relief = "solid",
    )

    labelTextoPassword = t.Label(divTextoPassword,
        #Texto
        text = "Ingrese la contraseña de su nueva Cuenta:",
        font = ("Arial", 14),

        #Padding
        padx = 5,
        pady = 5,
    )

    divTextoPassword.pack(
        #Align
        side = "left",

        #Margin
        padx = 30,
        pady = 10,
    )

    labelTextoPassword.pack(
        #Margin
        padx = 10,
        pady = 10,
    )

    #Input de Password

    divPassword = t.Frame(divBasePassword,
        #Margin
        borderwidth = 1,
        relief = "solid",
    )

    inputPassword = t.Entry(divPassword)
    inputPassword.bind('<Return>', crearCuenta)

    divPassword.pack(
        #Align
        side = "right",
    )

    inputPassword.pack()

def iniciarSesion ():
    print("a")

def borrarCuenta ():
    print("a")


divOpciones = t.Frame(baseMenuInicio,
    #Border
    borderwidth = 3,
    relief = "solid",
)

btnRegistrarse = t.Button(divOpciones, #Crea una cuenta a el usuario & inicia sesion con esta
    #Texto
    text = 'Crear Cuenta',
    font = ("Arial", 10),

    #Function
    command = menuCrearCuenta,

    #Padding
    padx = 15,
    pady  = 5,

    #H&W
    height = 2,
    width = 30,
)

btnIniciar = t.Button(divOpciones, #Inicia la Sesion del usuario en una cuenta ya hecha
    #Texto
    text = "Iniciar Sesion",
    font = ("Arial", 10),

    #Function
    command = iniciarSesion,

    #Padding
    padx = 15,
    pady = 5,

    #H&W
    height = 2,
    width = 10,
)

btnBorrar = t.Button(divOpciones, #Borra la cuenta de un usuario
    #Texto
    text = "Borrar Cuenta",
    font = ("Arial", 10),

    #Function
    command = borrarCuenta,
    
    #padding
    padx = 15,
    pady = 5,
    
    #H&W
    height = 2,
    width = 10,
)

divOpciones.pack(
    #Margin
    pady = 10,
)

btnRegistrarse.pack(
    #Align
    side = "top",

    #Margin
    padx = 20,
    pady = 10,
)

btnIniciar.pack(
    #Align
    side = "right",

    #Margin
    padx = 30,
    pady = 10,
)

btnBorrar.pack(
    #Align
    side = "left",

    #Margin
    padx = 30,
    pady = 10,
)

"""#Menu de Usuario

def menuUsuario(userName):
    print("'a' para ingresar dinero a su cuenta. \n'b' para depositar dinero en otra cuenta \n'c' para verificar el balance en su cuenta")
    opcionUsuario = input("Su opción es:   ")
    global money_ref 
    money_ref = db.reference("Usuarios/" + userName + "/dinero")
    money = money_ref.get()

    #Agrega balance, si tiene Deuda se resta a esta y se agrega lo que deje a balance

    if opcionUsuario.lower() == 'a':
        sumaMoney = int(input("Digite el monto a ingresar:   "))
        totalMoney = usuarios[userName]['dinero']['balance'] + sumaMoney
        money_ref.update({
            'balance':totalMoney,

        })
        print("Listo!! su balance ha sido actualizado")
        menuUsuario(userName)

    #Enviar dinero a otra cuenta con cd y nm, Si deposito < balance, se acumula deuda

    if opcionUsuario.lower() == 'b':
        print("Ingrese el nombre y código de la cuenta a la cual depositara dinero")
        nombreDeposito = input("Nombre de la cuenta:   ")
        codigoDeposito = int(input("Código de la cuenta:   "))
        if nombreDeposito in usuarios and codigoDeposito == usuarios[nombreDeposito]['codigo']:
            print("Listo! Ahora necesitamos que digite la cantidad de dinero que va a depositar a ",nombreDeposito)
            cantidadDeposito = int(input("Cantidad de dinero a depositar:   "))
            if cantidadDeposito < (money['balance'] - money['deuda']):
                usuarioDepositado = db.reference('Usuarios/' + nombreDeposito + '/dinero')
                depositoAgregado = cantidadDeposito + usuarios[nombreDeposito]['dinero']['balance']
                usuarioDepositado.update({
                    'balance': depositoAgregado,

                })
                money_ref.update({
                    'deuda': cantidadDeposito + 100,

                })
                sleep(2)
                menuUsuario(userName)

            else:
                print("Su cuenta no tiene los fondos necesarios en el balance para poder hacer este deposito")
                print("¿Quiere pedir un prestamo para pagar el deposito?")
                respuesta = input("Si o No:   ")
                if respuesta.lower() == "si":
                    usuarioDepositado = db.reference('Usuarios/' + nombreDeposito + '/dinero')
                    depositoAgregado = cantidadDeposito + usuarios[nombreDeposito]['dinero']['balance']
                    usuarioDepositado.update({
                        'balance': depositoAgregado,

                    })
                    money_ref.update({
                        'deuda': (cantidadDeposito + 100) * 1.7,

                    })
                    sleep(2)
                    menuUsuario(userName)
                elif respuesta.lower() == "no":
                    sleep(2)
                    menuUsuario(userName)    

    #Ver balance total = balance - Deuda
    elif opcionUsuario.lower() == 'c':
        print("El balance en su cuenta es de:   ", money['balance'] - money['deuda'])
        sleep(2)
        menuUsuario(userName)

#Menu de Inicio

def menuInicio():

    print("'a' para crear una nueva cuenta \n'b' para ingresar en su cuenta \n'c' para eliminar una cuenta")
    accion = input("Ingrese que accion quiere realizar:   ")

    if accion.lower() == 'a':
        nombreNewU = input("Ingrese el nombre del usuario:  ")
        if nombreNewU in usuarios:
            print("Este nombre de Usuario ya esta definido\nIntente otro nombre de usuario")
            sleep(tiempoIntervalo)
            menuInicio()
        else:    
            passwordNewU = int(input("Ingrese su contraseña:  "))
            codigoNewU = random.randint(1000)
            ref.update({
                nombreNewU:{
                    'password': passwordNewU, 
                    'codigo': codigoNewU,
                    'dinero':{
                        'balance': 0,
                        'deuda': 0,
                        } ,
                    },
                })
            print("Listo! Su usuario es: ", nombreNewU, "\nSu codigo es: ", codigoNewU) 
            sleep(tiempoIntervalo)
            menuUsuario(nombreNewU)   
    
    elif accion.lower() == 'b':
        nombreSignIn = input("Ingrese el nombre de usuario de su cuenta:  ")
        codigoSignIn = int(input("Ingrese el codigo de su cuenta:  "))    
        if nombreSignIn in usuarios and codigoSignIn == usuarios[nombreSignIn]['codigo']:
            passwordSignIn = int(input("Ingrese la constraseña de su cuenta:  "))
            if passwordSignIn == usuarios[nombreSignIn]['password']:
                print("Bienvenido Usuario: ", nombreSignIn)
                menuUsuario(nombreSignIn)
            else:
                print("Su contraseña esta mal \nVuelva a intentar")
                sleep(tiempoIntervalo)
                menuInicio()
        else:
            print("El nombre o el codigo estan mal \nVuelva a intentar")
            sleep(tiempoIntervalo)
            menuInicio()

    elif accion.lower() == 'c':
        nombreDelete = input("Ingrese el nombre del usuario que quiere eliminar:   ")
        codigoDelete = int(input("Ingrese el código del usuario que quiere eliminar:   "))
        if nombreDelete in usuarios and codigoDelete == usuarios[nombreDelete]['codigo']:
            passwordDelete = int(input("Ingrese la contraseña del usuario que quiere eliminar:   "))
            if passwordDelete == usuarios[nombreDelete]['password']:
                print("Hasta pronto ", nombreDelete)
            else:
                print("La contraseña del usuario a eliminar esta mal digitada\nVuelva a intentar")
                sleep(tiempoIntervalo)
                menuInicio()    
        else:
            print("El usuario que quiere eliminar no esta definido\nVuelva a intentar")
            sleep(tiempoIntervalo)
            menuInicio()
    else:
        print("Esa Opción no está definida en el programa\nVuelva a intentar")
        sleep(tiempoIntervalo)
        menuInicio()
"""
baseMenuInicio.mainloop()