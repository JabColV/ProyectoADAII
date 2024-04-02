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
    