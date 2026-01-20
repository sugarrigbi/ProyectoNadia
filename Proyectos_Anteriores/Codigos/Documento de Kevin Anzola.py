import sys
import math
#=========================================================
#Programa realizado por Kevin Anzola                     |
#kmanzolag@sanmateo.edu.co                               |
#+57 314 4048151                                         |
#version 4.0.2                                           |
#programa fusionado                                      |
#este programa esta protegido por derechos de autor 2025 |
#de puro desparche de mi vida                            |
#=========================================================
print("\033[35m")
print(r"""
+==========================================================+
| ____ ___ _____ _   ___     _______ _   _ ___ ____   ___  |
|| __ )_ _| ____| \ | \ \   / / ____| \ | |_ _|  _ \ / _ \ |
||  _ \| ||  _| |  \| |\ \ / /|  _| |  \| || || | | | | | ||
|| |_) | || |___| |\  | \ V / | |___| |\  || || |_| | |_| ||
||____/___|_____|_| \_|  \_/  |_____|_| \_|___|____/ \___/ |
+==========================================================+
""")
print("\033[0m")
#/////////////////////////VARIABLES////////////////////////////////
Contraseña = ""
Contraseña_Pass = ""
Contraseña_Verif = ""
Contraseña_Mod = ""
Contraseña_Correcta = False
Usuario = ""
Usuario_Pass = ""
Usuario_Verif = ""
Usuario_Mod = ""
Respuesta = 0
Caracteres = "!@#$%^&*(),.?\":{}|<>"
Respuesta_2 = 0
Numero_Piramide = 0
Seguir_Codigo_Piramide = 0
valor_1 = 0
valor_2 = 0
valor_3 = 0
Seguir_Codigo_Valores = 0
Radio_Figura = 0
Altura_Figura = 0
Base_Figura = 0
Generatriz_Figura = 0
Area_Figura = 0
Seguir_Codigo_Area_Cono = 0
Seguir_Codigo_Area_Cilindro = 0
Seguir_Codigo_Area_Romboide = 0
Seguir_Codigo_Area_Equilatero = 0
Seguir_Codigo_Area_Circulo = 0
Num_Compras = 0
Nombres = []
Precios = []
Cantidades = []
Nombre_Var = ""
Precio_Var = 0
Cantidad_Var = 0
Valor_total_Siniva = 0
Valor_total_Coniva = 0
Valor_iva = 0
Seguir_Codigo_Carrito_Compras = 0
Respuesta_3 = 0
Respuesta_Menu = 0
Respuesta_Figura = 0
#/////////////////////////FUNCION LOGIN1////////////////////////////////
def Crear_Contraseña():
    global Usuario, Contraseña
    Tiene_Mayus = False
    Tiene_Numr = False
    Tiene_Carac = False
    print("\033[45m===========================\033[0m")
    print("\033[45mCREAR USUARIO Y CONTRASEÑA:\033[0m")
    print("\033[45m===========================\033[0m")
    print("\033[34mEl usuario debe tener:")
    print("\033[36m -mínimo 5 caracteres\033[0m")
    print("\033[34mLa contraseña debe tener:")
    print("\033[36m -mínimo 8 caracteres")
    print("\033[36m -al menos un carácter en mayúscula")
    print("\033[36m -al menos un valor dígito")
    print("\033[36m -al menos un carácter especial")
    Usuario = input("\033[33mIngrese un Usuario:\033[0m ")
    while len(Usuario) < 5:
        print(
            "\033[31m==================================================\033[0m"
        )
        print(
            "\033[31mERROR: El usuario debe tener al menos 5 caracteres\033[0m"
        )
        print(
            "\033[31m==================================================\033[0m"
        )
        Usuario = input("\033[33mIngrese un usuario:\033[0m ")
    while True:
        Contraseña = input("\033[33mIngrese una contraseña:\033[0m ")
        if len(Contraseña) < 8:
            print(
                "\033[31m=====================================================\033[0m"
            )
            print(
                "\033[31mERROR: La contraseña debe tener al menos 8 caracteres\033[0m"
            )
            print(
                "\033[31m=====================================================\033[0m"
            )
            Contraseña = ""
            continue
        Tiene_Mayus = False
        for c in Contraseña:
            if c.isupper():
                Tiene_Mayus = True
                break
        if not Tiene_Mayus:
            print(
                "\033[31m=========================================================\033[0m"
            )
            print(
                "\033[31mERROR: La contraseña debe contener al menos una mayúscula\033[0m"
            )
            print(
                "\033[31m=========================================================\033[0m"
            )
            Contraseña = ""
            continue
        Tiene_Numr = False
        for c in Contraseña:
            if c.isdigit():
                Tiene_Numr = True
                break
        if not Tiene_Numr:
            print(
                "\033[31m=====================================================\033[0m"
            )
            print(
                "\033[31mERROR: La contraseña debe contener al menos un número\033[0m"
            )
            print(
                "\033[31m=====================================================\033[0m"
            )
            Contraseña = ""
            continue
        Tiene_Carac = False
        for c in Contraseña:
            if c in Caracteres:
                Tiene_Carac = True
                break
        if not Tiene_Carac:
            print(
                "\033[31m================================================================\033[0m"
            )
            print(
                "\033[31mERROR: La contraseña debe contener al menos un carácter especial\033[0m"
            )
            print(
                "\033[31m================================================================\033[0m"
            )
            Contraseña = ""
            continue
        print("\033[32m=====================================\033[0m")
        print("\033[32mEXITO: Contraseña ingresada con éxito\033[0m")
        print("\033[32m=====================================\033[0m")
        break
