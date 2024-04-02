def leer_archivo(filename):
    try:
        finca = []
        with open(filename, 'r') as file:
            n = int(file.readline().strip())
            for _ in range(n):
                tiempo_supervivencia, tiempo_riego, prioridad = file.readline().strip().split(",")
                finca.append((int(tiempo_supervivencia), int(tiempo_riego), int(prioridad)))
        return finca
    except Exception as e:  # Captura cualquier excepción
            print(f"Error al leer el archivo: {e}")
            return None 
    
finca = leer_archivo("finca_escogida.txt")

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

def calcular_tiempo(finca):
  tiempo_trans = 0
  for i in finca:
    tiempo_trans += i[1]
  return tiempo_trans

def finca_string(finca):
  respuesta = "["
  for i in finca:
    respuesta += "[" + str(i[0]) + "," + str(i[1]) + "," + str(i[2]) + "]"
  respuesta += "]"
  return respuesta