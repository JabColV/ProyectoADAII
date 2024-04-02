memoization = dict([])

def finca_string(finca):
  respuesta = "["
  for i in finca:
    respuesta += "[" + str(i[0]) + "," + str(i[1]) + "," + str(i[2]) + "]"
  respuesta += "]"
  return respuesta

def calcular_costo_por_tablon(tablon,tiempo_transcurrido):
  tiempo_supervivencia, tiempo_riego, prioridad = tablon
  if (tiempo_supervivencia - tiempo_riego >= tiempo_transcurrido):
    return tiempo_supervivencia - (tiempo_transcurrido + tiempo_riego)
  else:
    return prioridad * ((tiempo_transcurrido + tiempo_riego) - tiempo_supervivencia)

def calcular_costo_total(finca):
  costo_total = 0
  tiempo_trans = 0
  key = finca_string(finca)
  if memoization.get(key):
    return memoization[key]
  else:
    for i in finca:
      costo_total += calcular_costo_por_tablon(i, tiempo_trans)
      tiempo_trans += i[1]
    memoization[key] = costo_total
    return costo_total

def calcular_tiempo(finca):
  tiempo_trans = 0
  for i in finca:
    tiempo_trans += i[1]
  return tiempo_trans

def dinamico(finca):
  if len(finca) == 0:
    return finca
  min_cal = float('inf')
  programacion = []
  for i in range(len(finca)):
    finca_aux = finca[:]
    sacar = finca_aux.pop(i)
    resultado = dinamico(finca_aux) + [sacar]
    costo_total = calcular_costo_total(resultado)
    if costo_total < min_cal:
      min_cal = costo_total
      programacion = resultado
  return programacion

