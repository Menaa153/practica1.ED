from Usuario import Usuario

class RegistroUsuarios:
    def __init__(self, capacidad_maxima):
        self._capacidad_maxima = 8
        self._usuarios = []
    
    def agregar_usuario(self, usuario):
        if len(self.usuarios) < self.capacidad_maxima:
            if not self.buscar_usuario(usuario.id):
                self._usuarios.append(usuario)
                self._usuarios.sort(key=lambda u: u.id)
                return True
            else:
                print("Ya existe un usuario con esa identificación.")
        else:
            print("El registro está lleno, no se puede agregar más usuarios.")
        return False

    def buscar_usuario(self, id):
        for usuario in self._usuarios:
            if usuario.id == id:
                return usuario
        return None

    def eliminar_usuario(self, id):
        usuario = self.buscar_usuario(id)
        if usuario:
            self._usuarios.remove(usuario)
            return True
        else:
            print("No se encontró un usuario con esa identificación.")
            return False

    def guardar_en_archivo(self, archivo_nombre):
        with open(archivo_nombre, 'w') as archivo:
            for usuario in self.usuarios:
                archivo.write(f"{usuario.id},{usuario.nombre},{usuario.fecha_nacimiento},{usuario.ciudad_nacimiento},{usuario.direccion},{usuario.telefono},{usuario.correo}\n")

    def cargar_desde_archivo(self, archivo_nombre):
        with open(archivo_nombre, 'r') as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                campos = linea.strip().split(',')
                if len(campos) == 7:
                    id, nombre, fecha_nacimiento, ciudad_nacimiento, direccion, telefono, correo = campos
                    usuario = Usuario(id, nombre, fecha_nacimiento, ciudad_nacimiento, direccion, telefono, correo)
                    self.agregar_usuario(usuario)