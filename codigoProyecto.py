#Made By Bl4ky113 & XicXac

"""  Librerias  """

#Librerias Firebase 
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#Librerias tkinter
import tkinter as t

#Otras librerias
from numpy import random
from time import sleep

""" Firebase admin """

# Fetch the service account key JSON file contents
cred = credentials.Certificate('C:/Users/diana/OneDrive/Documentos/Haiko/proyecto/clave_Json/clave.json')
# Initialize the app with a service account, granting admin privileges       
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://bankdatabase-haiko.firebaseio.com/'
})

global ref, usuarios
ref = db.reference("usuarios")

"""  Class  """

#Plantila de titulos
class plantilla_titulo:
    #Base de titulo; Tamaño de borde; Tipo de borde; Tamaño letra; Posición; Titular (contenido)
    def __init__ (self, base, borde, tipoBorde, size, position, titular):
        #Titulo
        titulo = t.Label(base,
            #Border
            borderwidth = borde, relief = tipoBorde,
            #Texto
            text = titular, font = ("Arial Bold", size),
            #Padding
            padx = 10, pady = 10,
        )
        titulo.pack(
            #Align
            side = "top", fill = "x", anchor = position,
            #Margin
            padx = 20, pady = 10,
        )

#Plantilla de userInput
class plantilla_userInput:
    #Base del input; Mensaje del label; Status del div(show || hide)
    def __init__ (self, base, textoLabel, visual):
        #Div & base
        self.baseInput = t.Frame(base)
        if visual == "show":
            self.baseInput.pack()

        #Label
        label = t.Label(self.baseInput, 
            #Border
            borderwidth = 1, relief = "solid",
            #Texto
            text = textoLabel, font = ("Arial", 14),
            #Padding 
            padx = 5, pady = 5,
        )
        label.pack(
            #Align
            side = "left",
            #Margin
            padx = 30, pady = 10,
        )

        self.input = t.Entry(self.baseInput,
            #Border
            borderwidth = 1, relief = "solid",
        )
        self.input.pack(
            #Align
            side = "right"
        )

class plantilla_texto:
    def textoSinBorde (self, base, mensaje, size, padding, align, position, margin): 
        #Base del texto; Mensaje del texto; Tamaño del texto; Padding; Align(side, anchor); Margin
        self.label = t.Label(base,
            #Texto
            text = mensaje, font = ("Arial", size),
            #Padding
            padx = padding, pady = padding,
        )
        self.label.pack(
            #Align
            side = align, anchor = position,
            #Margin
            padx = margin, pady = margin,
        )
    
    def textoConBorde (self, base, mensaje, size, padding, align, position, margin, anchoBorde, tipoBorde): 
        #Base del texto; Mensaje del texto; Tamaño del texto; Padding; Align(side, anchor); Margin; Tamaño del borde; Tipo de borde
        self.label = t.Label(base,
            #Border
            borderwidth = anchoBorde, relief = tipoBorde,
            #Texto
            text = mensaje, font = ("Arial", size),
            #Padding
            padx = padding, pady = padding,
        )
        self.label.pack(
            #Align
            side = align, anchor = position,
            #Margin
            padx = margin, pady = margin,
        )

class plantilla_botones:
    def botonOpciones(self, base, mensaje, size, funcion, alto, ancho, align, margin_x, margin_y):
        button = t.Button (base,
            #Texto
            text = mensaje, font = ("Arial", size),
            #Function
            command = funcion,
            #Padding
            padx = 15, pady = 5,
            #Height & Width
            height = alto, width = ancho,
        )
        button.pack(
            #Align
            side = align,
            #Margin
            padx = margin_x, pady = margin_y,
        )
    
    def botonAceptar(self, base, function): #Base botón; Función 
        button = t.Button (base,
            #Texto
            text = "Aceptar", font = ("Arial", 12),
            #Function
            command = function,
            #Padding
            padx = 10, pady = 10,
            #Height & Width
            height = 2, width = 20,
        )
        button.pack(
            #Align
            side = "bottom",
            #Margin
            padx = 10, pady = 10,
        )

"""  Functions  """

