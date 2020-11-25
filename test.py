import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('C:/Users/diana/haiko/proyectoOctubre/proyecto/clave_Json/clave.json')
# Initialize the app with a service account, granting admin privileges       
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://proyecto-haiko-base-de-datos.firebaseio.com/'
})

print(" 'a' para crear una nueva cuenta \n'b' para ingresar en su cuenta")
accion = input("Ingrese que accion quiere realizar")

ref = db.reference("Usuarios")

if accion == 'a':
    nombreNewU = input("Ingrese el nombre del usuario")
    passwordNewU = int(input("Ingrese su contraseña"))
    codigoNewU = 10
    ref.update({
        nombreNewU:{
            'password': passwordNewU, 
            'codigo': codigoNewU,
            },
        })

usuarios = ref.get()
print(type(usuarios))
print(usuarios)
    