#/////////////////////////FUNCION LOGIN2////////////////////////////////
def Modificar_Contraseña():
    global Contraseña, Contraseña_Mod, Contraseña_Pass
    print("\033[45m=====================")
    print("\033[45mMODIFICAR CONTRASEÑA:")
    print("\033[45m=====================")
    Contraseña_Mod = input("\033[33mIngrese su contraseña actual:\033[0m ")
    if Contraseña_Mod == Contraseña:
        while True:
            print("\033[32m=====================================\033[0m")
            print("\033[32mEXITO: Contraseña ingresada con éxito\033[0m")
            print("\033[32m=====================================\033[0m")
            Contraseña_Pass = input(
                "\033[33mIngrese su nueva contraseña:\033[0m ")
            if len(Contraseña_Pass) < 8:
                print(
                    "\033[31m=====================================================\033[0m"
                )
                print(
                    "\033[31mERROR: La contraseña debe tener al menos 8 caracteres\033[0m"
                )
                print(
                    "\033[31m=====================================================\033[0m"
                )
                Contraseña_Pass = ""
                continue
            Tiene_Mayus = False
            for c in Contraseña_Pass:
                if c.isupper():
                    Tiene_Mayus = True
                    break
            if not Tiene_Mayus:
                print(
                    "\033[31m=========================================================\033[0m"
                )
                print(
                    "\033[31mERROR: La contraseña debe contener al menos una mayúscula\033[0m"
                )
                print(
                    "\033[31m=========================================================\033[0m"
                )
                Contraseña_Pass = ""
                continue
            Tiene_Numr = False
            for c in Contraseña_Pass:
                if c.isdigit():
                    Tiene_Numr = True
                    break
            if not Tiene_Numr:
                print(
                    "\033[31m=====================================================\033[0m"
                )
                print(
                    "\033[31mERROR: La contraseña debe contener al menos un número\033[0m"
                )
                print(
                    "\033[31m=====================================================\033[0m"
                )
                Contraseña_Pass = ""
                continue
            Tiene_Carac = False
            for c in Contraseña_Pass:
                if c in Caracteres:
                    Tiene_Carac = True
                    break
            if not Tiene_Carac:
                print(
                    "\033[31m================================================================\033[0m"
                )
                print(
                    "\033[31mERROR: La contraseña debe contener al menos un carácter especial\033[0m"
                )
                print(
                    "\033[31m================================================================\033[0m"
                )
                Contraseña_Pass = ""
                continue
            print("\033[32m=====================================\033[0m")
            print("\033[32mEXITO: Contraseña ingresada con éxito\033[0m")
            print("\033[32m=====================================\033[0m")
            Contraseña = Contraseña_Pass
            break
    else:
        print("\033[31m============================\033[0m")
        print("\033[31mERROR: Contraseña incorrecta\033[0m")
        print("\033[31m============================\033[0m")
#/////////////////////////FUNCION LOGIN3////////////////////////////////
def Modificar_Usuario():
    print("\033[45m==================")
    print("\033[45mMODIFICAR USUARIO:")
    print("\033[45m==================")
    global Usuario, Usuario_Mod, Usuario_Pass
    Usuario_Mod = input("\033[33mIngrese su usuario actual:\033[0m ")
    if Usuario_Mod == Usuario:
        print("\033[32m=====================================\033[0m")
        print("\033[32mEXITO: Usuario ingresado con éxito\033[0m")
        print("\033[32m=====================================\033[0m")
        Usuario_Pass = input("\033[33mIngrese su nuevo usuario:\033[0m ")
        while len(Usuario_Pass) < 5:
            print(
                "\033[31m==================================================\033[0m"
            )
            print(
                "\033[31mERROR: El usuario debe tener al menos 5 caracteres\033[0m"
            )
            print(
                "\033[31m==================================================\033[0m"
            )
            Usuario_Pass = input("\033[33mIngrese su nuevo usuario:\033[0m ")
        Usuario = Usuario_Pass
    else:
        print("\033[31m============================\033[0m")
        print("\033[31mERROR: Usuario incorrecto\033[0m")
        print("\033[31m============================\033[0m")
#/////////////////////////FUNCION LOGIN4////////////////////////////////
def Login():
    global Usuario, Contraseña, Usuario_Verif, Contraseña_Verif
    print("\033[45m====================\033[0m")
    print("\033[45mINGRESAR AL SISTEMA:\033[0m")
    print("\033[45m====================\033[0m")
    Usuario_Verif = input("\033[33mIngrese su usuario:\033[0m ")
    Contraseña_Verif = input("\033[33mIngrese su contraseña:\033[0m ")
    if Contraseña_Verif == Contraseña and Usuario_Verif == Usuario:
        print("\033[32m=======================")
        print("\033[32mEXITO: ACCESO CONCEDIDO")
        print("\033[32m=======================")
    elif Contraseña_Verif != Contraseña and Usuario_Verif == Usuario:
        print("\033[31m============================")
        print("\033[31mERROR: Contraseña incorrecta")
        print("\033[31m============================")
    elif Contraseña_Verif == Contraseña and Usuario_Verif != Usuario:
        print("\033[31m=========================")
        print("\033[31mERROR: Usuario incorrecto")
        print("\033[31m=========================")
    else:
        print("\033[31m=======================================")
        print("\033[31mERROR: Usuario y contraseña incorrectos")
        print("\033[31m=======================================")
