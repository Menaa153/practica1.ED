from Direccion import Direccion
from RegistroUsuarios import RegistroUsuarios
import csv


class Main:
    def __init__(self):
        self.RegistroUsuarios = RegistroUsuarios(capacidad_maxima=9)
    
    def main():
        while True:
            self.RegistroUsuarios.leerDatos()
            print("\nMenú:")
            print("1. Agregar persona")
            print("2. Mostrar personas")
            print("3. Eliminar persona")
            print("4. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                id = '1234567890'
                buscar_usuario = self.RegistroUsuarios.buscar_usuario(id)
            elif opcion == "2":
                id = '1234567890'
                buscar_usuario = self.RegistroUsuarios.buscar_usuario(id)
                print(buscar_usuario)
            elif opcion == "3":
                eliminar_usuario = self.RegistroUsuarios.eliminar_usuario(id)
            elif opcion == "4":
                break
            else:
                print("Opción no válida. Intente de nuevo.")

        main.menuconsola()
        
        usuarios = self.RegistroUsuarios.getUsuarios()
        for usuario in usuarios:
            print(f"{usuario}")
        
        id = '1234567890'
        buscar_usuario = self.RegistroUsuarios.buscar_usuario(id)
        print(buscar_usuario)
        
        agregar_usuario = self.RegistroUsuarios.agregar_usuario()
        for usuario in usuarios:
            print(f"{usuario}")
        agregar_usuario = self.RegistroUsuarios.agregar_usuario()
        guardarDatos= self.RegistroUsuarios.guardarDatos()
        
        #eliminar_usuario = self.RegistroUsuarios.eliminar_usuario(id)
        
        
        
        #if buscar_usuario==True:
        #    print('si esta')
        #else:
        #    print('No esta')
        
if __name__ == "__main__":
    main = Main()