

class Usuario:
    def __init__(self, id, nombre, fecha_nac, ciudad_nac, direccion, telefono, email):
        #Datos necesarios para identificar al usuario
        self._id = id
        self._nombre = nombre
        self._fechaNac = fecha_nac
        self._ciudadNac = ciudad_nac
        self._direccion = direccion
        self._telefono = telefono
        self._email = email
    
    def getId(self):
        return self._id
    def setId(self, id):
        self._id = id
    
    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getFechaNac(self):
        return self._fechaNac
    def setFechaNac(self, _fechaNac):
        self._fechaNac = fechaNac
    
    def setCiudadNac(self):
        return self.ciudadNac
    def setCiudadNac(self, ciudadNac):
        self._ciudadNac = ciudadNac
    
    def getDireccion(self):
        return self._direccion
    def setDireccion(self, direccion):
        self._direccion = direccion
    
    def getTelefono(self):
        return self._telefono
    def setTelefono(self, telefono):
        self._telefono = telefono
    
    def getEmail(self):
        return self._email
    def setEmail(self, email):
        self._email = email
    
    def toString(self):
        return toString
