#ALGORTIMO VORAZ #3
# CALCULANDO COSTOS DE MANERA DINAMICA #2

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
    costo_total += calcular_costo_por_tablon(i, tiempo_trans)
    tiempo_trans += i[1]
  return costo_total


def voraz(finca_entrada):
  finca = finca_entrada.copy()
  costo_actual = calcular_costo_total(finca)
  #print("costo_actual",costo_actual)
  modificado = True
  while modificado:
    modificado = False
    for i in range(len(finca)-1):
      finca_aux = finca.copy()
      temp = finca_aux[i]
      finca_aux[i] = finca_aux[i+1]
      finca_aux[i+1] = temp
      costo_aux = calcular_costo_total(finca_aux)
      if (costo_aux < costo_actual):
        modificado = True
        costo_actual = costo_aux
        #print("costo_actual",costo_actual)
        finca = finca_aux.copy()
        #print(finca)
      if (i+2 < len(finca)):
        finca_aux = finca.copy()
        temp = finca_aux[i]
        finca_aux[i] = finca_aux[i+2]
        finca_aux[i+2] = temp
        costo_aux = calcular_costo_total(finca_aux)
        if (costo_aux < costo_actual):
          modificado = True
          costo_actual = costo_aux
          #print("costo_actual",costo_actual)
          finca = finca_aux.copy()
          #print(finca)
  finca2 = finca_entrada.copy()
  finca2.reverse()
  costo_actual = calcular_costo_total(finca2)
  #print("costo_actual",costo_actual)
  modificado = True
  while modificado:
    modificado = False
    for i in range(len(finca2)-1):
      finca_aux = finca2.copy()
      temp = finca_aux[i]
      finca_aux[i] = finca_aux[i+1]
      finca_aux[i+1] = temp
      costo_aux = calcular_costo_total(finca_aux)
      if (costo_aux < costo_actual):
        modificado = True
        costo_actual = costo_aux
        #print("costo_actual",costo_actual)
        finca2 = finca_aux.copy()
        #print(finca)
      if (i+2 < len(finca2)):
        finca_aux = finca2.copy()
        temp = finca_aux[i]
        finca_aux[i] = finca_aux[i+2]
        finca_aux[i+2] = temp
        costo_aux = calcular_costo_total(finca_aux)
        if (costo_aux < costo_actual):
          modificado = True
          costo_actual = costo_aux
          #print("costo_actual",costo_actual)
          finca2 = finca_aux.copy()
          #print(finca)
  if(calcular_costo_total(finca) > calcular_costo_total(finca2)):
    return finca2
  return finca

ruta_archivo = None