#/////////////////////////FUNCION CERRAR////////////////////////////////
def Cerrar():
    print("\033[31m========================")
    print("\033[31mSaliendo del programa...\033[0m")
    print("\033[31m========================")
    exit()
#/////////////////////////FUNCION PIRAMIDE////////////////////////////////
def piramide():
    global Numero_Piramide, Seguir_Codigo_Piramide
    print("\033[45m=================\033[0m")
    print("\033[45mPIRAMIDE NUMERICA\033[0m")
    print("\033[45m=================\033[0m")
    print("\033[34mHola Usuario, Bienvenido a la piramide numerica\033[0m")
    print("\033[36mEste codigo creara una piramide con el numero de pisos que indique\033[0m")
    while True:
        try:
            Numero_Piramide = int(
                input("\033[33mIngrese un número entero: \033[0m"))
        except ValueError:
            print("\033[31m===============================\033[0m")
            print("\033[31mERROR: Ingrese un número válido\033[0m")
            print("\033[31m===============================\033[0m")
            continue
        for i in range(1, Numero_Piramide + 1):
            for j in range(1, i + 1):
                print("\033[35m", j, end=" ")
            print()
        for i in range(Numero_Piramide - 1, 0, -1):
            for j in range(1, i + 1):
                print("\033[35m", j, end=" ")
            print()
        print("\033[34mOPCIONES:")
        print("\033[36m1.) Volver a ejecutar el codigo")
        print("\033[36m2.) Salir del codigo")
        print("\033[36m3.) Volver al menu principal")
        print("\033[36m4.) Cerrar el programa")
        Seguir_Codigo_Piramide = input("\033[33melija una opcion: \033[0m")
        if Seguir_Codigo_Piramide == "1":
            print("\033[34m====================\033[0m")
            print("\033[34mReiniciando piramide\033[0m")
            print("\033[34m====================\033[0m")
            continue
        elif Seguir_Codigo_Piramide == "2":
            Cerrar()
        elif Seguir_Codigo_Piramide == "3":
            print("\033[34m===========================\033[0m")
            print("\033[34mVolviendo al menu principal\033[0m")
            print("\033[34m===========================\033[0m")
            break
        elif Seguir_Codigo_Piramide == "4":
            Cerrar()
        else:
            print("\033[31m===============================\033[0m")
            print("\033[31mERROR: Ingrese un número válido\033[0m")
            print("\033[31m===============================\033[0m")


