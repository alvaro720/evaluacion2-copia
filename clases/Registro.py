class Registro:
    def __init__(self,id,fecha,hora,descripcion,empleado,proyecto):
        self.__id = id
        self.__fecha = fecha
        self.__hora = hora
        self.__descripcion = descripcion
        self.__empleado = empleado
        self.__proyecto = proyecto

    
#id

    def get_id(self):
        return self.__id
    
    def set_id(self,id):
        self.__id = id

#fecha

    def get_fecha(self):
        return self.__fecha
    
    def set_fecha(self,fecha):
        self.__fecha = fecha

#hora

    def get_hora(self):
        return self.__hora
    
    def set_hora(self,hora):
        self.__hora = hora

#descripcion

    def get_descripcion(self):
        return self.__descripcion
    
    def set_descripcion(self,descripcion):
        self.__descripcion = descripcion

#empleado

    def get_empleado(self):
        return self.__empleado
    
    def set_empleado(self,empleado):
        self.__empleado = empleado

#proyecto

    def get_proyecto(self):
        return self.__proyecto
    
    def set_proyecto(self,proyecto):
        self.__proyecto = proyecto