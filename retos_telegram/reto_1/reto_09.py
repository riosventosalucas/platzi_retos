# -*- coding: utf-8 -*-
#!/usr/bin/env python

# Reto:
"""
Reto #9 “Calculando días”
Instrucciones: escribe un programa al que le indiques una cantidad de días y como resultado deberá mostrar cuantas horas, 
minutos y segundos hay en dicha cantidad de días.
"""


def main():
	days     = int(raw_input("Ingrese la cantidad de dias: "))
	hours    = days    * 24
	minutes  = hours   * 60
	secconds = minutes * 60

	print("Hay {} horas, {} minutos y {} segundos en {} dias.".format(hours, minutes, secconds, days))

if __name__ == '__main__':
	main()