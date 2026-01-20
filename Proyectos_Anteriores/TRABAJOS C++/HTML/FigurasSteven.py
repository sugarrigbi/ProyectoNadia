#=========================================================
#Programa realizado por Steven Mora                      |
#smorag@sanmateo.edu.co                                  |
#+57 302 8293988                                         |
#version 1.0                                             |
#programa que da el Area de varias figuras               |
#este programa esta protegido por derechos de autor 2025 |
#=========================================================
#LIBRERIAS
import math
#VARIABLES
Eleccion = 0
Radio_Figura = 0
Altura_Figura = 0
Base_Figura = 0
Generatiz_Figura = 0
Area_figura = 0
Diametro_Figura = 0
#INICIO MENU
#inicio
print("\033[46m//////////\033[0m")
print("\033[46mGEOMETRIA+\033[0m")
print("\033[46m//////////\033[0m")
print("\033[32mEste programa te permite calcular áreas de diferentes figuras\033[0m")
#OPCIONES DEL MENU
#pedir opcion y error
while True:
    print ("\033[36melije una opcion:\n\033[34m1.) Cono\n2.) Cilindro\n3.) Romboide\n4.) Triangulo Equilatero\033[0m")
    try:
        Eleccion = int(input("\033[32mIngrese una opción:\033[0m "))
    except ValueError:
        print("\033[32mIngrese un numero valido\033[0m")
        continue
#Area_figura DEL CONO
    if Eleccion == 1:
        print("\033[47m=====\033[0m")
        print("\033[47mCONO:\033[0m")
        print("\033[47m=====\033[0m")
#pedir numero1 y error
        try:
            Radio_Figura = float(input("\033[32mIngrese el Radio_Figura del cono(unidades):\033[0m "))
        except ValueError:
            print("\033[32mIngrese un numero valido\033[0m")
            continue
#pedir numero2 y error
        try:
            Altura_Figura = float(input("\033[32mIngrese la Altura_Figura del cono(unidades):\033[0m "))
        except ValueError:
            print("\033[32mIngrese un numero valido\033[0m")
            continue
#hacer los calculos matematicos y dar resultados
        Generatiz_Figura = math.sqrt(Radio_Figura**2 + Altura_Figura**2)
        Area_figura = math.pi * Radio_Figura * (Radio_Figura + Generatiz_Figura)
        print("\033[34mse usa la formula para un cono es \033[32mA = πr(r+g)\033[0m")
        print("\033[32mEl Resultado del cono es:\033[34m", Area_figura, "unidades²")
#preguntar si seguir el codigo o no al usuario y error
        while True:
            REPETIR = input("\033[47mQuieres volver al menu principal?(s/n)\033[0m ")
            if REPETIR in ["s", "n"]:
                break
            else:
                print("\033[32mError: Ingrese 's' o 'n'.\033[0m")
        if REPETIR == "n":
            print("\033[32mCerrando programa\033[0m")
            break
#Area_figura DEL CILINDRO  
    elif Eleccion == 2:
        print("\033[47m=========\033[0m")
        print("\033[47mCILINDRO:\033[0m")
        print("\033[47m=========\033[0m")
#pedir numero1 y error
        try:
            Radio_Figura = float(input("\033[32mIngrese el Radio_Figura del cilindro(unidades):\033[0m "))
        except ValueError:
            print("\033[32mIngrese un numero valido\033[0m")
            continue
#pedir numero2 y error
        try:    
            Altura_Figura = float(input("\033[32mIngrese la Altura_Figura del cilindro(unidades):\033[0m "))
        except ValueError:
            print("\033[32mIngrese un numero valido\033[0m")
            continue        
#hacer los calculos matematicos y dar resultados
        Area_figura = 2 * math.pi * Radio_Figura * (Radio_Figura + Altura_Figura)
        print("\033[34mse usa la formula para un cilindro es \033[32mA = 2πr(r+h)\033[0m")
        print("\033[32mEl Resultado del cilindro es:\033[34m", Area_figura, "unidades²")
#preguntar si seguir el codigo o no al usuario y error
        while True:
            REPETIR = input("\033[47mQuieres volver al menu principal?(s/n)\033[0m ")
            if REPETIR in ["s", "n"]:
                break
            else:
                print("\033[32mError: Ingrese 's' o 'n'.\033[0m")
        if REPETIR == "n":
            print("\033[32mCerrando programa\033[0m")
            break
