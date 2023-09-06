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
                fila = row[0].split(';')  # Divide la fila usando ';' como separador
                fila = [elemento.strip() for elemento in fila]  # Elimina espacios adicionales
                usuario = Usuario(id=fila[0], nombre=fila[1], fecha_nac=fila[2], ciudad_nac=fila[3], direccion=fila[4], telefono=fila[5], email=fila[6])

                self._usuarios.append(usuario)  # Agrega la fila a la lista 'datos'
            
            self._usuarios.sort(key=lambda u: u._id)

    
    def getUsuarios(self):
        return self._usuarios
    
    
    def agregar_usuario(self):
        if len(self._usuarios) < self._capacidad_maxima:
            # Solicita id para verificar si el usuario existe o no, si no existe se procedera a pedir los datos de el usuario
            id = input("Ingrese el ID del usuario: ")
            if self.buscar_usuario(id)==None:
                # Solicita los datos del usuario al usuario
                nombre = input("Ingrese el nombre del usuario: ")
                ciudad_nac = input('Ingrese la ciudad donde nació: ')
                
                # Solicita datos de la fecha al usuario
                dd = input("Ingrese el día (dd): ")
                mm = input("Ingrese el mes (mm): ")
                aaaa = input("Ingrese el año (aaaa): ")
                
                
                # Crea una instancia de la clase Fecha con los datos ingresados por el usuario
                fecha_usuario = Fecha(dd=dd, mm=mm, aaaa=aaaa)
                
                # Solicita datos de dirección al usuario
                calle = input("Ingrese la calle: ")
                noCalle = input("Ingrese el número de la calle: ")
                nomenclatura = input("Ingrese la nomenclatura: ")
                barrio = input("Ingrese el barrio: ")
                ciudad = input("Ingrese la ciudad: ")
                
                
                # Crea una instancia de la clase Direccion con los datos ingresados por el usuario
                direccion_usuario = Direccion(calle=calle, noCalle=noCalle, nomenclatura=nomenclatura, barrio=barrio, ciudad=ciudad)
                
                # Solicita los otros datos del usuario al usuario
                telefono = input("Ingrese el teléfono del usuario: ")
                email = input("Ingrese el correo electrónico del usuario: ")
                
                # Crea una instancia de la clase Usuario utilizando los objetos ya obtenidos
                usuario = Usuario(id=id, nombre=nombre, fecha_nac=fecha_usuario, ciudad_nac=ciudad_nac, direccion=direccion_usuario, telefono=telefono, email=email)
                
                self._usuarios.append(usuario)
                self._usuarios.sort(key=lambda u: u._id)
                return True
            else:
                print("Ya existe un usuario con esa identificación.")
        else:
            print("El registro está lleno, no se puede agregar más usuarios.")
        return False
    
    def pedirDatosUsuario(self, Usuario):
        # Solicita los datos del usuario al usuario
        id = input("Ingrese el ID del usuario: ")
        nombre = input("Ingrese el nombre del usuario: ")
        ciudad_nac = input('Ingrese la ciudad donde nació: ')
        
        # Solicita datos de la fecha al usuario
        dd = input("Ingrese el día (dd): ")
        mm = input("Ingrese el mes (mm): ")
        aa = input("Ingrese el año (aa): ")
        
        
        # Crea una instancia de la clase Fecha con los datos ingresados por el usuario
        fecha_usuario = Fecha(dd=dd, mm=mm, aa=aa)
        
        # Solicita datos de dirección al usuario
        calle = input("Ingrese la calle: ")
        noCalle = input("Ingrese el número de la calle: ")
        nomenclatura = input("Ingrese la nomenclatura: ")
        barrio = input("Ingrese el barrio: ")
        ciudad = input("Ingrese la ciudad: ")
        
        
        # Crea una instancia de la clase Direccion con los datos ingresados por el usuario
        direccion_usuario = Direccion(calle=calle, noCalle=noCalle, nomenclatura=nomenclatura, barrio=barrio, ciudad=ciudad)
        
        # Solicita los otros datos del usuario al usuario
        telefono = input("Ingrese el teléfono del usuario: ")
        email = input("Ingrese el correo electrónico del usuario: ")
        
        # Crea una instancia de la clase Usuario utilizando los objetos ya obtenidos
        return   Usuario(id=id, nombre=nombre, fecha_nac=fecha_usuario, ciudad_nac=ciudad_nac, direccion=direccion_usuario, telefono=telefono, email=email)
    
    
    def buscar_usuario(self, id):
        for i in self._usuarios:
            if i._id==id:
                #print(i)
                return i
            else:
                return None
        #return None
    
    
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
