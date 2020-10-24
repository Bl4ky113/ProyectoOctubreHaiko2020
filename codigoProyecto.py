import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from time import sleep

# Fetch the service account key JSON file contents
cred = credentials.Certificate('C:/Users/diana/OneDrive/Documentos/Haiko/proyectoOctubre/proyecto/clave_Json/clave.json')
# Initialize the app with a service account, granting admin privileges       
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://proyecto-haiko-base-de-datos.firebaseio.com/'
})

ref = db.reference("Usuarios")
usuarios = ref.get()
userName = []
tiempoIntervalo = 2.5

#Menu de Usuario

def menuUsuario():
    print("'a' para ingresar dinero a su cuenta. \n'b' para depositar dinero en otra cuenta \n'c' para verificar el balance en su cuenta")
    menu = input("Su opción es:   ")
    global money_ref 
    money_ref = db.reference("Usuarios/" + userName + "/dinero")
    money = money_ref.get()

    #Agrega balance, si tiene Deuda se resta a esta y se agrega lo que deje a balance

    if menu == 'a':
        sumaMoney = int(input("Digite el monto a ingresar:   "))
        totalMoney = usuarios[userName]['dinero']['balance'] + sumaMoney
        money_ref.set({
            'balance':totalMoney,

        })
        print("Listo!! su balance ha sido actualizado")
        menuUsuario()

    #Enviar dinero a otra cuenta con cd y nm, Si deposito < balance, se acumula deuda

    if menu == 'b':
        print("Ingrese el nombre y código de la cuenta a la cual depositara dinero")
        nombreDeposito = input("Nombre de la cuenta:   ")
        codigoDeposito = int(input("Código de la cuenta:   "))
        if nombreDeposito in usuarios and codigoDeposito == usuarios[nombreDeposito]['codigo']:
            print("Listo! Ahora necesitamos que digite la cantidad de dinero que va a depositar a ",nombreDeposito)
            cantidadDeposito = int(input("Cantidad de dinero a depositar:   "))
            if cantidadDeposito < money['balance']:
                print("hello")

    #Ver balance total = balance - Deuda
    elif menu == 'c':
        print("El balance en su cuenta es de:   ", usuarios[userName]['dinero'])

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
            codigoNewU = 10
            ref.update({
                nombreNewU:{
                    'password': passwordNewU, 
                    'codigo': codigoNewU,
                    'dinero':{
                        'balance': 0,
                        } ,
                    },
                })
            print("Listo! Su usuario es: ", nombreNewU, "\nSu codigo es: ", codigoNewU) 
            sleep(tiempoIntervalo)
            menuInicio()   
    
    elif accion.lower() == 'b':
        nombreSignIn = input("Ingrese el nombre de usuario de su cuenta:  ")
        codigoSignIn = int(input("Ingrese el codigo de su cuenta:  "))    
        if nombreSignIn in usuarios and codigoSignIn == usuarios[nombreSignIn]['codigo']:
            passwordSignIn = int(input("Ingrese la constraseña de su cuenta:  "))
            if passwordSignIn == usuarios[nombreSignIn]['password']:
                print("Bienvenido Usuario: ", nombreSignIn)
                global userName
                userName = nombreSignIn
                menuUsuario()
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

menuInicio()
