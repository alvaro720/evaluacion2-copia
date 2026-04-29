import mysql.connector
from credenciales import llaves
from conexiones import Conexion
from clases.Departamento import Departamento

class DAODepartamento:
    def __init__(self):
        self.__conexion = None
        self.__cursor = None
        self.__conectar()

    def registrar_departamento(self, d: Departamento):
        self.__conectar()
        self.__cursor = self.__conexion.cursor()
        sql = "INSERT INTO departamento (nombre, gerente) VALUES (%s, %s)"
        datos = (d.get_nombre(), d.get_gerente())
        self.__cursor.execute(sql, datos)
        self.__conexion.commit()
        self.__desconectar()

    def obtener_departamentos(self):
        self.__conectar()
        self.__cursor = self.__conexion.cursor()
        sql = "SELECT * FROM departamento"
        self.__cursor.execute(sql)
        respuesta = self.__cursor.fetchall()
        departamentos = []
        for r in respuesta:

            departamentos.append(Departamento(r[0], r[1], r[2]))
        return departamentos

    def obtener_un_departamento(self, nombre):
        self.__conectar()
        self.__cursor = self.__conexion.cursor()
        sql = "SELECT * FROM departamento WHERE nombre = %s"
        self.__cursor.execute(sql, (nombre,))
        r = self.__cursor.fetchone()
        if r is not None:
            return Departamento(r[0], r[1], r[2])
        return None

    def obtener_id_por_nombre(self, nombre):
        self.__conectar()
        self.__cursor = self.__conexion.cursor()
        sql = "SELECT id FROM departamento WHERE nombre = %s"
        self.__cursor.execute(sql, (nombre,))
        resultado = self.__cursor.fetchone()
        return resultado[0] if resultado else None

    def actualizar_departamento(self, d: Departamento):
        self.__conectar()
        self.__cursor = self.__conexion.cursor()

        sql = "UPDATE departamento SET gerente=%s WHERE nombre=%s"
        datos = (d.get_gerente(), d.get_nombre())
        self.__cursor.execute(sql, datos)
        self.__conexion.commit()
        self.__desconectar()

    def eliminar_departamento(self, nombre):
        self.__conectar()
        self.__cursor = self.__conexion.cursor()
        sql = "DELETE FROM departamento WHERE nombre = %s"
        self.__cursor.execute(sql, (nombre,))
        self.__conexion.commit()
        self.__desconectar()