#=========================================================
#Programa realizado por Urrego Nadia                     |
#ndurregov@sanmateo.edu.co                               |
#+57 312 5261601                                         |
#version 1.0                                             |
#programa que da el Area                                 |
#este programa esta protegido por derechos de autor 2025 |
#=========================================================
#LIBRERIAS
import math
#VARIABLES
opc = 0
rad = 0
alt = 0
bas = 0
gen = 0
area = 0
dia = 0
#INICIO MENU
#inicio
print("\033[49m----------\033[0m")
print("\033[49mCalculadora+\033[0m")
print("\033[49m----------\033[0m")
print("\033[38mEste programa te permite calcular el area de las figuras\033[0m")
#OPCIONES DEL MENU
#pedir opcion y error
while True:
    print ("\033[31melije una opcion:\n\033[34m1.) Cono\n2.) Cilindro\n3.) Romboide\n4.) Triangulo Equilatero\033[0m")
    try:
        opc = int(input("\033[38mIngrese una opción:\033[0m "))
    except ValueError:
        print("\033[38mIngrese un numero valido\033[0m")
        continue
#area DEL CONO
    if opc == 1:
        print("\033[49m=====\033[0m")
        print("\033[49mCONO:\033[0m")
        print("\033[49m=====\033[0m")
#pedir numero1 y error
        try:
            rad = float(input("\033[38mIngrese el rad del cono(unidades):\033[0m "))
        except ValueError:
            print("\033[38mIngrese un numero valido\033[0m")
            continue
#pedir numero2 y error
        try:
            alt = float(input("\033[38mIngrese la alt del cono(unidades):\033[0m "))
        except ValueError:
            print("\033[38mIngrese un numero valido\033[0m")
            continue
#hacer los calculos matematicos y dar resultados
        gen = math.sqrt(rad**2 + alt**2)
        area = math.pi * rad * (rad + gen)
        print("\033[34mse usa la formula para un cono es \033[38mA = πr(r+g)\033[0m")
        print("\033[38mEl Resultado del cono es:\033[34m", area, "unidades²")
#preguntar si seguir el codigo o no al usuario y error
        while True:
            REPETIR = input("\033[49mQuieres volver al menu principal?(s/n)\033[0m ")
            if REPETIR in ["s", "n"]:
                break
            else:
                print("\033[38mError: Ingrese 's' o 'n'.\033[0m")
        if REPETIR == "n":
            print("\033[38mCerrando programa\033[0m")
            break
#area DEL CILINDRO  
    elif opc == 2:
        print("\033[49m=========\033[0m")
        print("\033[49mCILINDRO:\033[0m")
        print("\033[49m=========\033[0m")
#pedir numero1 y error
        try:
            rad = float(input("\033[38mIngrese el rad del cilindro(unidades):\033[0m "))
        except ValueError:
            print("\033[38mIngrese un numero valido\033[0m")
            continue
#pedir numero2 y error
        try:    
            alt = float(input("\033[38mIngrese la alt del cilindro(unidades):\033[0m "))
        except ValueError:
            print("\033[38mIngrese un numero valido\033[0m")
            continue        
#hacer los calculos matematicos y dar resultados
        area = 2 * math.pi * rad * (rad + alt)
        print("\033[34mse usa la formula para un cilindro es \033[38mA = 2πr(r+h)\033[0m")
        print("\033[38mEl Resultado del cilindro es:\033[34m", area, "unidades²")
#preguntar si seguir el codigo o no al usuario y error
        while True:
            REPETIR = input("\033[49mQuieres volver al menu principal?(s/n)\033[0m ")
            if REPETIR in ["s", "n"]:
                break
            else:
                print("\033[38mError: Ingrese 's' o 'n'.\033[0m")
        if REPETIR == "n":
            print("\033[38mCerrando programa\033[0m")
            break
