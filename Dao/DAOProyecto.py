import mysql.connector
from credenciales import llaves
from conexiones import Conexion
from clases.Proyecto import Proyecto

class DAOProyecto:
    def __init__(self):
        self.__conexion = None
        self.__cursor = None
        self.__conectar()

    def registrar_proyecto(self, p: Proyecto):
        self.__conectar()
        self.__cursor = self.__conexion.cursor()
        sql = "INSERT INTO proyecto (nombre, descripcion, fecha_inicio) VALUES (%s, %s, %s)"
        datos = (p.get_nombre(), p.get_descripcion(), p.get_fecha_inicio())
        self.__cursor.execute(sql, datos)
        self.__conexion.commit()
        self.__desconectar()

    def obtener_proyectos(self):
        self.__conectar()
        self.__cursor = self.__conexion.cursor()
        sql = "SELECT * FROM proyecto"
        self.__cursor.execute(sql)
        respuesta = self.__cursor.fetchall()
        proyectos = []
        for r in respuesta:

            proyectos.append(Proyecto(r[0], r[1], r[2], r[3]))
        return proyectos

    def obtener_un_proyecto(self, nombre):
        self.__conectar()
        self.__cursor = self.__conexion.cursor()
        sql = "SELECT * FROM proyecto WHERE nombre = %s"
        self.__cursor.execute(sql, (nombre,))
        r = self.__cursor.fetchone()
        if r is not None:
            return Proyecto(r[0], r[1], r[2], r[3])
        return None

    def obtener_id_por_nombre(self, nombre):
        self.__conectar()
        self.__cursor = self.__conexion.cursor()
        sql = "SELECT id FROM proyecto WHERE nombre = %s"
        self.__cursor.execute(sql, (nombre,))
        resultado = self.__cursor.fetchone()
        return resultado[0] if resultado else None

    def actualizar_proyecto(self, p: Proyecto):
        self.__conectar()
        self.__cursor = self.__conexion.cursor()
        sql = "UPDATE proyecto SET descripcion=%s, fecha_inicio=%s WHERE nombre=%s"
        datos = (p.get_descripcion(), p.get_fecha_inicio(), p.get_nombre())
        self.__cursor.execute(sql, datos)
        self.__conexion.commit()
        self.__desconectar()

    def eliminar_proyecto(self, nombre):
        self.__conectar()
        self.__cursor = self.__conexion.cursor()
        sql = "DELETE FROM proyecto WHERE nombre = %s"
        self.__cursor.execute(sql, (nombre,))
        self.__conexion.commit()
        self.__desconectar()