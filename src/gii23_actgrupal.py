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

def raiz_cuadrada(n, error=1e-5):
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


def exponencial(x, error=1e-5):
  term = 1.0  # Primer término de la serie de Taylor
  sum = 1.0   # La suma comienza con el primer término
  n = 1       # Contador para el factorial en el denominador

  while abs(term) > error:
    term = multiplicacion(term, division(x, n))
    sum = suma(sum, term)
    n = n + 1

  return sum
