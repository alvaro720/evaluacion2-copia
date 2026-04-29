from clases.Usuario import Usuario

class Empleado:
    def __init__(self,id,nombre,rut,correo,contrasena,rol,telefono,salario,inicio_contrato,departamento):
        super().__init__(id,nombre,rut,correo,contrasena,rol)

        self.__telefono = telefono
        self.__salario = salario
        self.__inicio_contrato = inicio_contrato
        self.__departamento = departamento

#telefono

    def get_telefono(self):
        return self.__telefono
    
    def set_telefono(self,telefono):
        self.__telefono = telefono

#salario

    def get_salario(self):
        return self.__salario
    
    def set_salario(self,salario):
        self.__salario = salario

#inicio_contrato

    def get_inicio_contrato(self):
        return self.__inicio_contrato
    
    def set_inicio_contrato(self,inicio_contrato):
        self.__inicio_contrato = inicio_contrato

#departamento

    def get_departamento(self):
        return self.__departamento
    
    def set_departamento(self,departamento):
        self.__departamento = departamento


