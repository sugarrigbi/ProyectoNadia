Algoritmo sin_titulo
	Definir Cifra1 , Cifra2 , resultado Como real
	Definir eleccion Como Caracter
	escribir "Que tipo de operacion desea hacer?"
	escribir "+ para suma, - para resta, * para multiplicacion, / para divicion"
	leer eleccion
	Escribir "Escriba primer numero"
	leer Cifra1
	Escribir "Escriba segundo numero"
	leer Cifra2
	Segun eleccion hacer
		"+" : resultado = Cifra1 + Cifra2
			Escribir "el resultado es " resultado
		"-" : resultado = Cifra1 - Cifra2
			Escribir "el resultado es " resultado
		"*" : resultado = Cifra1 * Cifra2
			Escribir "el resultado es " resultado
		"/" : resultado = Cifra1 / Cifra2
			Escribir "el resultado es " resultado
	FinSegun
FinAlgoritmo