#/////////////////////////FUNCION VALORES////////////////////////////////
def valores():
    global valor_1, valor_2, valor_3, Seguir_Codigo_Valores
    print("\033[45m========================\033[0m")
    print("\033[45mIDENTIFICADOR DE VALORES\033[0m")
    print("\033[45m========================\033[0m")
    print(
        "\033[34mHola Usuario, Bienvenido al identificador de numeros\033[0m")
    while True:
        try:
            valor_1 = float(input("\033[33mDigite el primer valor: \033[0m"))
            valor_2 = float(input("\033[33mDigite el segundo valor: \033[0m"))
            valor_3 = float(input("\033[33mDigite el tercero valor: \033[0m"))
        except ValueError:
            print("\033[31m========================\033[0m")
            print("\033[31mERROR: Ingrese un numero\033[0m")
            print("\033[31m========================\033[0m")
            Cerrar()

        if valor_1 < valor_2 and valor_1 < valor_3:
            print("\033[34mEl valor mas bajo es: \033[0m", valor_1)
        elif valor_2 < valor_1 and valor_2 < valor_3:
            print("\033[34mEl valor mas bajo es: \033[0m", valor_2)
        elif valor_3 < valor_1 and valor_3 < valor_2:
            print("\033[34mEl valor mas bajo es: \033[0m", valor_3)

        if valor_1 < valor_2 < valor_3:
            print("\033[34mEl valor del medio es: \033[0m", valor_2)
        elif valor_1 < valor_3 < valor_2:
            print("\033[34mEl valor del medio es: \033[0m", valor_3)
        elif valor_2 < valor_1 < valor_3:
            print("\033[34mEl valor del medio es: \033[0m", valor_1)
        elif valor_2 > valor_3 > valor_1:
            print("\033[34mEl valor del medio es: \033[0m", valor_3)
        elif valor_3 < valor_1 < valor_2:
            print("\033[34mEl valor del medio es: \033[0m", valor_1)
        elif valor_3 < valor_2 < valor_1:
            print("\033[34mEl valor del medio es: \033[0m", valor_2)

        if valor_1 > valor_2 and valor_1 > valor_3:
            print("\033[34mEl valor mas alto es: \033[0m", valor_1)
        elif valor_2 > valor_1 and valor_2 > valor_3:
            print("\033[34mEl valor mas alto es: \033[0m", valor_2)
        elif valor_3 > valor_1 and valor_3 > valor_2:
            print("\033[34mEl valor mas alto es: \033[0m", valor_3)

        if valor_1 == valor_2 == valor_3:
            print("\033[34mLos valores son iguales\033[0m")
        elif valor_1 == valor_2 < valor_3:
            print(
                "\033[34mvalor 1 y valor 2 son los valores mas bajos e iguales y equivalen a: \033[0m",
                valor_1)
        elif valor_1 == valor_3 < valor_2:
            print(
                "\033[34mvalor 1 y valor 3 son los valores mas bajos e iguales y equivalen a: \033[0m",
                valor_1)
        elif valor_2 == valor_3 < valor_1:
            print(
                "\033[34mvalor 2 y valor 3 son los valores mas bajos e iguales y equivalen a: \033[0m",
                valor_2)
        elif valor_1 == valor_2 > valor_3:
            print(
                "\033[34mvalor 1 y valor 2 son los valores mas altos e iguales y equivalen a: \033[0m",
                valor_2)
        elif valor_1 == valor_3 > valor_2:
            print(
                "\033[34mvalor 1 y valor 3 son los valores mas altos e iguales y equivalen a: \033[0m",
                valor_3)
        elif valor_2 == valor_3 > valor_1:
            print(
                "\033[34mvalor 2 y valor 3 son los valores mas altos e iguales y equivalen a: \033[0m",
                valor_3)
        print("\033[34mOPCIONES:\033[0m")
        print("\033[36m1.) Volver a ejecutar el codigo\033[0m")
        print("\033[36m2.) Salir del codigo\033[0m")
        print("\033[36m3.) Volver al menu principal\033[0m")
        print("\033[36m4.) Cerrar el programa")
        Seguir_Codigo_Valores = input("\033[33melija una opcion: \033[0m")
        if Seguir_Codigo_Valores == "1":
            print("\033[34m===================\033[0m")
            print("\033[34mReiniciando Valores\033[0m")
            print("\033[34m===================\033[0m")
            continue
        elif Seguir_Codigo_Valores == "2":
            Cerrar()
        elif Seguir_Codigo_Valores == "3":
            print("\033[34m===========================\033[0m")
            print("\033[34mVolviendo al menu principal\033[0m")
            print("\033[34m===========================\033[0m")
            break
        elif Seguir_Codigo_Valores == "4":
            Cerrar()
        else:
            print("\033[31m===============================\033[0m")
            print("\033[31mERROR: Ingrese un número válido\033[0m")
            print("\033[31m===============================\033[0m")


#/////////////////////////FUNCION AREA_CONO////////////////////////////////
def Area_Cono():
    global Radio_Figura, Altura_Figura, Generatriz_Figura, Area_Figura, Seguir_Codigo_Area_Cono
    print("\033[45m==========\033[0m")
    print("\033[45mAREA CONO:\033[0m")
    print("\033[45m==========\033[0m")
    while True:
        try:
            Radio_Figura = float(
                input("\033[33mIngrese el radio del cono(unidades):\033[0m "))
        except ValueError:
            print("\033[31m===============================\033[0m")
            print("\033[31mERROR: Ingrese un número válido\033[0m")
            print("\033[31m===============================\033[0m")
            continue
        try:
            Altura_Figura = float(
                input("\033[33mIngrese la altura del cono(unidades):\033[0m "))
        except ValueError:
            print("\033[31m===============================\033[0m")
            print("\033[31mERROR: Ingrese un número válido\033[0m")
            print("\033[31m===============================\033[0m")
            continue
        Generatriz_Figura = math.sqrt(Radio_Figura**2 + Altura_Figura**2)
        Area_Figura = math.pi * Radio_Figura * (Radio_Figura +
                                                Generatriz_Figura)
        print(
            "\033[36mLa formula para hallar el área de un cono es \033[31mA = πr(r+g)\033[0m"
        )
        print("\033[34mEl área total del cono es:\033[33m",
              round(Area_Figura, 2), "unidades²\n")
        print("\033[34mOPCIONES:\033[0m")
        print("\033[36m1.) Volver a ejecutar el codigo\033[0m")
        print("\033[36m2.) Salir del codigo\033[0m")
        print("\033[36m3.) Volver al menu principal\033[0m")
        print("\033[36m4.) Cerrar el programa")
        Radio_Figura = 0
        Altura_Figura = 0
        Generatriz_Figura = 0
        Area_Figura = 0
        Seguir_Codigo_Area_Cono = input("\033[33melija una opcion:\033[0m ")
        if Seguir_Codigo_Area_Cono == "1":
            print("\033[34m=======================\033[0m")
            print("\033[34mReiniciando Calculadora\033[0m")
            print("\033[34m=======================\033[0m")
            continue
        elif Seguir_Codigo_Area_Cono == "2":
            Cerrar()
        elif Seguir_Codigo_Area_Cono == "3":
            print("\033[34m===========================\033[0m")
            print("\033[34mVolviendo al menu principal\033[0m")
            print("\033[34m===========================\033[0m")
            break
        elif Seguir_Codigo_Area_Cono == "4":
            Cerrar()
        else:
            print("\033[31m===============================\033[0m")
            print("\033[31mERROR: Ingrese un número válido\033[0m")
            print("\033[31m===============================\033[0m")