#Revisar info del usuario en dataBase
def checkUserInfo (opcion, nombreUsuario, passwordUsuario, codigoUsuario):
    #Obtener info de dataBase
    usuarios = ref.get()
    # Opción 1: Check Nombre en dataBase
    if opcion == 1:
        if nombreUsuario in usuarios:
            return True

        else:
            return False

    #Opción 2: Check Password y Código de un Usuario en dataBase
    elif opcion == 2:
        if passwordUsuario == usuarios[nombreUsuario]['password'] and codigoUsuario == usuarios[nombreUsuario]['code']:
            return True

        else:
            return False
    #Opción 3: Check sí deuda es menor a 0
    elif opcion == 3:
        if usuarios[nombreUsuario]['money']['debt'] == 0:
            return True
        
        else:
            return False

#Hacer el código númerico del usuario
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

#Ventana sí el usuario obtiene un error
def ventanaError (opcion):
    #Contexto del error
    mensajeError = "Error no especificado"

    #Base de Error (ventana emergente)
    baseError = t.Toplevel()
    baseError.title("Error")

    #Titulo Error
    tituloError = plantilla_titulo(
        #Base de titulo; Tamaño de borde; Tipo de borde; Tamaño letra; Posición; Titular (contenido)
        baseError, 2, "solid", 16, "center", "Error" 
    )

    #Texto especificacion del Error
    textoError = plantilla_texto()
    textoError.textoSinBorde(
        #Base del texto; Mensaje del texto; Tamaño del texto; Padding; Align(side, anchor); Margin
        baseError, mensajeError, 12, 5, "top", "center",5,
    )

    #Botón Aceptar
    btnAceptar = plantilla_botones()
    btnAceptar.botonAceptar(
        #Base botón; Función
        baseError, baseError.destroy,
    )

    #Opcion 1: Nombre usuario ya ocupado en dataBase al crear una nueva cuenta
    if opcion == "nombre_existente":
        mensajeError = "El nombre de la Cuenta ya esta ocupado.\nIntente otro nombre."
        textoError.label.config(text = mensajeError)
    
    elif opcion == "nombre_noExistente":
        mensajeError = "El nombre de la Cuenta no esta registrado.\nIntente otro nombre."
        textoError.label.config(text = mensajeError)

    elif opcion == "passwordcodigo_mal":
        mensajeError = "La contraseña o el código de la cuenta es incorrecto.\nIntente otra vez"
        textoError.label.config(text = mensajeError)


""" Menu De Usuario """

