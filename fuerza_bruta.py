import itertools

def calcular_costo_por_tablon(tablon,tiempo_transcurrido):
  tiempo_supervivencia = tablon[0]
  tiempo_riego = tablon[1]
  prioridad = tablon[2]
  if (tiempo_supervivencia - tiempo_riego >= tiempo_transcurrido):
    return tiempo_supervivencia - (tiempo_transcurrido + tiempo_riego)
  else:
    return prioridad * ((tiempo_transcurrido + tiempo_riego) - tiempo_supervivencia)

def calcular_costo_total(finca):
  costo_total = 0
  tiempo_trans = 0
  for i in finca:
    costo_total += calcular_costo_por_tablon(i,tiempo_trans)
    tiempo_trans += i[1]
  return costo_total

def permutacion_finca(finca):
  n = len(finca)
  permutaciones = list(itertools.permutations(finca,n))
  return permutaciones

def calcular_costo_minimo(finca):
  permutaciones = permutacion_finca(finca)
  costo_minimo_solucion = float('inf')
  permutacion_optima = []
  for i in permutaciones:
    costo_actual = calcular_costo_total(i)
    if costo_actual < costo_minimo_solucion:
      costo_minimo_solucion = costo_actual
      permutacion_optima = i
  return costo_minimo_solucion, permutacion_optima




