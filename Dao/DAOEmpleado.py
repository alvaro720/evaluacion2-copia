import mysql.connector
from credenciales import llaves
from conexiones import Conexion

from clases.Empleado import Empleado

class DAOEmpleado:
    def __init__(self):
        self.__conexion = None #conecta a db
        self.__cursor = None #ejecuta sql y obtiene registros
        
        self.__conectar()#

    def registrar_empleado(self, e:Empleado):

        self.__conectar()
        self.__cursor = self.__conexion.cursor()

        #definir query
        sql = "INSERT INTO empleado (nombre,rut,correo,contrasena,rol,telefono,salario,inicio_contrato,departamento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        datos = (e.get_nombre(),e.get_rut(),e.get_correo(),e.get_contrasena(),e.get_rol(),e.get_telefono(),e.get_salario(),e.get_inicio_contrato(),e.get_departamento()) #guardar en tupla

        #ejecutar query
        self.__cursor.execute(sql, datos)
        self.__conexion.commit()
        self.__desconectar()

    def obtener_empleado(self):

        self.__conectar()
        self.__cursor = self.__conexion.cursor()
        sql = "SELECT * FROM empleado"
        self.__cursor.execute(sql)

        respuesta = self.__cursor.fetchall()

        print(respuesta)

        empleados = []

        for e in respuesta:
            empleado = Empleado(e[0],e[1], e[2], e[3], e[4], e[5], e[6], e[7], e[8], e[9])
            empleados.append(empleado)

        return empleados

    def obtener_un_empleado(self, rut):

        self.__conectar()
        self.__cursor = self.__conexion.cursor()
        sql = "SELECT * FROM empleado WHERE rut = %s"
        datos = (rut,)
        self.__cursor.execute(sql, datos)

        respuesta = self.__cursor.fetchone()

        print(respuesta)

        if respuesta != None:

            empleado = Empleado(respuesta[0], respuesta[1], respuesta[2], respuesta[3], respuesta[4], respuesta[5], respuesta[6], respuesta[7], respuesta[8], respuesta[9])
            return empleado
    
    def actualizar_empleado(self,e:Empleado,):

        self.__conectar()
        self.__cursor = self.__conexion.cursor()

        sql = "Update empleado set nombre=%s, correo=%s, contrasena=%s, rol=%s, telefono=%s, salario=%s, inicio_contrato=%s, departamento=%s WHERE rut = %s"

        datos = (e.get_nombre(),e.get_correo(),e.get_contrasena(),e.get_rol(),e.get_telefono(),e.get_salario(),e.get_inicio_contrato(),e.get_departamento(),e.get_rut())
        self.__cursor.execute(sql,datos)
        self.__conexion.commit() # aplica los cambios
        self.__desconectar()
    
    def eliminar_empleado(self, rut):
        self.__conectar()
        self.__cursor = self.__conexion.cursor()

        sql = "Delete from empleado WHERE rut = %s"
        datos = (rut,)
        self.__cursor.execute(sql,datos)
        self.__conexion.commit()
        self.__desconectar()
