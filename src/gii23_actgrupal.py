def suma(a, b):
  return a + b

def resta(a, b):
  return a - b

def multiplicacion(a, b):
  return a * b

def division(a, b):
  if b == 0:
    raise ValueError("Error: No se puede dividir por cero")
  return a / b


# Pruebas unitarias
import unittest

class TestCalculadora(unittest.TestCase):

  def test_suma(self):
    self.assertAlmostEqual(suma(2, 1), 3, places=3)
    self.assertAlmostEqual(suma(-1, 1), 0, places=3)
    self.assertAlmostEqual(suma(-2, -1), -3, places=3)

  def test_resta(self):
    self.assertAlmostEqual(resta(2, 1), 1, places=3)
    self.assertAlmostEqual(resta(-1, -1), 0, places=3)
    self.assertAlmostEqual(resta(-1, 1), -2, places=3)

  def test_multiplicacion(self):
    self.assertAlmostEqual(multiplicacion(2, 3), 6, places=3)
    self.assertAlmostEqual(multiplicacion(-1, 1), -1, places=3)
    self.assertAlmostEqual(multiplicacion(-1, -1), 1, places=3)

  def test_division(self):
    self.assertAlmostEqual(division(3, 2), 1.5 , places=3)
    self.assertAlmostEqual(division(-6, 2), -3, places=3)
    self.assertAlmostEqual(division(-7, -3), 2.333333333333333, places=3)

if __name__ == '__main__':
    unittest.main()
