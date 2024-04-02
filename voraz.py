from generales import calcular_costo_total

def roV(finca_entrada):
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





