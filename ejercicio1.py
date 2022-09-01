from random import random
import matplotlib.pyplot as plt

class Point(object):
  def __init__(self, x: float, y: float) -> None:
    self.x = x
    self.y = y

  def __str__(self) -> str:
    return '({0}, {1})'.format(self.x, self.y)

# Creando las funciones
def f1(p: Point) -> Point:
  return Point(p.x/2, p.y/2)

def f2(p: Point) -> Point:
  return Point((p.x + 1)/2, p.y/2)

def f3(p: Point) -> Point:
  return Point(((2 * p.x) + 1)/4, (p.y + 1)/2)

# Initial values
iterations = 100000
point = Point(0.5, 0.5)
x = []
y = []

pf1 = 1/3
pf2 = 1/3

for i in range(iterations):
  rvalue = random()
  x.append(point.x)
  y.append(point.y)

  if (rvalue < pf1):
    rfun = f1
  elif (pf1 <= rvalue and rvalue < (pf2 + pf1)):
    rfun = f2
  else:
    rfun = f3

  point = rfun(point)

plt.scatter(x, y, color='black', marker='*')
plt.show()
