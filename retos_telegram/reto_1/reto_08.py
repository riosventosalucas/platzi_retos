# -*- coding: utf-8 -*-
#!/usr/bin/env python

# Reto:
"""
Reto #8 “Divide la cuenta”
Instrucciones: vas con tus amigos a tu restaurante favorito y acuerdan dividir la cuenta. 
Para facilitar las cosa pedirás al usuario que indique el total a pagar, entre cuantas personas se dvidirá la cuenta, 
porcentaje de propina a incluir, un porcentaje de impuestos, 
total a pagar incluyendo propina más impuestos y el total a pagar por cada persona.
"""


def main():
	total_to_paid     = float(raw_input("Ingrese el total a pagar y presione ENTER: "))
	number_of_friends = float(raw_input("Ingrese el total de personas que deben pagar y presione ENTER: "))
	tip_percentage    = int(raw_input("Ingrese el porcentaje de propina que desean dar y presione ENTER: "))
	tax               = int(raw_input("Ingrese el porcentaje de impuesto y presione ENTER: "))

	total_with_tax         = (total_to_paid + (total_to_paid * tax) / 100)
	total_to_paid_with_tip = (total_with_tax + ((total_with_tax * tip_percentage) / 100)) 
	total                  = total_to_paid_with_tip / number_of_friends

	print("El total a pagar por persona es de : {:.2f}".format(total))
	

if __name__ == '__main__':
	main()