class Departamento:
    def __init__(self,id,nombre,gerente):
        self.__id = id
        self.__nombre = nombre
        self.__gerente = gerente

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

#gerente

    def get_gerente(self):
        return self.__gerente
    
    def set_gerente(self,gerente):
        self.__gerente = gerente