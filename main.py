class Cliente:
    '''
    Clase que crea objetos de tipo cliente
    '''

    def __init__(self, nombre: str, apellido: str, cedula: str, email: str,
                 vip: bool = False, direccion: str = None,
                 telefono: str = None, celular: str = None, edad: int = None):
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._email = email
        self._vip = vip
        self._direccion = direccion
        self._telefono = telefono
        self._celular = celular
        self._edad = edad

    def __str__(self):
        return f'Cliente [{self.__dict__.__str__()}]'

    # nombre
    # método que permite conocer o ver el atributo nombre
    @property
    def nombre(self):
        return self._nombre

    # método que permite modificar el valor de nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    #  apellido
    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, nuevo_apellido):
        self._apellido = nuevo_apellido

    #  cedula
    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, nueva_cedula):
        self._cedula = nueva_cedula

    #  email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, nuevo_email):
        self._email = nuevo_email

    #  vip
    @property
    def vip(self):
        return self._vip

    @vip.setter
    def vip(self, nuevo_vip):
        self._vip = nuevo_vip

    #  direccion
    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, nueva_direccion):
        self._direccion = nueva_direccion

    #  telefono
    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, nuevo_telefono):
        self._telefono = nuevo_telefono

    #  celular
    @property
    def celular(self):
        return self._celular

    @celular.setter
    def celular(self, nuevo_celular):
        self._celular = nuevo_celular

    #  edad
    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad


#  Resultado
if __name__ == '__main__':
    cliente1 = Cliente(nombre="Maria", apellido="Paz", cedula="0987654321",
                       email='maria@mail.com',
                       vip=True, direccion='Centro', telefono='0425566778899',
                       celular='0993344556677')
    print(cliente1)