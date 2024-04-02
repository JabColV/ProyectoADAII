from generales import calcular_costo_total

memoization = dict([])

def roPD(finca):
  if len(finca) == 0:
    return finca
  min_cal = float('inf')
  programacion = []
  for i in range(len(finca)):
    finca_aux = finca[:]
    sacar = finca_aux.pop(i)
    resultado = roPD(finca_aux) + [sacar]
    costo_total = calcular_costo_total(resultado)
    if costo_total < min_cal:
      min_cal = costo_total
      programacion = resultado
  return programacion