#area DEL ROMBOIDE
    elif opc == 3:
        print("\033[49m=========\033[0m")
        print("\033[49mROMBOIDE:\033[0m")
        print("\033[49m=========\033[0m")
#pedir numero1 y error
        try:
            bas = float(input("\033[38mIngrese la bas del romboide(unidades):\033[0m "))
        except ValueError:
            print("\033[38mIngrese un numero valido\033[0m")
            continue
#pedir numero2 y error
        try:       
            alt = float(input("\033[38mIngrese la alt del romboide(unidades):\033[0m "))
        except ValueError:
            print("\033[38mIngrese un numero valido\033[0m")
            continue        
#hacer los calculos matematicos y dar resultados
        area = bas * alt
        print("\033[34mse usa la formula para un romboide es \033[38mA = b⋅h\033[0m")
        print("\033[38mEl Resultado del romboide es:\033[34m", area, "unidades²")
#preguntar si seguir el codigo o no al usuario y error
        while True:
            REPETIR = input("\033[49mQuieres volver al menu principal?(s/n)\033[0m ")
            if REPETIR in ["s", "n"]:
                break
            else:
                print("\033[38mError: Ingrese 's' o 'n'.\033[0m")
        if REPETIR == "n":
            print("\033[38mCerrando programa\033[0m")
            break
#area DEL TRIANGULO EQUILATERO
    elif opc == 4:
        print("\033[49m======\033[0m")
        print("\033[49mTRIANGULO EQUILATERO:\033[0m")
        print("\033[49m======\033[0m")
#pedir numero1 y error
        try:        
            bas = float(input("\033[38mIngrese la bas del triángulo equilátero(unidades):\033[0m "))
        except ValueError:
            print("\033[38mIngrese un numero valido\033[0m")
            continue
#pedir numero2 y error
        try:      
            alt = float(input("\033[38mIngrese la alt del triángulo equilátero(unidades):\033[0m "))
        except ValueError:
            print("\033[38mIngrese un numero valido\033[0m")
            continue        
#hacer los calculos matematicos y dar resultados
        area = (bas * alt) / 2
        print("\033[34mse usa la formula para un triángulo equilátero es \033[38mA = b⋅h/2\033[0m")
        print("\033[38mEl Resultado del cilindro es:\033[34m", area, "unidades²")
#preguntar si seguir el codigo o no al usuario y error
        while True:
            REPETIR = input("\033[49mQuieres volver al menu principal?(s/n)\033[0m ")
            if REPETIR in ["s", "n"]:
                break
            else:
                print("\033[38mError: Ingrese 's' o 'n'.\033[0m")
        if REPETIR == "n":
            print("\033[38mCerrando programa\033[0m")
            break
#area DEL CIRCULO
    elif opc == 5:
        print("\033[49m=======\033[0m")
        print("\033[49mCIRCULO:\033[0m")
        print("\033[49m=======\033[0m")
#pedir numero1 y error
        try:        
            rad = float(input("\033[38mIngrese el rad del circulo(unidades):\033[0m "))
        except ValueError:
            print("\033[38mIngrese un numero valido\033[0m")
            continue
#hacer los calculos matematicos y dar resultados
        dia = 2 * rad
        area = math.pi * rad ** 2
        print("\033[34mse usa la formula para un circulo es \033[38mA = π⋅r²\033[0m")
        print("\033[38mEl Resultado del circulo es:\033[34m", area, "unidades²")
#preguntar si seguir el codigo o no al usuario y error
        while True:
            REPETIR = input("\033[49mQuieres volver al menu principal?(s/n)\033[0m ")
            if REPETIR in ["s", "n"]:
                break
            else:
                print("\033[38mError: Ingrese 's' o 'n'.\033[0m")
        if REPETIR == "n":
            print("\033[38mCerrando programa\033[0m")
            break
#CERRAR CODIGO
    else:
        print("\033[38mCerrando programa\033[0m")
        break