import itertools
from generales import calcular_costo_total

def roFB(finca):
  n = len(finca)
  permutaciones = list(itertools.permutations(finca,n))
  # permutaciones = permutacion_finca(finca)
  costo_minimo_solucion = float('inf')
  permutacion_optima = []
  for i in permutaciones:
    costo_actual = calcular_costo_total(i)
    if costo_actual < costo_minimo_solucion:
      costo_minimo_solucion = costo_actual
      permutacion_optima = i
  return costo_minimo_solucion, permutacion_optima




