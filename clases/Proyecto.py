class Proyecto:
    def __init___(self,id,nombre,descripcion,fecha_inicio):
        self.__id = id
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__fecha_inicio = fecha_inicio

#id

    def get_id(self):
        return self.__id
    
    def set_id(self,id):
        self.__id = id

#nombre

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nombre):
        self.__nombre = nombre

#descripcion

    def get_descripcion(self):
        return self.__descripcion
    
    def set_descripcion(self,descripcion):
        self.__descripcion = descripcion

#fecha_inicio

    def get_fecha_inicio(self):
        return self.__fecha_inicio
    
    def set_fecha_inicio(self,fecha_inicio):
        self.__fecha_inicio = fecha_inicio