def menuUsuario(nombre, codigo):
    #Info del Usuario
    userRef = db.reference("usuarios/" + nombre)
    userData = userRef.get()

    #Base del Menu Usuario
    baseMenuUsuario = t.Toplevel()
    baseMenuUsuario.title("Banco Virutal Haiko; Usuario: " + nombre)
    baseMenuUsuario.geometry('1000x500')

    #Titulo Menu Usuario
    tituloUsuario = plantilla_titulo(
        #Base del titulo; Tamaño de Borde; Tipo de Borde; Tamaño letra; Posición; Titular contenido
        baseMenuUsuario, 4, "solid", 20, "nw", "Banco Virtual Haiko",    
    )

    #Info de Usuario
    baseInfoUsuario = t.Frame(baseMenuUsuario)
    baseInfoUsuario.pack(
        #Align
        anchor = "nw",
        #Paddding
        padx = 10,
        pady = 10,
    )

    textoInfoUsuario = plantilla_texto()
    textoInfoUsuario.textoConBorde(
        #Base del texto; Mensaje del texto; Tamaño del texto; Padding; Align(side, anchor); Margin; Tamaño del borde; Tipo de borde
        baseInfoUsuario, "Usuario: " + nombre, 16, 5, "left", "nw", 5, 1, "solid",
    )
    textoInfoUsuario.textoConBorde(
        #Base del texto; Mensaje del texto; Tamaño del texto; Padding; Align(side, anchor); Margin; Tamaño del borde; Tipo de borde
        baseInfoUsuario, "Código: "+ codigo, 16, 5, "left", "nw", 5, 1, "solid",
    )

    #Opciones Menu Usuario
    """"
    - Pedir Prestamos a nuestro Banco.
    - Depositar Dinero en tu Cuenta.
    - Retirar Dinero en Efectivo de tu Cuenta.
    - Transferir Dinero a Otros Usuarios.
    - Poder Mirar el Balance en tu Cuenta.
    - Recibir Dinero de Otros Usuarios.
    """

    #Pedir un Prestamo a el banco Haiko (+ Balance; + Deuda)
    def menuPedirPrestamo():
        print("A")

    btnPedirPrestamo = plantilla_botones()
    btnPedirPrestamo.botonOpciones(
        #Base botón; Texto botón; Tamaño letra; Función; H&W; Align; Margin (X, Y)
        baseMenuUsuario, "Pedir Prestamo", 14, menuPedirPrestamo, 2, 30, "top", 10, 10,
    )

    #Depositar dinero en tu cuenta (+ Balance || - Deuda)
    def menuDepositarDinero():
        #Base Depositar Dinero
        baseDepositarDinero = t.Toplevel()
        baseDepositarDinero.title("Depositar Dinero a Tu Cuenta")

        #Titulo
        tituloDepositarDinero = plantilla_titulo(
            #Base del titulo; Tamaño de Borde; Tipo de Borde; Tamaño letra; Posición; Titular contenido
            baseDepositarDinero, 2, "solid", 20, "center", "Depositar Dinero en Tu Cuenta",    
        )

        #Texto
        textoDepositarDinero = plantilla_texto()
        textoDepositarDinero.textoSinBorde(
            #Base del texto; Mensaje del texto; Tamaño del texto; Padding; Align(side, anchor); Margin
            baseDepositarDinero, "Ingresa la cantidad de dinero que quieras sumarle a el balance de tu cuenta", 14, 5, "top", "center", 5,
        )

        #Function Ingresa el dinero
        def ingresarDinero(info):
            #Dinero ingresado, Dinero de balance y Dinero de deusda
            dinero = int(inputCantidadDinero.input.get())
            balance = userData['money']['balance']
            deuda = userData['money']['debt']

            #Añade balance a la cuenta sí deuda = 0
            if checkUserInfo(3, nombre, "password", "code") == True:
                #Suma dinero a cuenta en dataBase
                balance += dinero
                userRef.update({
                    'money':{
                        'balance': balance,
                        'debt': deuda,

                    }

                })

                #Base Dinero Depositado
                baseDineroDepositado = t.Toplevel()
                baseDineroDepositado.title("¡Dinero Depositado!")

                #Titulo Dinero Depositado
                tituloDepositarDinero = plantilla_titulo(
                    #Base del titulo; Tamaño de Borde; Tipo de Borde; Tamaño letra; Posición; Titular contenido
                    baseDineroDepositado, 2, "solid", 20, "center", "¡Dinero Depositado en Tu Cuenta",    
                )

                #Texto Dinero Depositado
                textoDineroDepositado = plantilla_texto()
                textoDineroDepositado.textoSinBorde(
                    #Base del texto; Mensaje del texto; Tamaño del texto; Padding; Align(side, anchor); Margin
                    baseDineroDepositado,
                    "Se ha Depositado $" + str(dinero) + " a tu Cuenta " + str(nombre) + "\nDando un balance total de: $" + str(balance), 
                    16, 5, "top", "center", 5,
                )

                #Botón Aceptar
                def kill():
                    baseDineroDepositado.destroy()
                    baseDepositarDinero.destroy()

                btnAceptar = plantilla_botones()
                btnAceptar.botonAceptar(
                    #Base botón; Función
                    baseDineroDepositado, kill
                )

            #Sí tiene dueda,paga la deuda y despues deposita el dinero (sí queda alguno)
            else:
                deuda -= dinero
                
                #Paga la deuda y queda con dinero de sobra
                if deuda < 0:
                    balance = deuda * -1
                    userRef.update({
                        'money':{
                            'balance': balance,
                            'debt': 0,

                        }

                    })

                #No paga la deuda y queda sin dinero de sobra
                elif deuda > 0:
                    userRef.update({
                        'money':{
                            'balance': balance,
                            "debt": deuda,

                        }

                    })

                #Paga la deuda y queda sin dinero de sobra
                else:
                    userRef.update({
                        'money':{
                            'balance': balance,
                            'debt': 0,

                        }

                    })
                
        #Input cantidad de dinero a ingresar
        inputCantidadDinero = plantilla_userInput(
            #Base del input; Mensaje del label; Status del div(show || hide)
            baseDepositarDinero, "Cantidad de dinero:", "show",
        )
        inputCantidadDinero.input.bind('<Return>', ingresarDinero)

    btnDepositarDinero = plantilla_botones()
    btnDepositarDinero.botonOpciones(
        #Base botón; Texto botón; Tamaño letra; Función; H&W; Align; Margin (X, Y)
        baseMenuUsuario, "Depositar Dinero en tu Cuenta", 12, menuDepositarDinero, 1, 35, "top", 10, 5,
    )

    #Retirar dinero de tu cuenta, para obtener "efectivo" (- Balance || + Deuda)
    def menuRetirarDinero():
        print("A")

    btnRetirarDinero = plantilla_botones()
    btnRetirarDinero.botonOpciones(
        #Base botón; Texto botón; Tamaño letra; Función; H&W; Align; Margin (X, Y)
        baseMenuUsuario, "Retirar Dinero de tu Cuenta", 12, menuRetirarDinero, 1, 35, "top", 10, 5,
    )

    #Depositar & Transferir dinero a otra cuenta; NECESITA ID DE OTRA CUENTA (- Balance || + Deuda)
    def menuTransferirDinero():
        print("a")

    btnTransferirDinero = plantilla_botones()
    btnTransferirDinero.botonOpciones(
        #Base botón; Texto botón; Tamaño letra; Función; H&W; Align; Margin (X, Y)
        baseMenuUsuario, "Transferir Dinero a otra Cuenta", 12, menuTransferirDinero, 1, 35, "top", 10, 5, 
    )
    
    #Ver el balance o el dinero de la Cuenta
    def menuBalanceCuenta():
        print("a")

    btnBalanceCuenta = plantilla_botones()
    btnBalanceCuenta.botonOpciones(
        #Base botón; Texto botón; Tamaño letra; Función; H&W; Align; Margin (X, Y)
        baseMenuUsuario, "Revisar el Balance de la Cuenta", 12, menuBalanceCuenta, 1, 35, "top", 10, 5, 
    )

