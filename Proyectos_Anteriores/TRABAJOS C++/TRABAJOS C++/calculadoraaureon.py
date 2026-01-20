
Valor_Sumado = 0
Valor = 0

def pedir_valores():
    global Costo_Base, Nivel_Maximo, Potencia_Base
    Costo_Base = int(input("Ingrese el Costo Base: "))
    Nivel_Maximo = int(input("Ingrese el Nivel Maximo: "))
    Potencia_Base = float(input("Ingrese la potencia: "))
def main():
    global Valor_Sumado
    for i in range(1, Nivel_Maximo + 1):
        Potencia = Potencia_Base**i
        Valor = Costo_Base * Potencia
        Valor_Sumado += Valor
        print(f"Nivel {i}: {Valor:.3f}")
    print(f"Total acumulado: {Valor_Sumado:.3f}")

if __name__ == "__main__":
    pedir_valores()
    main()