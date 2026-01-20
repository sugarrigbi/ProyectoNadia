#=========================================================
#Programa realizado por Kevin Anzola                     |
#kmanzolag@sanmateo.edu.co                               |
#+57 314 4048151                                         |
#version 1.0                                             |
#programa que organiza numeros                           |
#este programa esta protegido por derechos de autor 2025 |
#=========================================================
import sys

valor1 = 0
valor2 = 0
valor3 = 0
try:
  valor1 = int(input("Digite el primer valor: "))
  valor2 = int(input("Digite el segundo valor: "))
  valor3 = int(input("Digite el tercero valor: "))
except ValueError:
  print("El valor ingresado no es un número entero")
  sys.exit()
/*
if valor1 > valor2 and valor1 > valor3:
  print("El valor mayor es: ", valor1)
elif valor2 > valor1 and valor2 > valor3:
  print("El valor mayor es: ", valor2)
elif valor3 > valor1 and valor3 > valor2:
  print("El valor mayor es: ", valor3)

if valor1 < valor2 and valor1 < valor3:
  print("El valor menor es: ", valor1)
elif valor2 < valor1 and valor2 < valor3:
  print("El valor menor es: ", valor2)
elif valor3 < valor1 and valor3 < valor2:
  print("El valor menor es: ", valor3)

if valor1 < valor2 < valor3:
  print("El valor mediano es: ", valor2)
elif valor1 < valor3 < valor2:
  print("El valor mediano es: ", valor3)
elif valor2 < valor1 < valor3:
  print("El valor mediano es: ", valor1)
elif valor2 > valor3 > valor1:
  print("El valor mediano es: ", valor3)
elif valor3 < valor1 < valor2:
  print("El valor mediano es: ", valor1)
elif valor3 < valor2 < valor1:
  print("El valor mediano es: ", valor2)

if valor1 == valor2 == valor3:
  print("Los valores son iguales")
elif valor1 == valor2 < valor3:
  print("valor1 y valor2 son menores e iguales y el valor menor es: ", valor1)
elif valor1 == valor3 < valor2:
  print("valor1 y valor3 son menores e iguales y el valor menor es: ", valor1)
elif valor2 == valor3 < valor1:
  print("valor2 y valor3 son menores e iguales y el valor menor es: ", valor2)
elif valor1 == valor2 > valor3:
  print("valor1 y valor2 son mayores e iguales y el valor mayor es: ", valor2)
elif valor1 == valor3 > valor2:
  print("valor1 y valor3 son mayores e iguales y el valor mayor es: ", valor3)
elif valor2 == valor3 > valor1:
  print("valor2 y valor3 son mayores e iguales y el valor mayor es: ", valor3)