"""  Menu de inicio """

#Base del Menu Inicio (Main Ventana)
baseMenuInicio = t.Tk()
baseMenuInicio.title("Banco Virtual Haiko")
baseMenuInicio.geometry('1000x500')

#Titulo Inicio
tituloInicio = plantilla_titulo(
    #Base del titulo; Tamaño de Borde; Tipo de Borde; Tamaño letra; Posición; Titular contenido
    baseMenuInicio, 4, "solid", 20, "center", "Banco Virtual Haiko",
)

#Saludo
textoSaludo = plantilla_texto()
textoSaludo.textoConBorde(
    #Base del texto; Mensaje del texto; Tamaño del texto; Padding; Align(side, anchor); Margin; Tamaño del borde; Tipo de borde
    baseMenuInicio, "¡¡Bienvenido a El Banco Virtual de Haiko!!", 20, 5, "top", "center", 10, 1, "solid",
)

#Introduccion
textoIntroduccion = plantilla_texto()
textoIntroduccion.textoSinBorde(
    #Base del texto; Mensaje del texto; Tamaño del texto; Padding; Align(side, anchor); Margin
    baseMenuInicio, "Ingrese que acción quiere realizar", 14, 5, "top", "center", 5,
)

"""  Opciones  Menu  Inicio  """    

#Botones Opciones

baseBotonesOpciones = t.Frame(baseMenuInicio,
    #Border
    borderwidth = 3,
    relief = "solid",
)
baseBotonesOpciones.pack(
    #Margin
    pady = 10,
)