#/////////////////////////FUNCION AREA_CILINDRO////////////////////////////////
def Area_Cilindro():
    global Radio_Figura, Altura_Figura, Area_Figura, Seguir_Codigo_Area_Cilindro
    print("\033[45m==============\033[0m")
    print("\033[45mAREA CILINDRO:\033[0m")
    print("\033[45m==============\033[0m")
    while True:
        try:
            Radio_Figura = float(
                input(
                    "\033[33mIngrese el radio del cilindro(unidades):\033[0m ")
            )
        except ValueError:
            print("\033[31m===============================\033[0m")
            print("\033[31mERROR: Ingrese un número válido\033[0m")
            print("\033[31m===============================\033[0m")
            continue
        try:
            Altura_Figura = float(
                input(
                    "\033[33mIngrese la altura del cilindro(unidades):\033[0m "
                ))
        except ValueError:
            print("\033[31m===============================\033[0m")
            print("\033[31mERROR: Ingrese un número válido\033[0m")
            print("\033[31m===============================\033[0m")
            continue
        Area_Figura = 2 * math.pi * Radio_Figura * (Radio_Figura +
                                                    Altura_Figura)
        print(
            "\033[36mLa formula para hallar el área de un cilindro es \033[31mA = 2πr(r+h)\033[0m"
        )
        print("\033[34mEl área total del cilindro es:\033[33m",
              round(Area_Figura, 2), "unidades²\n")
        print("\033[34mOPCIONES:\033[0m")
        print("\033[36m1.) Volver a ejecutar el codigo\033[0m")
        print("\033[36m2.) Salir del codigo\033[0m")
        print("\033[36m3.) Volver al menu principal\033[0m")
        print("\033[36m4.) Cerrar el programa")
        Radio_Figura = 0
        Altura_Figura = 0
        Area_Figura = 0
        Seguir_Codigo_Area_Cilindro = input(
            "\033[33melija una opcion:\033[0m ")
        if Seguir_Codigo_Area_Cilindro == "1":
            print("\033[34m=======================\033[0m")
            print("\033[34mReiniciando Calculadora\033[0m")
            print("\033[34m=======================\033[0m")
            continue
        elif Seguir_Codigo_Area_Cilindro == "2":
            Cerrar()
        elif Seguir_Codigo_Area_Cilindro == "3":
            print("\033[34m===========================\033[0m")
            print("\033[34mVolviendo al menu principal\033[0m")
            print("\033[34m===========================\033[0m")
            break
        elif Seguir_Codigo_Area_Cilindro == "4":
            Cerrar()
        else:
            print("\033[31m===============================\033[0m")
            print("\033[31mERROR: Ingrese un número válido\033[0m")
            print("\033[31m===============================\033[0m")


#/////////////////////////FUNCION AREA_ROMBOIDE////////////////////////////////
def Area_Romboide():
    global Base_Figura, Altura_Figura, Area_Figura, Seguir_Codigo_Area_Romboide
    print("\033[45m==============\033[0m")
    print("\033[45mAREA ROMBOIDE:\033[0m")
    print("\033[45m==============\033[0m")
    while True:
        try:
            Base_Figura = float(
                input(
                    "\033[33mIngrese la base del romboide(unidades):\033[0m "))
        except ValueError:
            print("\033[31m===============================\033[0m")
            print("\033[31mERROR: Ingrese un número válido\033[0m")
            print("\033[31m===============================\033[0m")
            continue
        try:
            Altura_Figura = float(
                input(
                    "\033[33mIngrese la altura del romboide(unidades):\033[0m "
                ))
        except ValueError:
            print("\033[31m===============================\033[0m")
            print("\033[31mERROR: Ingrese un número válido\033[0m")
            print("\033[31m===============================\033[0m")
            continue
        Area_Figura = Base_Figura * Altura_Figura
        print(
            "\033[36mLa formula para hallar el área de un romboide es \033[31mA = b⋅h\033[0m"
        )
        print("\033[34mEl área total del romboide es:\033[33m",
              round(Area_Figura, 2), "unidades²\n")
        print("\033[34mOPCIONES:\033[0m")
        print("\033[36m1.) Volver a ejecutar el codigo\033[0m")
        print("\033[36m2.) Salir del codigo\033[0m")
        print("\033[36m3.) Volver al menu principal\033[0m")
        print("\033[36m4.) Cerrar el programa")
        Base_Figura = 0
        Altura_Figura = 0
        Area_Figura = 0
        Seguir_Codigo_Area_Romboide = input(
            "\033[33melija una opcion:\033[0m ")
        if Seguir_Codigo_Area_Romboide == "1":
            print("\033[34m=======================\033[0m")
            print("\033[34mReiniciando Calculadora\033[0m")
            print("\033[34m=======================\033[0m")
            continue
        elif Seguir_Codigo_Area_Romboide == "2":
            Cerrar()
        elif Seguir_Codigo_Area_Romboide == "3":
            print("\033[34m===========================\033[0m")
            print("\033[34mVolviendo al menu principal\033[0m")
            print("\033[34m===========================\033[0m")
            break
        elif Seguir_Codigo_Area_Romboide == "4":
            Cerrar()
        else:
            print("\033[31m===============================\033[0m")
            print("\033[31mERROR: Ingrese un número válido\033[0m")
            print("\033[31m===============================\033[0m")


