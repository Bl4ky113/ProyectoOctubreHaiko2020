
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from time import sleep



# Fetch the service account key JSON file contents
cred = credentials.Certificate('C:/Users/diana/haiko/proyectoOctubre/firebase_python/clave_Json/clave.json')
# Initialize the app with a service account, granting admin privileges       
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://proyecto-haiko-base-de-datos.firebaseio.com/'
})

mensajeA = db.reference('usuarios/Angel/enviado/eMenasajeM')
enviarM = input("mensaje")


refA = db.reference("usuarios")
refA.update({
    #Angel
    'Angel':{
        'enviado': {
            'eMensajeM': enviarM
        }
    }
