from Direccion import Direccion
from RegistroUsuarios import RegistroUsuarios
import csv


#direccion = Direccion("Calle Principal", 123, "A", "Centro", "Ciudad Ejemplo")

# Ejemplo de uso
#print(textoDescripcion)

class Main:
    def __init__(self):
        self.RegistroUsuarios = RegistroUsuarios(capacidad_maxima=8)

    def ejecutar(self):
        main.menuconsola()
        self.RegistroUsuarios.leerDatos()
        usuarios = self.RegistroUsuarios.getUsuarios()
        for usuario in usuarios:
            print(f"{usuario}")
        
        id = '123456890'
        buscar_usuario = self.RegistroUsuarios.buscar_usuario(id)
        #print(buscar_usuario)
        
        agregar_usuario = self.RegistroUsuarios.agregar_usuario()
        for usuario in usuarios:
            print(f"{usuario}")
        agregar_usuario = self.RegistroUsuarios.agregar_usuario()
        
        #eliminar_usuario = self.RegistroUsuarios.eliminar_usuario(id)
        
        #for usuario in usuarios:
        #    print(usuario)
        
        
        #if buscar_usuario==True:
        #    print('si esta')
        #else:
        #    print('No esta')
        
    """
    while True:
        entrada = int(input())
        if entrada==1:
            id = int(input())
            RegistroUsuarios.buscar_usuario()
        break
    """
    
    def menuconsola(self):
        textoDescripcion = f"Hola, bienvenido a la PRACTIA 1: REGISTRO DE USUARIOS:\n" \
                    f"¿Que deseas hacer?.\n" \
                    f"1. Agregar un nuevo usuario.\n" \
                    f"2. Eliminar un usuario.\n" \
                    f"3. Buscar informacion de usuario.\n" \
                    f"4. Almacenar el nuevo registro de usuario.\n" 
        print(textoDescripcion)

if __name__ == "__main__":
    main = Main()
    main.ejecutar()