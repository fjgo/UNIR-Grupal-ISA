#!/usr/bin/env python3
import unittest
import math
from gii23_actgrupal import suma, resta, multiplicacion, division, raiz_cuadrada,exponencial

# Pruebas unitarias
class TestCalculadora(unittest.TestCase):
  precision = 3
  error = 10**-precision # Utilizamos el inverso de la precisión para calcular el error admisible en los cálculos

  def test_suma(self):
    self.assertAlmostEqual(suma(1, 2), 3, places=self.precision)
    self.assertAlmostEqual(suma(-1, 1), 0, places=self.precision)
    self.assertAlmostEqual(suma(-1, -1), -2, places=self.precision)

  def test_resta(self):
    self.assertAlmostEqual(resta(10, 5), 5, places=self.precision)
    self.assertAlmostEqual(resta(-1, 1), -2, places=self.precision)
    self.assertAlmostEqual(resta(-1, -1), 0, places=self.precision)

  def test_multiplicacion(self):
    self.assertAlmostEqual(multiplicacion(2, 3), 6, places=self.precision)
    self.assertAlmostEqual(multiplicacion(-1, 1), -1, places=self.precision)
    self.assertAlmostEqual(multiplicacion(-1, -1), 1, places=self.precision)

  def test_division(self):
    self.assertAlmostEqual(division(10, 2), 5, places=self.precision)
    self.assertAlmostEqual(division(-6, 2), -3, places=self.precision)
    self.assertAlmostEqual(division(-6, -2), 3, places=self.precision)
    self.assertAlmostEqual(division(-7, -3), 2.333333333333333, places=self.precision)
    with self.assertRaises(ValueError):
      division(10, 0)

  def test_raiz_cuadrada(self):
    self.assertAlmostEqual(raiz_cuadrada(4, self.error), 2, places=self.precision)
    self.assertAlmostEqual(raiz_cuadrada(9,  self.error), 3, places=self.precision)
    self.assertAlmostEqual(raiz_cuadrada(2,  self.error), 1.414213562373095, places=self.precision)
    with self.assertRaises(ValueError):
      raiz_cuadrada(-1)

  def test_exponencial(self):
    self.assertAlmostEqual(exponencial(0, self.error), 1, places=self.precision)
    self.assertAlmostEqual(exponencial(1, self.error), math.e, places=self.precision)
    self.assertAlmostEqual(exponencial(-1, self.error), 1 / math.e, places=self.precision)
    self.assertAlmostEqual(exponencial(2, self.error), math.e**2, places=self.precision)

if __name__ == '__main__':
  unittest.main()
