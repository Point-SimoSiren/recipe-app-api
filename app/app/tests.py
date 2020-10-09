from django.test import TestCase
import unittest

from app.calc import add

class CalcTests(TestCase):
    """Test that values are added together"""
    def test_add_pos_numbers(self):
        self.assertEqual(add(3, 8), 11)
    
    def test_add_neg_numbers(self):
        self.assertEqual(add(-3, -8), -11)

    def test_add_both_numbers(self):
        self.assertEqual(add(-10, 11), 1)

    def testCustomAssert1(self):
        self.assertEqual(add('tuomas', '12'), 'tuomas12')

    """Testin pitää epäonnistua"""
    @unittest.expectedFailure
    def testCustomAssert2(self):
        self.assertEqual(add('tuomas', 12), 'tuomas12')