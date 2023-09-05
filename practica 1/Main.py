from Direccion import Direccion
from RegistroUsuarios import RegistroUsuarios
import csv


textoDescripcion = f"Hola, bienvenido a la PRACTIA 1: REGISTRO DE USUARIOS:\n" \
                    f"¿Que deseas hacer?.\n" \
                    f"1. Agregar un nuevo usuario.\n" \
                    f"2. Eliminar un usuario.\n" \
                    f"3. Buscar informacion de usuario.\n" \
                    f"4. Almacenar el nuevo registro de usuario.\n" 




# Abre el archivo CSV en modo lectura
with open('practica 1/usuarios.csv', mode='r', newline='') as file:
    # Crea un objeto CSV Reader
    csv_reader = csv.reader(file)
    
    # Itera a través de las filas del archivo CSV
    for row in csv_reader:
        RegistroUsuarios.agregar_usuario()
        # Imprime cada fila (que son listas)
        #print(row)


# Ejemplo de uso
print(textoDescripcion)
direccion = Direccion("Calle Principal", 123, "A", "Centro", "Ciudad Ejemplo")
print(direccion.to_string())