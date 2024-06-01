import math;

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

def raiz_cuadrada(n):
  error=1e-5
  if n < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")

    # Aproximación inicial
    a = n
    b = 1

    # Mejorar la aproximación
    while abs(resta(a, b)) > error:  # Usando abs(a - b) para calcular la diferencia
        a = division(suma(a, b), 2)  # Promedio de a y b, a = (a + b) / 2
        b = division(n, a)  # Nuevo valor de b, b = n / a

  return a

def exponencial(a):
  return 0

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

  def test_raiz_cuadrada(self):
    self.assertAlmostEqual(raiz_cuadrada(4), 2, places=3)
    self.assertAlmostEqual(raiz_cuadrada(9), 3, places=3)
    self.assertAlmostEqual(raiz_cuadrada(2), 1.414213562373095, places=3)
    with self.assertRaises(ValueError):
        raiz_cuadrada(-1)

  def test_exponencial(self):
    self.assertAlmostEqual(exponencial(0), 1, places=3)
    self.assertAlmostEqual(exponencial(1), math.e, places=3)
    self.assertAlmostEqual(exponencial(-1), 1 / math.e, places=3)
    self.assertAlmostEqual(exponencial(2), math.e**2, places=3)

if __name__ == '__main__':
    unittest.main()
