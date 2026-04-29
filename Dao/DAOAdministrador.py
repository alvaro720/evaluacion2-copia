import mysql.connector
from credenciales import llaves
from conexiones import Conexion
from Seguridad import Seguridad 
from clases.Administrador import Administrador


class DAOAdministrador(Conexion):
    def __init__(self):
        super().__init__() 

    def validar_login(self, nombre, clave_plana):
        sql = "SELECT id, nombre, rol, contrasena FROM usuarios WHERE nombre = %s"
        
        try:
            self._Conexion__conectar() 
            self._Conexion__cursor.execute(sql, (nombre,))
            fila = self._Conexion__cursor.fetchone()
            self._Conexion__desconectar()

            if fila:
                if Seguridad.validar_clave(clave_plana, fila[3]):
                    return Administrador(fila[0], fila[1], "", "", fila[2])
            
        except Exception as e:
            print(f"Error: {e}")
            
        return None

    def registrar_administrador(self, a: Administrador):
        self.__conectar()
        self.__cursor = self.__conexion.cursor()
        sql = "INSERT INTO administrador (nombre, rut, correo, contrasena, rol) VALUES (%s, %s, %s, %s, %s)"
        datos = (a.get_nombre(), a.get_rut(), a.get_correo(), a.get_contrasena(), a.get_rol())
        self.__cursor.execute(sql, datos)
        self.__conexion.commit()
        self.__desconectar()

    def obtener_administradores(self):
        self.__conectar()
        self.__cursor = self.__conexion.cursor()
        sql = "SELECT * FROM administrador"
        self.__cursor.execute(sql)
        respuesta = self.__cursor.fetchall()
        administradores = []
        for r in respuesta:
            obj = Administrador(r[0], r[1], r[2], r[3], r[4], r[5])
            administradores.append(obj)
        return administradores

    def obtener_un_administrador(self, rut):
        self.__conectar()
        self.__cursor = self.__conexion.cursor()
        sql = "SELECT * FROM administrador WHERE rut = %s"
        self.__cursor.execute(sql, (rut,))
        r = self.__cursor.fetchone()
        if r:
            return Administrador(r[0], r[1], r[2], r[3], r[4], r[5])
        return None

    def actualizar_administrador(self, a: Administrador):
        self.__conectar()
        self.__cursor = self.__conexion.cursor()
        sql = "UPDATE administrador SET nombre=%s, correo=%s, contrasena=%s, rol=%s WHERE rut=%s"
        datos = (a.get_nombre(), a.get_correo(), a.get_contrasena(), a.get_rol(), a.get_rut())
        self.__cursor.execute(sql, datos)
        self.__conexion.commit()
        self.__desconectar()

    def eliminar_administrador(self, rut):
        self.__conectar()
        self.__cursor = self.__conexion.cursor()
        sql = "DELETE FROM administrador WHERE rut = %s"
        self.__cursor.execute(sql, (rut,))
        self.__conexion.commit()
        self.__desconectar()