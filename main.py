# -*- coding: utf-8 -*-
from __future__ import division
from decimal import Decimal

import argparse
from operator import sub, add, mul
import math
import unittest
import argparse

def doIt(operator, *args):
	result = 0
	if (len(args) == 2):
		first_arg = Decimal(args[0])
		second_arg = Decimal(args[1])
		# first_arg = args[0]
		# second_arg = args[1]
		# args[1] = Decimal(args[1])
		if (operator == '+'):
			result = first_arg + second_arg 
		elif (operator == '-'):
			result = sub(first_arg, second_arg)
		elif (operator == '*'):
			result = mul(first_arg, second_arg)
		elif (operator == '/'):
			result = first_arg / second_arg
		else:
			raise TypeError("Данный калькулятор не поддерживает операцию: " + operator)
			return 0; 
		result = Decimal(result)	
	elif(len(args) == 1):
		if (operator == 'sin'):
			result = math.sin(args[0])
		else:
			raise TypeError("Данный калькулятор не поддерживает операцию: " + operator)
			return 0; 
	else:
		raise TypeError("Введенно некорректное количество аргументов")
	return result       

def main():
	parser = argparse.ArgumentParser(description='Формат ввода "<оператор>" <argument> [argument+]')	
	parser.add_argument('operator')
	parser.add_argument('arguments', type=str, nargs='+')

	args = parser.parse_args()

	try:
		print doIt(args.operator, *args.arguments)
	except Exception as e:
		print "Ошибка: " + e.message

	if __name__ == "__main__":
		main()