#=========================================================
#Programa realizado por Kevin Anzola                     |
#kmanzolag@sanmateo.edu.co                               |
#+57 314 4048151                                         |
#version 1.0                                             |
#programa que da el area de varias figuras               |
#este programa esta protegido por derechos de autor 2025 |
#=========================================================
CARACTERES = "!@#$%^&*(),.?\":{}|<>"
CONTRASEÑA = ""
Contraseña_Verif = ""
Respuesta = 0
Tiene_Digitos = False
Tiene_Mayus = False
Tiene_Numr = False
Tiene_Carac = False

print("\033[35m")
print(r"""
.------------------------------------------------------------.
|   ____                 __          _  __          _        |
|  / ___| __ _ _ __ ____/_/  _ __   | |/ /_____   _(_)_ __   |
| | |  _ / _` | '__|_  / _ \| '_ \  | ' // _ \ \ / / | '_ \  |
| | |_| | (_| | |   / / (_) | | | | | . \  __/\ V /| | | | | |
|  \____|\__,_|_|  /___\___/|_| |_| |_|\_\___| \_/ |_|_| |_| |
'------------------------------------------------------------'
""")
print("\033[0m")

print("\033[44m=====\033[0m")
print("\033[44mLOGIN\033[0m")
print("\033[44m=====\033[0m")
print("\033[32mHola Usuario, Bienvenido al Login\033[0m")

while True:
    print ("\033[35melije una opcion:\n\033[33m1.) Crear Contraseña\n2.) Ingresar\n3.) Salir\033[0m")
    try:
        Respuesta = int(input("\033[32mIngrese una opción:\033[0m "))
    except ValueError:
        print("\033[31mError: Ingrese un número válido.\033[0m")
        continue

    if Respuesta == 1:
        print("\033[45m=================\033[0m")
        print("\033[45mCrear Contraseña:\033[0m")
        print("\033[45m=================\033[0m")
        print("\033[34mLa contraseña debe tener:")
        print("\033[36m-debe contener mínimo 8 caracteres")
        print("\033[36m-debe tener al menos un caracter en mayúscula")
        print("\033[36m-debe tener al menos un valor dígito")
        print("\033[36m-debe tener al menos un caracter especial")
        CONTRASEÑA = input("\033[32mIngrese una Contraseña:\033[0m ")
#VERIFICAR DIGITO
        if len(CONTRASEÑA) > 8:
            Tiene_Digitos = True
        else:
            print("\033[31mError: No tiene 8 Caracteres, Intente de nuevo")
#VERIFICAR MAYUS
        for c in CONTRASEÑA:
            if c.isupper():
                Tiene_Mayus = True
        if Tiene_Mayus:
            Tiene_Mayus = True
        else:
            print("\033[31mError: No tiene Mayus, Intente de nuevo")
#VERIFICAR DIGITO
        for c in CONTRASEÑA:
            if c.isdigit():
                Tiene_Numr = True
        if Tiene_Numr:
            Tiene_Numr = True
        else:
            print("\033[31mError: No tiene Numero, Intente de nuevo")
#VERIFICAR NUMR
        for c in CONTRASEÑA:
            if c in CARACTERES:
                Tiene_Carac = True
        if Tiene_Carac:
            print("\033[33mExito: Contraseña ingresada con exito")
        else:
            print("\033[31mError: No tiene Caracter Especial, Intente de nuevo")
#VERIFICAR CONTRASEÑA
    elif Respuesta == 2:
        Contraseña_Verif = input("\033[32mIngrese su contraseña:\033[0m ")
        if Contraseña_Verif == CONTRASEÑA:
            print("\033[32mExito: Contraseña Correcta")
            print("\033[36m==========")
            print("\033[36mBIENVENIDO")
            print("\033[36m==========")
            break
        else:
            print("\033[31mError: Contraseña Incorrecta")
            print("\033[31m============")
            print("\033[31mNO PERMITIDO")
            print("\033[31m============")
#OTRAS RESPUESTAS
    elif Respuesta == 3:
        print("\033[31mSaliendo del programa...\033[0m")
        break
    else:
        print("\033[31mError: Ingrese un número válido.\033[0m")   