def menuCrearCuenta ():
    #Functions Crear nueva cuenta en FireBase

    #Check de nombre en data Base
    def nombreCheck (info):
        nombreNuevaCuenta = inputNombre.input.get()
        if checkUserInfo(1, nombreNuevaCuenta, "password", "codigo") == False:
            #Activa el input de Password
            inputPassword.baseInput.pack()

        else:
            ventanaError("nombre_existente")

    #Crear la cuenta
    def crearCuenta (info):
        #Info de la nueva cuenta
        nombre = inputNombre.input.get()
        password = inputPassword.input.get()
        codigo = codigoUsuario(4)

        ref.update({
            nombre:{
                'password': password, 
                'code': codigo,
                'money':{
                    'balance': 0,
                    'debt': 0,

                },

            },

        })

        #Base Cuenta creada
        baseCuentaCreada = t.Toplevel()
        baseCuentaCreada.title("¡Cuenta Creada!")

        #Titulo Cuenta Creada
        tituloCuentaCreada = plantilla_titulo(
            #Base de titulo; Tamaño de borde; Tipo de borde; Tamaño letra; Posición; Titular (contenido)
            baseCuentaCreada,2, "solid", 16, "center", "¡Cuenta Creada!", 
        )   
        
        #Texto Cuenta Creada
        textoCuentaCreada = plantilla_texto()
        textoCuentaCreada.textoSinBorde(
            #Base del texto; Mensaje del texto; Tamaño del texto; Padding; Align(side, anchor); Margin
            baseCuentaCreada, "Su cuenta ha sido correctamente creada.\nLa información de su cuenta es:", 12, 5, "top", "center", 10,
        )
        
        #Info Usuario
        baseInfoUsuario = t.Frame(baseCuentaCreada,
            #Border
            borderwidth = 1,
            relief = "solid",
            #Padding
            padx = 5,
            pady = 5,
        )
        baseInfoUsuario.pack(
            #Margin
            padx = 5,
            pady = 5,
        )

        textoNombreUsuario = plantilla_texto()
        textoNombreUsuario.textoConBorde(
            #Base del texto; Mensaje del texto; Tamaño del texto; Padding; Align(side, anchor); Margin; Tamaño del borde; Tipo de borde
            baseInfoUsuario, "Nombre del usuario:  " + nombre, 12, 5, "top", "center", 5, 1, "solid",
        )

        textoPasswordUsuario = plantilla_texto()
        textoNombreUsuario.textoConBorde(
            #Base del texto; Mensaje del texto; Tamaño del texto; Padding; Align(side, anchor); Margin; Tamaño del borde; Tipo de borde
            baseInfoUsuario, "Contraseña del usuario:  " + password, 12, 5, "top", "center", 5, 1, "solid",
        )

        textoCodigoUsuario = plantilla_texto()
        textoCodigoUsuario.textoConBorde(
            #Base del texto; Mensaje del texto; Tamaño del texto; Padding; Align(side, anchor); Margin; Tamaño del borde; Tipo de borde
            baseInfoUsuario, "Código del usuario:  " + codigo, 15, 5, "top", "center", 5, 1, "solid",
        )

        #Botón aceptar
        def kill ():
            baseCuentaCreada.destroy()
            baseCrearCuenta.destroy()
        
        btnAceptar = plantilla_botones()
        btnAceptar.botonAceptar(
            #Base botón; Función
            baseCuentaCreada, kill,
        )
            
    #Base Crear Nueva Cuenta
    baseCrearCuenta = t.Toplevel()
    baseCrearCuenta.title("Crear Nueva Cuenta")
    baseCrearCuenta.geometry('600x250')

    #Titulo Crear Cuenta

    tituloCrearCuenta = plantilla_titulo(
        #Base de titulo; Tamaño de borde; Tipo de borde; Tamaño letra; Posición; Titular (contenido)
        baseCrearCuenta, 2, "solid", 18, "center", "Crear una Nueva Cuenta", 
    )

    #Input del Nuevo Usuario

    #Input Nombre
    inputNombre = plantilla_userInput(
        #Base del input; Mensaje del label; Status del div(show || hide)
        baseCrearCuenta, "Ingrese el nombre de su nueva Cuenta:", "show"
    )
    inputNombre.input.bind('<Return>', nombreCheck)

    #Input Password (hidden)
    inputPassword = plantilla_userInput(
        #Base del input; Mensaje del label; Status del div(show || hide)
        baseCrearCuenta, "Ingrese la contraseña de su nueva Cuenta:", "hide", 
    )
    inputPassword.input.bind('<Return>', crearCuenta)

