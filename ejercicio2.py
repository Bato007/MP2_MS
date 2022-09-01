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
  return Point(
    p.x*0.85 + p.y*0.04 + 0.0,
    p.x*-0.04 + p.y*0.85 + 1.6
  )

def f2(p: Point) -> Point:
  return Point(
    p.x*-0.15 + p.y*0.28 + 0.0,
    p.x*0.26 + p.y*0.24 + 0.44
  )

def f3(p: Point) -> Point:
  return Point(
    p.x*0.2 + p.y*-0.26 + 0.0,
    p.x*0.23 + p.y*0.22 + 1.6
  )

def f4(p: Point) -> Point:
  return Point(
    0.0,
    p.y*0.16
  )

# Inicializando las variables
F = [
  f1, f2, f3, f4,
]

P = [
  0.85, 0.07, 0.07, 0.01
]

n = 100000
point = Point(0.5, 0.5)
x = []
y = []

for i in range(n):
  rvalue = random()
  x.append(point.x)
  y.append(point.y)

  if (rvalue < P[0]):
    rfun = F[0]
  elif (P[0] <= rvalue and rvalue < (P[0] + P[1])):
    rfun = F[1]
  elif ((P[0] + P[1]) <= rvalue and rvalue < (P[0] + P[1] + P[2])):
    rfun = F[2]
  else:
    rfun = F[3]

  point = rfun(point)

plt.scatter(x, y, color='black', marker='*')
plt.show()