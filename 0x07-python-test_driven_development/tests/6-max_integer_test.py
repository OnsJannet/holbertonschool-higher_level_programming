#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

  def test_max_ints(self):
      self.assertEqual(max_integer([1, 2, 3, 4]), 4)

  def test_uniq(self):
      self.assertAlmostEqual(max_integer([4]), 4)

  def test_floats(self):
      self.assertEqual(max_integer([4, 4.4, 4.8]), 4.8)

  def test_float_neg(self):
      self.assertAlmostEqual(max_integer([-1.5, -2.5, -3.5, -4.5]), -1.5)

  def test_string(self):
      self.assertAlmostEqual(max_integer("Camila"), "m")

  def test_atuples(self):
      self.assertEqual(max_integer((1, 13, 14, 3)), 14)

  def test_large_intbeg(self):
      self.assertEqual(max_integer([999999999999999, 1]), 999999999999999)

  def test_empty(self):
      self.assertAlmostEqual(max_integer([]), None)

  def test_max_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

  def test_max_True(self):
        with self.assertRaises(TypeError):
            max_integer(True)
  
  def test_emptylist(self):
      self.assertEqual(max_integer([]), None)

  if __name__ == '__main__':
    unittest.main()