#/////////////////////////FUNCION AREA_EQUILATERO////////////////////////////////
def Area_Equilatero():
    global Base_Figura, Altura_Figura, Area_Figura, Seguir_Codigo_Area_Equilatero
    print("\033[45m================\033[0m")
    print("\033[45mAREA EQUILATERO:\033[0m")
    print("\033[45m================\033[0m")
    while True:
        try:
            Base_Figura = float(
                input(
                    "\033[33mIngrese la base del triángulo equilátero(unidades):\033[0m "
                ))
        except ValueError:
            print("\033[31m===============================\033[0m")
            print("\033[31mERROR: Ingrese un número válido\033[0m")
            print("\033[31m===============================\033[0m")
            continue
        try:
            Altura_Figura = float(
                input(
                    "\033[33mIngrese la altura del triángulo equilátero(unidades):\033[0m "
                ))
        except ValueError:
            print("\033[31m===============================\033[0m")
            print("\033[31mERROR: Ingrese un número válido\033[0m")
            print("\033[31m===============================\033[0m")
            continue
        Area_Figura = (Base_Figura * Altura_Figura) / 2
        print(
            "\033[36mLa formula para hallar el área de un triángulo equilátero es \033[31mA = b⋅h/2\033[0m"
        )
        print("\033[34mEl área total del triángulo equilátero es:\033[33m",
              round(Area_Figura, 2), "unidades²\n")
        print("\033[34mOPCIONES:\033[0m")
        print("\033[36m1.) Volver a ejecutar el codigo\033[0m")
        print("\033[36m2.) Salir del codigo\033[0m")
        print("\033[36m3.) Volver al menu principal\033[0m")
        print("\033[36m4.) Cerrar el programa")
        Base_Figura = 0
        Altura_Figura = 0
        Area_Figura = 0
        Seguir_Codigo_Area_Equilatero = input(
            "\033[33melija una opcion:\033[0m ")
        if Seguir_Codigo_Area_Equilatero == "1":
            print("\033[34m=======================\033[0m")
            print("\033[34mReiniciando Calculadora\033[0m")
            print("\033[34m=======================\033[0m")
            continue
        elif Seguir_Codigo_Area_Equilatero == "2":
            Cerrar()
        elif Seguir_Codigo_Area_Equilatero == "3":
            print("\033[34m===========================\033[0m")
            print("\033[34mVolviendo al menu principal\033[0m")
            print("\033[34m===========================\033[0m")
            break
        elif Seguir_Codigo_Area_Equilatero == "4":
            Cerrar()
        else:
            print("\033[31m===============================\033[0m")
            print("\033[31mERROR: Ingrese un número válido\033[0m")
            print("\033[31m===============================\033[0m")


#/////////////////////////FUNCION AREA_CIRCULO////////////////////////////////
def Area_Circulo():
    global Radio_Figura, Area_Figura, Seguir_Codigo_Area_Circulo
    print("\033[45m=============\033[0m")
    print("\033[45mAREA CIRCULO:\033[0m")
    print("\033[45m=============\033[0m")
    while True:
        try:
            Radio_Figura = float(
                input(
                    "\033[33mIngrese el radio del circulo(unidades):\033[0m "))
        except ValueError:
            print("\033[31m===============================\033[0m")
            print("\033[31mERROR: Ingrese un número válido\033[0m")
            print("\033[31m===============================\033[0m")
            continue
        Area_Figura = math.pi * Radio_Figura**2
        print(
            "\033[36mLa formula para hallar el área de un circulo es \033[31mA = π⋅r²\033[0m"
        )
        print("\033[34mEl área total del circulo es:\033[33m",
              round(Area_Figura, 2), "unidades²\n")
        print("\033[34mOPCIONES:\033[0m")
        print("\033[36m1.) Volver a ejecutar el codigo\033[0m")
        print("\033[36m2.) Salir del codigo\033[0m")
        print("\033[36m3.) Volver al menu principal\033[0m")
        print("\033[36m4.) Cerrar el programa")
        Radio_Figura = 0
        Area_Figura = 0
        Seguir_Codigo_Area_Circulo = input("\033[33melija una opcion:\033[0m ")
        if Seguir_Codigo_Area_Circulo == "1":
            print("\033[34m=======================\033[0m")
            print("\033[34mReiniciando Calculadora\033[0m")
            print("\033[34m=======================\033[0m")
            continue
        elif Seguir_Codigo_Area_Circulo == "2":
            Cerrar()
        elif Seguir_Codigo_Area_Circulo == "3":
            print("\033[34m===========================\033[0m")
            print("\033[34mVolviendo al menu principal\033[0m")
            print("\033[34m===========================\033[0m")
            break
        elif Seguir_Codigo_Area_Circulo == "4":
            Cerrar()
        else:
            print("\033[31m===============================\033[0m")
            print("\033[31mERROR: Ingrese un número válido\033[0m")
            print("\033[31m===============================\033[0m")