btnRegistrarse = plantilla_botones()
btnRegistrarse.botonOpciones(
    #Base botón; Texto botón; Tamaño letra; Función; H&W; Align; Margin (X, Y)
    baseBotonesOpciones, "Crear Cuenta", 12, menuCrearCuenta, 2, 30, "top", 20, 10,
)

def menuIniciarSesion ():
    #Menu Functions

    #Check sí nombre esta en db
    def nombreCheck (info):
        nombre = inputNombre.input.get()
        if checkUserInfo(1, nombre, "password", "code") == True:
            #Activa los inputs de Password & Código
            inputCodigo.baseInput.pack()
            inputPassword.baseInput.pack()
        
        else:
            ventanaError("nombre_noExistente")

    #Iniciar Sesion 
    def iniciarSesion (info):
        nombre = inputNombre.input.get()
        codigo = inputCodigo.input.get()
        password = inputPassword.input.get()
        if checkUserInfo(2, nombre, password, codigo) == True:
            #Base de Iniciar Menu
            baseIniciarMenu = t.Toplevel()
            baseIniciarMenu.title("¡Bienvenido " + nombre + "!")

            #Titulo Iniciar Menu
            tituloIniciarMenu = plantilla_titulo(
                #Base de titulo; Tamaño de borde; Tipo de borde; Tamaño letra; Posición; Titular (contenido)
                baseIniciarMenu, 2, "solid", 18, "center", "¡Bienvenido " + nombre + "!", 
            )

            #Texto Iniciar Menu
            textoIniciarMenu = plantilla_texto()
            textoIniciarMenu.textoSinBorde(
                #Base del texto; Mensaje del texto; Tamaño del texto; Padding; Align(side, anchor); Margin
                baseIniciarMenu,
                "Con tu cuenta, " + nombre + ", puedes:\n\n - Depositar Dinero en tu Cuenta.\n\n - Retirar Dinero en Efectivo de tu Cuenta.\n\n - Recibir Dinero de Otros Usuarios.\n\n - Depositar Dinero a Otros Usuarios.\n\n - Pedir Prestamos a nuestro Banco.\n\n - Poder Mirar el Balance en tu Cuenta.\n\n - Entre Otros...",
                12, 5, "top", "center", 5,
            )

            #Botón Aceptar
            def kill():
                #Inicia el menu del usuario
                menuUsuario(nombre, codigo)

                baseIniciarMenu.destroy()
                baseIniciarSesion.destroy()

            btnAceptar = plantilla_botones()
            btnAceptar.botonAceptar(
                #Base botón; Función
                baseIniciarMenu, kill,
            )

        else:
            ventanaError("passwordcodigo_mal")

    #Base IniciarSesion
    baseIniciarSesion = t.Toplevel()
    baseIniciarSesion.title("Iniciar Sesion")
    baseIniciarSesion.geometry('600x250')

    #Titulo iniciarSesion
    tituloIniciarSesion = plantilla_titulo(
        #Base de titulo; Tamaño de borde; Tipo de borde; Tamaño letra; Posición; Titular (contenido)
        baseIniciarSesion, 2, "solid", 18, "center", "Iniciar Sesion", 
    )

    #Input Info Usuario a Iniciar Sesion

    #Input Nombre
    inputNombre = plantilla_userInput(
        #Base del input; Mensaje del label; Status del div(show || hide)
        baseIniciarSesion, "Ingrese el nombre de su cuenta:", "show",
    )
    inputNombre.input.bind('<Return>', nombreCheck)

    #Input Código (Hidden)
    inputCodigo = plantilla_userInput(
        #Base del input; Mensaje del label; Status del div(show || hide)
        baseIniciarSesion, "Ingrese el código su cuenta:", "hide",
    )
    inputCodigo.input.bind('Return', iniciarSesion)

    #Input Password (Hidden)
    inputPassword = plantilla_userInput(
        #Base del input; Mensaje del label; Status del div(show || hide)
        baseIniciarSesion, "Ingrese la contraseña de su cuenta:", "hide",
    )
    inputPassword.input.bind('<Return>', iniciarSesion)