#Area_figura DEL ROMBOIDE
    elif Eleccion == 3:
        print("\033[47m=========\033[0m")
        print("\033[47mROMBOIDE:\033[0m")
        print("\033[47m=========\033[0m")
#pedir numero1 y error
        try:
            Base_Figura = float(input("\033[32mIngrese la Base_Figura del romboide(unidades):\033[0m "))
        except ValueError:
            print("\033[32mIngrese un numero valido\033[0m")
            continue
#pedir numero2 y error
        try:       
            Altura_Figura = float(input("\033[32mIngrese la Altura_Figura del romboide(unidades):\033[0m "))
        except ValueError:
            print("\033[32mIngrese un numero valido\033[0m")
            continue        
#hacer los calculos matematicos y dar resultados
        Area_figura = Base_Figura * Altura_Figura
        print("\033[34mse usa la formula para un romboide es \033[32mA = b⋅h\033[0m")
        print("\033[32mEl Resultado del romboide es:\033[34m", Area_figura, "unidades²")
#preguntar si seguir el codigo o no al usuario y error
        while True:
            REPETIR = input("\033[47mQuieres volver al menu principal?(s/n)\033[0m ")
            if REPETIR in ["s", "n"]:
                break
            else:
                print("\033[32mError: Ingrese 's' o 'n'.\033[0m")
        if REPETIR == "n":
            print("\033[32mCerrando programa\033[0m")
            break
#Area_figura DEL TRIANGULO EQUILATERO
    elif Eleccion == 4:
        print("\033[47m======\033[0m")
        print("\033[47mTRIANGULO EQUILATERO:\033[0m")
        print("\033[47m======\033[0m")
#pedir numero1 y error
        try:        
            Base_Figura = float(input("\033[32mIngrese la Base_Figura del triángulo equilátero(unidades):\033[0m "))
        except ValueError:
            print("\033[32mIngrese un numero valido\033[0m")
            continue
#pedir numero2 y error
        try:      
            Altura_Figura = float(input("\033[32mIngrese la Altura_Figura del triángulo equilátero(unidades):\033[0m "))
        except ValueError:
            print("\033[32mIngrese un numero valido\033[0m")
            continue        
#hacer los calculos matematicos y dar resultados
        Area_figura = (Base_Figura * Altura_Figura) / 2
        print("\033[34mse usa la formula para un triángulo equilátero es \033[32mA = b⋅h/2\033[0m")
        print("\033[32mEl Resultado del cilindro es:\033[34m", Area_figura, "unidades²")
#preguntar si seguir el codigo o no al usuario y error
        while True:
            REPETIR = input("\033[47mQuieres volver al menu principal?(s/n)\033[0m ")
            if REPETIR in ["s", "n"]:
                break
            else:
                print("\033[32mError: Ingrese 's' o 'n'.\033[0m")
        if REPETIR == "n":
            print("\033[32mCerrando programa\033[0m")
            break
#Area_figura DEL CIRCULO
    elif Eleccion == 5:
        print("\033[47m=======\033[0m")
        print("\033[47mCIRCULO:\033[0m")
        print("\033[47m=======\033[0m")
#pedir numero1 y error
        try:        
            Radio_Figura = float(input("\033[32mIngrese el Radio_Figura del circulo(unidades):\033[0m "))
        except ValueError:
            print("\033[32mIngrese un numero valido\033[0m")
            continue
#hacer los calculos matematicos y dar resultados
        Diametro_Figura = 2 * Radio_Figura
        Area_figura = math.pi * Radio_Figura ** 2
        print("\033[34mse usa la formula para un circulo es \033[32mA = π⋅r²\033[0m")
        print("\033[32mEl Resultado del circulo es:\033[34m", Area_figura, "unidades²")
#preguntar si seguir el codigo o no al usuario y error
        while True:
            REPETIR = input("\033[47mQuieres volver al menu principal?(s/n)\033[0m ")
            if REPETIR in ["s", "n"]:
                break
            else:
                print("\033[32mError: Ingrese 's' o 'n'.\033[0m")
        if REPETIR == "n":
            print("\033[32mCerrando programa\033[0m")
            break
#CERRAR CODIGO
    else:
        print("\033[32mCerrando programa\033[0m")
        break