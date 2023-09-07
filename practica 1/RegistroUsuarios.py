from Usuario import Usuario
from Direccion import Direccion
from Fecha import Fecha

import csv

class RegistroUsuarios:
    def __init__(self, capacidad_maxima):
        self._capacidad_maxima = capacidad_maxima
        self._usuarios = []
    
    def leerDatos(self):
        # Abre el archivo CSV en modo lectura
        with open('practica 1/usuarios.csv', mode='r', newline='') as file:
            # Crea un objeto CSV Reader
            csv_reader = csv.reader(file)
            # Lee la primera fila (fila de encabezado) y omítela
            next(csv_reader)
            
            # Itera a través de las filas del archivo CSV
            for row in csv_reader:
                fila = [elemento.strip() for elemento in row]  # Elimina espacios adicionales
                usuario = Usuario(id=int(fila[0]), nombre=fila[1], fecha_nac=fila[2], ciudad_nac=fila[3], direccion=fila[4], telefono=fila[5], email=fila[6])

                self._usuarios.append(usuario)  # Agrega la fila a la lista 'datos'
            
            self._usuarios.sort(key=lambda u: u._id)

    
    def getUsuarios(self):
        return self._usuarios
    
    
    def agregar_usuario(self):
        # Se verifica que haya espacio para agregar un usuario
        if len(self._usuarios) < self._capacidad_maxima:
            
            # Solicita id para verificar si el usuario existe o no, si no existe se procedera a pedir los datos de el usuario para registrarlo
            id = int(input("Ingrese el ID del Usuario: "))
            if self.buscar_usuario(id)==None:
                # Solicita los datos del usuario al usuario
                nombre = input("Ingrese el nombre del Usuario: ")
                ciudad_nac = input('Ingrese la ciudad donde nació: ')
                
                # Solicita datos de la fecha de nacimiento del usuario
                dd = input("Ingrese el día de nacimiento (dd): ")
                mm = input("Ingrese el mes de nacimiento (mm): ")
                aaaa = input("Ingrese el año de nacimiento (aaaa): ")
                
                # Crea una instancia de la clase Fecha con los datos ingresados por el usuario anteriormente
                fecha_usuario = Fecha(dd=dd, mm=mm, aaaa=aaaa)
                
                # Solicita datos de dirección del usuario
                calle = input("Ingrese la calle: ")
                noCalle = input("Ingrese el número de la calle: ")
                nomenclatura = input("Ingrese la nomenclatura: ")
                barrio = input("Ingrese el barrio: ")
                ciudad = input("Ingrese la ciudad: ")
                
                # Crea una instancia de la clase Direccion con los datos ingresados por el usuario anteriormente
                direccion_usuario = Direccion(calle=calle, noCalle=noCalle, nomenclatura=nomenclatura, barrio=barrio, ciudad=ciudad)
                
                # Solicita los otros datos del usuario
                telefono = input("Ingrese el teléfono del usuario: ")
                email = input("Ingrese el Email del usuario: ")
                
                # Crea una instancia de la clase Usuario utilizando los objetos ya obtenidos
                usuario = Usuario(id=id, nombre=nombre, fecha_nac=fecha_usuario, ciudad_nac=ciudad_nac, direccion=direccion_usuario, telefono=telefono, email=email)
                
                self._usuarios.append(usuario) #se agrega el usuario a la lista de usuarios
                self._usuarios.sort(key=lambda u: u._id) #se ordena los usuarios de forma ascendente segun su ID
                print("¡Usuario registrado correctamente!")
            else:
                print("Ya existe un usuario con ese ID.")
        else:
            print("El registro está lleno, no se puede agregar más usuarios.")
    
    def buscar_usuario(self, id):
        for i in self._usuarios:
            if i._id==id:
                return i # Devuelve el usuario si se encuentra
        return None # Devuelve None solo si no se encuentra 
    
    
    def eliminar_usuario(self, id):
        usuario = self.buscar_usuario(id)
        if usuario:
            self._usuarios.remove(usuario)
            print("¡Usuario eliminado con exito!")
        
        else:
            print("No se encontró un usuario con esa identificación.")
    
    
    def guardarDatos(self):
        # Abre el archivo CSV en modo escritura
        with open('practica 1/usuarios.csv', mode='w', newline='') as file:
            # Crea un objeto CSV Writer
            csv_writer = csv.writer(file)

            # Escribe la fila de encabezado
            csv_writer.writerow(["ID", "Nombre", "Fecha de Nacimiento", "Ciudad de Nacimiento", "Dirección", "Teléfono", "Email"])

            # Escribe cada usuario en el archivo CSV
            for usuario in self._usuarios:
                csv_writer.writerow([usuario._id, usuario._nombre, usuario._fechaNac, usuario._ciudadNac, usuario._direccion, usuario._telefono, usuario._email])