btnIniciarSesion = plantilla_botones()
btnIniciarSesion.botonOpciones(
    #Base botón; Texto botón; Tamaño letra; Función; H&W; Align; Margin (X, Y)
    baseBotonesOpciones, "Iniciar Sesion", 12, menuIniciarSesion, 2, 10, "right", 30, 10, 
)

def menuBorrarCuenta ():
    #Check sí cuenta a borrar existe
    def nombreCheck (info):
        nombre = inputNombre.input.get()
        if checkUserInfo(1, nombre, "password", "codigo") == True:
            inputCodigo.baseInput.pack()
            inputPassword.baseInput.pack()

        else:
            ventanaError("nombre_noExistente")

    #Borrar cuenta de dataBase
    def borrarCuenta (info):
        nombre = inputNombre.input.get()
        password = inputPassword.input.get()
        codigo = inputCodigo.input.get()
        if checkUserInfo(2, nombre, password, codigo) == True:
            #Borrar usuario de dataBase
            ref.child(nombre).delete()

            #Base ByeBye
            baseByeBye = t.Toplevel()
            baseByeBye.title("Hasta Luego " + nombre)

            #Titulo ByeBye
            tituloByeBye = plantilla_titulo(
                #Base de titulo; Tamaño de borde; Tipo de borde; Tamaño letra; Posición; Titular (contenido)
                baseByeBye, 2, "solid", 18, "center", "Hasta Luego " + nombre, 
            )

            #Despedida :c
            textoByeBye = plantilla_texto()
            textoByeBye.textoConBorde(
                #Base del texto; Mensaje del texto; Tamaño del texto; Padding; Align(side, anchor); Margin; Tamaño del borde; Tipo de borde
                baseByeBye,
                "Ojala nuestro camino se vuelva a encontrar " + nombre + ".\nPero, él que recorrimos juntos fue maravilloso.\nHasta Luego " + nombre,
                12, 15, "top", "center", 10, 2, "solid",
            )

            #Boton Aceptar
            def kill ():
                baseByeBye.destroy()
                baseBorrarCuenta.destroy()
            
            btnAceptar = plantilla_botones()
            btnAceptar.botonAceptar(
                #Base botón; Función
                baseByeBye, kill,
            )

        else:
            ventanaError("passwordcodigo_mal")    

    #Base Borrar Cuenta
    baseBorrarCuenta = t.Toplevel()
    baseBorrarCuenta.title("Borrar Cuenta")
    baseBorrarCuenta.geometry('600x250')

    #Titulo Borrar Cuenta

    tituloBorrarCuenta = plantilla_titulo(
        #Base de titulo; Tamaño de borde; Tipo de borde; Tamaño letra; Posición; Titular (contenido)
        baseBorrarCuenta, 2, "solid", 18, "center", "Borrar Cuenta", 
    )

    #Inputs Info del Usuario a borrar

    #Input Nombre
    inputNombre = plantilla_userInput(
        #Base del input; Mensaje del label; Status del div(show || hide)
        baseBorrarCuenta, "Ingrese el nombre de la cuenta a borrar:", "show",
    )
    inputNombre.input.bind('<Return>', nombreCheck)

    #Input Código (hidden)
    inputCodigo = plantilla_userInput(
        #Base del input; Mensaje del label; Status del div(show || hide)
        baseBorrarCuenta, "Ingrese el código de la cuenta a borrar:", "hide",
    )
    inputCodigo.input.bind('<Return>', borrarCuenta)

    #Input Password (hidden)
    inputPassword = plantilla_userInput(
        #Base del input; Mensaje del label; Status del div(show || hide)
        baseBorrarCuenta, "Ingrese la contraseña de la cuenta a borrar:", "hide",
    )
    inputPassword.input.bind('<Return>', borrarCuenta)

btnBorrarCuenta = plantilla_botones()
btnBorrarCuenta.botonOpciones(
    #Base botón; Texto botón; Tamaño letra; Función; H&W; Align; Margin (X, Y)
    baseBotonesOpciones, "Borrar Cuenta", 12, menuBorrarCuenta, 2, 10, "left", 30, 10, 
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


"""
baseMenuInicio.mainloop()