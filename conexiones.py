import mysql.connector
from credenciales import llaves

class Conexion:
    def __init__(self):
        self.__conexion = None #conecta a db
        self.__cursor = None #ejecuta sql y obtiene registros
        
        self.__conectar()#


#conexion a la base de datos
    def __conectar(self):
        try:
            #reemplazar con credenciales
            self.__conexion = mysql.connector.connect(
                host = llaves["host"],
                user = llaves["usuario"],
                password = llaves["contrasena"],
                database = llaves["db"]
    )
            
            if self.__conexion.is_connected():
                print("conectado")
        
        except mysql.connector.Error as e:
            print(f"error al conectarse a {e}")

#desconexion a la base de datos                  
    def __desconectar(self):
        try:
            if self.__conexion and self.__conexion.is_connected():
                self.__conexion.close()
                  
        except mysql.connector.Error as e:
            print(f"error al desconectarse de {e}")