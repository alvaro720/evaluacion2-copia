import mysql.connector
from credenciales import llaves
from conexiones import Conexion
from clases.Registro import Registro

class DAORegistro:
    def __init__(self):
        self.__conexion = None
        self.__cursor = None
        self.__conectar()

    def registrar_registro(self, r: Registro):
        self.__conectar()
        self.__cursor = self.__conexion.cursor()
        sql = "INSERT INTO registro (fecha, hora, descripcion, empleado, proyecto) VALUES (%s, %s, %s, %s, %s)"
        datos = (r.get_fecha(), r.get_hora(), r.get_descripcion(), r.get_empleado(), r.get_proyecto())
        self.__cursor.execute(sql, datos)
        self.__conexion.commit()
        self.__desconectar()

    def obtener_registros(self):
        self.__conectar()
        self.__cursor = self.__conexion.cursor()
        sql = "SELECT * FROM registro"
        self.__cursor.execute(sql)
        respuesta = self.__cursor.fetchall()
        registros = []
        for r in respuesta:
            # id, fecha, hora, descripcion, empleado, proyecto
            registros.append(Registro(r[0], r[1], r[2], r[3], r[4], r[5]))
        return registros

    def obtener_ids_por_empleado(self, rut_empleado):
        self.__conectar()
        self.__cursor = self.__conexion.cursor()
        sql = "SELECT id FROM registro WHERE empleado = %s"
        self.__cursor.execute(sql, (rut_empleado,))
        resultados = self.__cursor.fetchall()
        return [r[0] for r in resultados]

    def obtener_un_registro_por_id(self, id):
        self.__conectar()
        self.__cursor = self.__conexion.cursor()
        sql = "SELECT * FROM registro WHERE id = %s"
        self.__cursor.execute(sql, (id,))
        r = self.__cursor.fetchone()
        if r is not None:
            return Registro(r[0], r[1], r[2], r[3], r[4], r[5])
        return None

    def actualizar_registro(self, r: Registro):
        self.__conectar()
        self.__cursor = self.__conexion.cursor()
        # Se usa ID en el WHERE ya que un registro no tiene clave natural única
        sql = "UPDATE registro SET fecha=%s, hora=%s, descripcion=%s, empleado=%s, proyecto=%s WHERE id=%s"
        datos = (r.get_fecha(), r.get_hora(), r.get_descripcion(), r.get_empleado(), r.get_proyecto(), r.get_id())
        self.__cursor.execute(sql, datos)
        self.__conexion.commit()
        self.__desconectar()

    def eliminar_registro(self, id):
        self.__conectar()
        self.__cursor = self.__conexion.cursor()
        sql = "DELETE FROM registro WHERE id = %s"
        self.__cursor.execute(sql, (id,))
        self.__conexion.commit()
        self.__desconectar()