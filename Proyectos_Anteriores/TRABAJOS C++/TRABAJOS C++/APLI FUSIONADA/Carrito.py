#=========================================================
#Programa realizado por Kevin Anzola                     |
#kmanzolag@sanmateo.edu.co                               |
#+57 314 4048151                                         |
#version 1.0                                             |
#programa que da el area de varias figuras               |
#este programa esta protegido por derechos de autor 2025 |
#=========================================================
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

print("\033[44m==================\033[0m")
print("\033[44mCARRITO DE COMPRAS\033[0m")
print("\033[44m==================\033[0m")
print("\033[32mHola Usuario, Bienvenido al Carrito de compras\033[0m")

while True:
  print(
      "\033[35melije una opcion:\n\033[33m1.) Comprar\n2.) lista de compras\n3.) Total de productos(Sin iva)\n4.) Total de productos(con iva)\n5.) Iva\n6.) Salir\033[0m"
  )
  try:
    Respuesta = int(input("\033[32mIngrese una opción:\033[0m "))
  except ValueError:
    print("\033[31mError: Ingrese un número válido.\033[0m")
    continue

  if Respuesta == 1:
    print("\033[45m========\033[0m")
    print("\033[45mComprar:\033[0m")
    print("\033[45m========\033[0m")
    print("\033[32mHola Usuario, Bienvenido al apartado de compras\033[0m")
    while True:
      try:
        Num_Compras = int(
            input(
                "\033[33mIngrese el número de objetos que desea comprar:\033[0m "
            ))
        break
      except ValueError:
        print("\033[31mError: Ingrese un número válido.\033[0m")

    print("\033[33mhas elejido", Num_Compras, "objetos\033[0m ")

    for i in range(Num_Compras):
      while True:
        try:
          Nombre_Var = input("\033[34mIngrese el nombre del objeto:\033[0m ").strip()
          if Nombre_Var:
            break
          else: print("\033[31mError: No puede dejar el campo vacio.\033[0m")
        except ValueError:
          print("\033[31mError: Ingrese un número válido.\033[0m")
          Nombre_Var = ""
      while True:
        try:
          Precio_Var = float(input("\033[35mIngrese el precio del objeto:\033[0m "))
          break
        except ValueError:
          print("\033[31mError: Ingrese un número válido.\033[0m")
          Precio_Var = 0
      while True:
        try:
          Cantidad_Var = int(
              input("\033[36mIngrese la cantidad de objetos:\033[0m "))
          break
        except ValueError:
          print("\033[31mError: Ingrese un número válido.\033[0m")
          Cantidad_Var = 0
      print("\033[36m----------------\033[0m ")
      print("\033[36mEl Producto es :\033[0m ")
      print(Nombre_Var)
      print(Precio_Var)
      print(Cantidad_Var)
      print("\033[36m----------------\033[0m ")
      Nombres.append(Nombre_Var)
      Precios.append(Precio_Var)
      Cantidades.append(Cantidad_Var)
    print("\033[36m--------------------\033[0m ")
    print("\033[36mGracias por comprar!")
    print("\033[36m--------------------\033[0m ")    
    Valor_total_Siniva = 0
    Valor_total_Coniva = 0
    Valor_iva = 0

    for i in range(Num_Compras):
        Valor_total_Siniva = Valor_total_Siniva + (Precios[i] * Cantidades[i])
    for i in range(Num_Compras):
        Valor_total_Coniva = Valor_total_Siniva + (Valor_total_Siniva * 0.19)
    for i in range(Num_Compras):
        Valor_iva = Valor_total_Siniva * 0.19

  elif Respuesta == 2:
    print("\033[32mLos productos que ha comprado son:\033[0m")
    for i in range(Num_Compras):
      print("\033[36m_________\033[0m ")
      print("\033[33mProducto numero", i+1)
      print(Nombres[i])
      print(Precios[i])
      print(Cantidades[i])
      print("\033[36m_________\033[0m ")

  elif Respuesta == 3:
    print("\033[35mEl total de productos sin iva es:\033[0m",round(Valor_total_Siniva, 5))

  elif Respuesta == 4:
    print("\033[35mEl total de productos con iva es:\033[0m",round(Valor_total_Coniva, 5))

  elif Respuesta == 5:
    print("\033[35mEl total del iva es:\033[0m", round(Valor_iva, 5))

  elif Respuesta == 6:
    print("\033[31mSaliendo del programa...\033[0m")
    break

  else:
    print("\033[31mError: Ingrese un número válido.\033[0m")