def sumar(numeros):
    Resultado = numeros[0]
    for i in numeros:
        Resultado += i
    return Resultado

def restar(numeros):
    Resultado = numeros[0]
    for i in numeros[1:]:
        Resultado -= i
    return Resultado

def multiplicar(numeros):
    Resultado = numeros[0]
    for i in numeros:
        Resultado *= i
    return Resultado

def dividir(numeros):
    Resultado = numeros[0]
    for i in numeros[1:]:
        if i == 0:
            return "Error: No se puede dividir entre cero"
        Resultado /= i
    return Resultado

def mostrar_menu():
    print("\nCalculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def obtener_numeros():
    numeros = []
    print("Introduce los números (escribe 'fin' para terminar):")
    while True:
        entrada = input(": ")
        if entrada.lower() == 'fin':
            if len(numeros) < 2:
                print("Debes ingresar al menos dos números")
                continue
            break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Error: Ingresa un número o 'fin'.")
    return numeros

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "5":
            print("¡Hasta luego!")
            break
        if opcion not in ["1", "2", "3", "4"]:
            print("Opción no válida. Intenta de nuevo.")
            continue
        numeros = obtener_numeros()
        if opcion == "1":
            resultado = sumar(numeros)
        elif opcion == "2":
            resultado = restar(numeros)
        elif opcion == "3":
            resultado = multiplicar(numeros)
        elif opcion == "4":
            resultado = dividir(numeros)

        print("Resultado:", resultado)

if __name__ == "__main__":
    main()