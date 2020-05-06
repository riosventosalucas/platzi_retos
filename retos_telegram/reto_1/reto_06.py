# -*- coding: utf-8 -*-
#!/usr/bin/env python

import random
import time

# Reto:
"""
Reto #6 “Resta de pizzas”
Instrucciones: llegaste a una fiesta con X cantidad de rebanadas de pizza (indicadas por el usuario), 
después de un rato se consumió Y cantidad de rebanadas y quedan Z. Fácil ¿cierto?
El reto está en que expreses lo que sucede es una forma comprensible para cualquier persona, 
imprescindible pensar en tus usuarios 😉
"""

#Aclaracion:
"""
Por motivos practicos he decidido utilizar un numero aleatorio entre el numero ingresado y 1
"""


def main():
	portions_of_pizza = int(raw_input("Ingrese la cantidad de rebanadas de pizza: "))
	
	if portions_of_pizza < 1:
		print("Se acabaron las rebanadas :'(")
	else:
		total = portions_of_pizza
		while portions_of_pizza is not 0:
			time.sleep(5)
			random_number_of_discount = random.randint(1, portions_of_pizza)

			portions_of_pizza = portions_of_pizza - random_number_of_discount

			print("Ya comieron {} rebanadas de pizza.".format(random_number_of_discount))
			if portions_of_pizza == 0:
				print("Ya no quedan rebanadas de pizza :(")
				break
			else:
				print("Quedan {} de {} rebanadas de pizza, apresurate!!!".format(portions_of_pizza, total))




if __name__ == '__main__':
	main()