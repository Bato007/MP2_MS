import numpy as np
import random as rnd

STEP_DICT = {
  0.0: 0,
  0.1: 0,
  0.2: 0,
  0.3: 0,
  0.4: 0,
  0.5: 0,
  0.6: 0,
  0.7: 0,
  0.8: 0,
  0.9: 0,
  1.0: 0,
}

def generate_values(n, generator_number):
  values = []
  x = 1
  for i in range(n):
    if (generator_number == 1):
      x = 5**5 * x % (2**35 - 1)
      result = x/(2**35 - 1)
    if (generator_number == 2):
      x = 7**5 * x % (2**31 - 1)
      result = x/(2**31 - 1)
    if (generator_number == 3):
      result = rnd.random()

    result = round(result, 2)
    values.append(result)
  
  return values

def asterisk_histogram(n, generator_number):
  step = 0.1
  table = STEP_DICT
  generated_values = generate_values(n, generator_number)
  interval = np.arange(0.0, 1.1, step)
  round_interval = np.around(interval, 1)
  for i in round_interval:
    for value in generated_values:
      if (i <= value  and value < (i + 0.1)):
        table[i] += 1
  table.pop(1)
  display_table(n, generator_number, table)


def display_table(n, generator_number, table):
  print('----------------- RESULTADOS UTILIZANDO GENERADOR ', generator_number, ' -----------------')
  print('----------------------- REPETICIONES: ', n, ' -----------------------')
  print('***********************************************************************')
  for value in table:
    percentage = table[value]*100/n
    print(value, '-', round(value+0.1, 1), ': ********************************************* (', table[value], ', ', round(percentage, 2), '%)')
  print('***********************************************************************')

# CHANGE NUMBER OF ITERATIONS
ITERATIONS = 100000

# UNCOMMENT FOR EXECUTION

# generator1 = asterisk_histogram(ITERATIONS, 1)
# generator2 = asterisk_histogram(ITERATIONS, 2)
# generator3 = asterisk_histogram(ITERATIONS, 3)