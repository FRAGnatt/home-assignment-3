# -*- coding: utf-8 -*-
from __future__ import division
from decimal import Decimal
import sys
sys.path.append('../')

from main import doIt
from operator import add, sub, mul
from math import sin
import unittest

class EvaluateTestCase(unittest.TestCase):
	def test_not_supported_method(self):
		with self.assertRaises(TypeError):
			doIt("not_supported", 1, 2)

	def test_supported_method(self):		
		self.assertEqual(doIt("+", 9, 22), 31)

class OperatorsTestCase(unittest.TestCase):

	def test_add(self):
		self.assertEqual(doIt('+' , 6, 8), 14)
	def test_addString(self):
		self.assertEqual(doIt('+' , '6', '8'), 14)

	def test_sub(self):
		self.assertEqual(doIt('-', 2, 3.5), -1.5)

	def test_subString(self):
		self.assertEqual(doIt('-', '2', '3.5'), -1.5)
	
	def test_sub2(self):
		self.assertEqual(doIt('-', 10, 2), 8)

	def test_mul(self):
		self.assertEqual(doIt('*', 2, 3.5), 2 * 3.5)

	def test_mulString(self):
		self.assertEqual(doIt('*', '2', '3.5'), 2 * 3.5)

	def test_div(self):
		self.assertEqual(doIt('/', 10, 5), 2)

	def test_div2(self):
		self.assertEqual(doIt('/', 5, 2), 2.5)

	def test_sin(self):
		self.assertEqual(doIt('sin', 2), sin(2))

	def test_invalid_count_args(self):
		with self.assertRaises(TypeError):
			doIt('sin', 1, 2)

	def test_div_null(self):
		with self.assertRaises(ZeroDivisionError):
			doIt('/', 2, 0)
	def test_sum_float(self):
		self.assertEqual(doIt('+', '0.1', '0.2'), Decimal('0.3'))