#/////////////////////////FUNCION CARRITO_COMPRAS////////////////////////////////
def Carrito_Compras():
    global Num_Compras, Nombres, Precios, Cantidades, Nombre_Var, Precio_Var, Cantidad_Var, Valor_total_Siniva, Valor_total_Coniva, Valor_iva, Seguir_Codigo_Carrito_Compras, Respuesta_3
    print("\033[45m==================\033[0m")
    print("\033[45mCARRITO DE COMPRAS\033[0m")
    print("\033[45m==================\033[0m")
    while True:
      print("\033[34melije una opcion:\033[0m")
      print("\033[36m1.) Comprar\033[0m")
      print("\033[36m2.) lista de compras\033[0m")
      print("\033[36m3.) Total de productos(Sin iva)\033[0m")
      print("\033[36m4.) Total de productos(con iva)\033[0m")
      print("\033[36m5.) Valor del Iva\033[0m")
      print("\033[36m6.) Volver al menu principal\033[0m")
      print("\033[36m7.) Cerrar el programa")
      try:
        Respuesta_3 = int(input("\033[32mIngrese una opción:\033[0m "))
      except ValueError:
        print("\033[31mError: Ingrese un número válido.\033[0m")
        continue
      if Respuesta_3 == 1:
        print("\033[45m================\033[0m")
        print("\033[45mComprar objetos:\033[0m")
        print("\033[45m================\033[0m")
        print("\033[34mHola Usuario, Bienvenido al apartado de compras\033[0m")
        while True:
          try:
            Num_Compras = int(input("\033[33mIngrese el número de objetos que desea comprar:\033[0m "))
            break
          except ValueError:
              print("\033[31m===============================\033[0m")
              print("\033[31mERROR: Ingrese un número válido\033[0m")
              print("\033[31m===============================\033[0m")
        print("\033[34mhas elejido", Num_Compras, "objetos\033[0m ")
        for i in range(Num_Compras):
          while True:
            try:
              Nombre_Var = input("\033[33mIngrese el nombre del objeto:\033[0m ").strip()
              if Nombre_Var:
                break
              else:
                print("\033[31m====================================\033[0m")
                print("\033[31mERROR: No puede dejar el campo vacio\033[0m")
                print("\033[31m====================================\033[0m")
            except ValueError:
              print("\033[31m===============================\033[0m")
              print("\033[31mERROR: Ingrese un número válido\033[0m")
              print("\033[31m===============================\033[0m")
              Nombre_Var = ""
          while True:
            try:
              Precio_Var = float(input("\033[33mIngrese el precio del objeto:\033[0m "))
              break
            except ValueError:
              print("\033[31m===============================\033[0m")
              print("\033[31mERROR: Ingrese un número válido\033[0m")
              print("\033[31m===============================\033[0m")
              Precio_Var = 0
          while True:
            try:
              Cantidad_Var = int(input("\033[36mIngrese la cantidad de objetos:\033[0m "))
              break
            except ValueError:
              print("\033[31m===============================\033[0m")
              print("\033[31mERROR: Ingrese un número válido\033[0m")
              print("\033[31m===============================\033[0m")
              Cantidad_Var = 0
          print("\033[34m==================\033[0m ")
          print("\033[36mEl Producto es :\033[0m ")
          print("\033[37m", Nombre_Var, "\033[0m")
          print("\033[37m", Precio_Var, "\033[0m")
          print("\033[37m", Cantidad_Var, "\033[0m")
          print("\033[34m==================\033[0m ")
          Nombres.append(Nombre_Var)
          Precios.append(Precio_Var)
          Cantidades.append(Cantidad_Var)
        print("\033[32m====================\033[0m ")
        print("\033[32mGracias por comprar!\033[0m")
        print("\033[32m====================\033[0m ")    
        Valor_total_Siniva = 0
        Valor_total_Coniva = 0
        Valor_iva = 0

        for i in range(Num_Compras):
            Valor_total_Siniva = Valor_total_Siniva + (Precios[i] * Cantidades[i])
        for i in range(Num_Compras):
            Valor_total_Coniva = Valor_total_Siniva + (Valor_total_Siniva * 0.19)
        for i in range(Num_Compras):
            Valor_iva = Valor_total_Siniva * 0.19
            
      elif Respuesta_3 == 2:
        print("\033[34mLos productos que ha comprado son:\033[0m")
        for i in range(Num_Compras):
          print("\033[34m==================\033[0m ")
          print("\033[33mProducto numero", i+1)
          print("\033[37m", Nombres[i], "\033[0m")
          print("\033[37m", Precios[i], "\033[0m")
          print("\033[37m", Cantidades[i], "\033[0m")
          print("\033[34m==================\033[0m ")
      elif Respuesta_3 == 3:
        print("\033[34mEl total de productos sin iva es:\033[0m",round(Valor_total_Siniva, 5))
      elif Respuesta_3 == 4:
        print("\033[34mEl total de productos con iva es:\033[0m",round(Valor_total_Coniva, 5))
      elif Respuesta_3 == 5:
        print("\033[34mEl total del iva es:\033[0m", round(Valor_iva, 5))
      elif Respuesta_3 == 6:
          print("\033[34m===========================\033[0m")
          print("\033[34mVolviendo al menu principal\033[0m")
          print("\033[34m===========================\033[0m")
          break
      elif Respuesta_3 == 7:
        Cerrar()
      else:
        print("\033[31m===============================\033[0m")
        print("\033[31mERROR: Ingrese un número válido\033[0m")
        print("\033[31m===============================\033[0m")
