class Usuario:
    def __init__(self,id,nombre,rut,correo,contrasena,rol):
        self.__id = id
        self.__nombre = nombre
        self.__rut = rut
        self.__correo = correo
        self.__contrasena = contrasena
        self.__rol = rol


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

#rut

    def get_rut(self):
        return self.__rut
    
    def set_rut(self,rut):
        self.__rut = rut

#correo

    def get_correo(self):
        return self.__correo
    
    def set_correo(self,correo):
        self.__correo = correo

#contraseña

    def get_contrasena(self):
        return self.__contrasena
    
    def set_contrasena(self,contrasena):
        self.__contrasena = contrasena

#rol

    def get_rol(self):
        return self.__rol
    
    def set_rol(self,rol):
        self.__rol = rol

