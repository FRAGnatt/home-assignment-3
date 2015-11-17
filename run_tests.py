# -*- coding: utf-8 -*-

import unittest
import sys

from tests.test_calculator import EvaluateTestCase, OperatorsTestCase

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(EvaluateTestCase),
        unittest.makeSuite(OperatorsTestCase)
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
