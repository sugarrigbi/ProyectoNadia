#===========================
#Programa realizado por kevin anzola
#kmanzolag@sanmateo.edu.co
#+57 3144048151
#programa que recoge datos los almacena y los da en pantalla
#este programa esta protegido por derechos de autor 2025
#===========================
#VARIABLES
Pri_nom,Seg_nom,Pri_Ape,Seg_Ape,Pais,Ciudad = "","","","","",""
Edad = 0
#INICIO DEL PROGRAMA
print ("Este Programa  permite capturar los datos personales y mostrar en pantalla")
#RECOLECCION DE DATOS
Pri_nom = input("Ingrese su primer nombre:\n")
Sec_nom = input("Ingrese su segundo nombre:\n")
Pri_Ape = input("Ingrese su primer apellido:\n")
Sec_Ape = input("Ingrese su segundo apellido:\n")
Pais = input("Ingrese su pais:\n")
Ciudad = input("Ingrese su ciudad:\n")
Edad = int(input("Ingrese su edad:\n"))
#ESCRIBIR DATOS EN PANTALLA
print ("Su nombre completo es:" + Pri_nom + " " + Sec_nom + " " + Pri_Ape + " " + Sec_Ape)
print ("su Edad es:" + str(Edad))
print ("Usted es de:" + Pais + " " + Ciudad)
print ("este programa fue diseñado por kevin anzola y esta sujeto a derechos de autor 2025")