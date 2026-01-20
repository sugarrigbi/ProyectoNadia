# ============================================================
# Autor: Kevin Mauricio Anzola Garzón
# Fecha: 08/08/2025
# Descripción: Programa en Python que administra animales en
#              un pequeño menú, permitiendo ver sus datos y
#              modificar su estado de salud.
# ============================================================
#Definición de la clase Animal
class Animal:
    #Constructor que inicializa los atributos de cada animal
    def __init__(self, nombre, especie, edad, salud):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.salud = salud
    #Método para mostrar los datos del animal
    def Mostrar_Datos(self):
        print(self.nombre, " / ", self.especie, " / ", self.edad, " / ", self.salud)
    #Método para actualizar el estado de salud del animal
    def Actualizar_Estado(self):
        while True:
            estado = input("Escriba la salud del animal(Bien, Regular, Mal):").strip().capitalize()
            #Validación del estado ingresado
            if estado not in ("Bien", "Regular", "Mal"):
                print("=======================================")
                print("Error, Ese estado de salud no es valido")
                print("=======================================")
            else:
                print("Estado de salud almacenado con exito")
                self.salud = estado
                break
#Creación de tres objetos de tipo Animal
Animal1 =  Animal("Roberto", "Leon", "4 Años", "Bien")
Animal2 =  Animal("Sara", "Tucan", "1 Años", "Regular")
Animal3 =  Animal("Steven", "Hiena", "6 Años", "Mal")
#Función que muestra el menú principal
def Menu():
    while True:
        #Opciones del menú
        print("1. Leer Datos Animales")
        print("2. Reescribir salud Animal")
        print("3. Salir")
        Respuesta = int(input("Que desea hacer: "))
        #Validación de opción ingresada
        if Respuesta not in (1, 2, 3):
            print("==============================")
            print("Error, Esa opcion no existe...")
            print("==============================")
        #Opción 1: Mostrar datos de todos los animales
        elif Respuesta == 1:
            print("=====")
            print("DATOS")
            print("=====")
            Animal1.Mostrar_Datos()
            Animal2.Mostrar_Datos()
            Animal3.Mostrar_Datos()
        #Opción 2: Actualizar la salud de un animal
        elif Respuesta == 2:
            print("=========")
            print("MODIFICAR")
            print("=========")
            print("1. ", Animal1.nombre)
            print("2. ", Animal2.nombre)
            print("3. ", Animal3.nombre)
            try:
                Respuesta_Animal = int(input("Selecciona un animal(1/2/3): "))
                #Validación de selección
                if Respuesta_Animal not in (1, 2, 3):
                    print("==============================")
                    print("Error, Esa opcion no existe...")
                    print("==============================")
                else:
                    #Llamada dinámica usando eval
                    eval(f"Animal{Respuesta_Animal}.Actualizar_Estado()")
            #Validacion de error
            except ValueError:
                print("==============================")
                print("Error: debes ingresar 1, 2 o 3")
                print("==============================")
        #Opción 3: Salir del programa
        elif Respuesta == 3:
            print("===========")
            print("Cerrando...")
            print("===========")
            break

#Punto de entrada del programa
if __name__ == "__main__":
    Menu()