#/////////////////////////FUNCION MENU1////////////////////////////////
def Menu_Formas():
    global Respuesta_Figura
    while True:
        print("\033[45m======================\033[0m")
        print("\033[45mCALCULADORA GEOMETRICA\033[0m")
        print("\033[45m======================\033[0m")
        print("\n\033[34mElije una opcion: \033[0m")
        print("\033[36m1.) Calcular area de un cono\033[0m")
        print("\033[36m2.) Calcular area de un cilindro\033[0m")
        print("\033[36m3.) Calcular area de un romboide\033[0m")
        print("\033[36m4.) Calcular area de un triangulo equilatero\033[0m")
        print("\033[36m5.) Calcular area de un circulo\033[0m")
        print("\033[36m6.) Volver al menu principal\033[0m")
        print("\033[36m7.) Cerrar el programa")
        try:
            Respuesta_Figura = int(input("\033[33mIngrese una opción:\033[0m "))
        except ValueError:
            print("\033[31m===============================\033[0m")
            print("\033[31mERROR: Ingrese un número válido\033[0m")
            print("\033[31m===============================\033[0m")
            continue
        match Respuesta_Figura:
            case 1:
                Area_Cono()
            case 2:
                Area_Cilindro()
            case 3:
                Area_Romboide()
            case 4:
                Area_Equilatero()
            case 5:
                Area_Circulo()
            case 6:
                print("\033[34m===========================\033[0m")
                print("\033[34mVolviendo al menu principal\033[0m")
                print("\033[34m===========================\033[0m")
                break
            case 7:
                Cerrar()
            case _:
                print("\033[31m===============================\033[0m")
                print("\033[31mERROR: Ingrese un número válido\033[0m")
                print("\033[31m===============================\033[0m")
#/////////////////////////FUNCION MENU1////////////////////////////////
def Menu_Funciones():
    global Respuesta_Menu
    while True:
        print("\033[45m==============\033[0m")
        print("\033[45mMENU FUNCIONES\033[0m")
        print("\033[45m==============\033[0m")
        print("\n\033[34mElije una opcion: \033[0m")
        print("\033[36m1.) Crear piramide\033[0m")
        print("\033[36m2.) Comprar valores\033[0m")
        print("\033[36m3.) Calcular areas\033[0m")
        print("\033[36m4.) Carrito de compras\033[0m")
        print("\033[36m5.) Volver al menu anterior\033[0m")
        print("\033[36m6.) Cerrar el programa")
        try:
            Respuesta_Menu = int(input("\033[33mIngrese una opción:\033[0m "))
        except ValueError:
            print("\033[31m===============================\033[0m")
            print("\033[31mERROR: Ingrese un número válido\033[0m")
            print("\033[31m===============================\033[0m")
            continue
        match Respuesta_Menu:
            case 1:
                piramide()
            case 2:
                valores()
            case 3:
                Menu_Formas()
            case 4:
                Carrito_Compras()
            case 5:
                print("\033[34m===========================\033[0m")
                print("\033[34mVolviendo al menu principal\033[0m")
                print("\033[34m===========================\033[0m")
                break
            case 6:
                Cerrar()
            case _:
                print("\033[31m===============================\033[0m")
                print("\033[31mERROR: Ingrese un número válido\033[0m")
                print("\033[31m===============================\033[0m")
#**********************************************INICIO CODIGO**********************************************
print("\033[45m=====================================\033[0m")
print("\033[45mAPLICACION FUSIONADA POR KEVIN ANZOLA\033[0m")
print("\033[45m=====================================\033[0m")
print("\033[34mHola Usuario, Porfavor ingrese antes de continuar\033[0m")
while True:
    print("\n\033[34mElije una opcion: \033[0m")
    print("\033[36m1.) Crear usuario y contraseña\033[0m")
    print("\033[36m2.) Modificar contraseña\033[0m")
    print("\033[36m3.) Modificar usuario\033[0m")
    print("\033[36m4.) Ingresar al sistema\033[0m")
    print("\033[36m5.) Salir\033[0m")
    try:
        Respuesta = int(input("\033[33mIngrese una opción:\033[0m "))
    except ValueError:
        print("\033[31m===============================\033[0m")
        print("\033[31mERROR: Ingrese un número válido\033[0m")
        print("\033[31m===============================\033[0m")
        continue
    match Respuesta:
        case 1:
            Crear_Contraseña()
        case 2:
            Modificar_Contraseña()
        case 3:
            Modificar_Usuario()
        case 4:
            Login()
            Menu_Funciones()
        case 5:
            Cerrar()
        case 6:
            Carrito_Compras()
        case _:
            print("\033[31m===============================\033[0m")
            print("\033[31mERROR: Ingrese un número válido\033[0m")
            print("\033[31m===============================\033[0m")