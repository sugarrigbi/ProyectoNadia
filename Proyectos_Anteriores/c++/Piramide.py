#=========================================================
#Programa realizado por Kevin Anzola                     |
#kmanzolag@sanmateo.edu.co                               |
#+57 314 4048151                                         |
#version 1.0                                             |
#programa que da el area de varias figuras               |
#este programa esta protegido por derechos de autor 2025 |
#=========================================================
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

print("\033[44m=================\033[0m")
print("\033[44mPIRAMIDE NUMERICA\033[0m")
print("\033[44m=================\033[0m")
print("\033[32mHola Usuario, Bienvenido a la piramide numerica\033[0m")

Numero = 0
while True:

  Numero = int(input("\033[33mIngrese un número entero: \033[0m"))

  for i in range(1, Numero + 1):
    for j in range(1, i + 1):
      print(j, end=" ")
    print()

  for i in range(Numero - 1, 0, -1):
    for j in range(1, i + 1):
      print(j, end=" ")
    print()
