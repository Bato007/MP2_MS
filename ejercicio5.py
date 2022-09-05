import numpy as np

def integral(x):
  numerator = ((-1 * np.exp((-2)*((1/x)-1))) + (np.exp((-1) * ((1/x)-1))))
  denominator = x**2
  return numerator/denominator

def calculate(n):
  x = np.random.uniform(-5, 5, n)
  y = np.random.uniform(0, 1, n)
  hits = sum(y <= integral(x))
  mascara= y <= integral(x)
  return (10) * (hits) / float(n), x, y, mascara

resultado_100 = calculate(100)
resultado_10000 = calculate(10000)
resultado_100000 = calculate(100000)
print('RESULTADO 100: ', resultado_100[0])
print('RESULTADO 10000: ', resultado_10000[0])
print('RESULTADO 100000: ', resultado_100000[0])
