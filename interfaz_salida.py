import tkinter as tk
from tkinter import scrolledtext
import os
from PIL import ImageTk, Image
import dinamico
import voraz
import fuerza_bruta
import interfaz_entrada
from generales import finca_string, finca

ruta_archivo = None
def generarSalida(finca):
    if interfaz_entrada.select_var.get() == 'Dinamico':
        programacion = dinamico.roPD(finca)
        nombre_archivo = 'outputDynamic.txt'
        costo_solucion = dinamico.calcular_costo_total(programacion)
        finca_string(programacion)
    elif interfaz_entrada.select_var.get() == 'Voraz':
        programacion = voraz.roV(finca)
        costo_solucion = voraz.calcular_costo_total(programacion)
        nombre_archivo = 'outputGreedy.txt'
    elif interfaz_entrada.select_var.get() == 'Fuerza_Bruta':
        costo_solucion, programacion = fuerza_bruta.roFB(finca)
        nombre_archivo = 'outputBruteForce.txt'

    carpeta_salida = "./resultados/"

    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)
    
    # Ruta completa del archivo de salida
    global ruta_archivo
    ruta_archivo = os.path.join(carpeta_salida, nombre_archivo)

    # Guardar el costo y las posiciones en un archivo
    with open(ruta_archivo, 'w') as archivo:
        # Escribir el costo en la primera línea del archivo
        archivo.write(str(costo_solucion) + '\n')

        # Escribir las posiciones en el archivo
        for elem in programacion:
            posicion = finca.index(elem)
            if interfaz_entrada.select_var.get() == 'dinamico':
                finca[posicion] = []
            archivo.write(str(posicion) + '\n')
        
generarSalida(finca)
ventana = tk.Tk()
ventana.title("Optimizar un sistema de riego")
ventana.configure(bg="#7FBF50")
ico = Image.open('icono.png')
photo = ImageTk.PhotoImage(ico)
ventana.wm_iconphoto(False, photo)

# Configurar la posición de la ventana
ancho_pantalla = ventana.winfo_screenwidth()
altura_pantalla = ventana.winfo_screenheight()
x = int((ancho_pantalla - 500) / 2)
y = int((altura_pantalla - 600) / 2)
ventana.geometry(f"500x500+{x}+{y}")

# Estilo de la interfaz
font_title = ("Times New Roman", 20, "bold")
font_text = ("Times New Roman", 16, "bold", "italic")
font_button = ("Times New Roman", 12, "bold")

def mostrar_resultado():
    mensaje = f"Resultados obtenidos de {interfaz_entrada.select_var.get()}"
    label_bienvenida.config(text=mensaje)

# Cargar el contenido del archivo en el widget de texto
def cargar_contenido(archivo, cuadro):
    with open(archivo, 'r') as f:
        contenido = f.read()
        cuadro.delete('1.0', tk.END)
        cuadro.insert(tk.END, contenido)

cuadro_info = tk.Canvas(ventana, width=400, height=50, bg="#7FBF50", highlightbackground="#7FBF50")
cuadro_info.place(x=50, y=5, width=400, height=500)

label_bienvenida = tk.Label(ventana, text="", font=font_text, bg="#7FBF50")
label_bienvenida.place(x=250, y=50, relwidth=1, anchor="center")

label_entrada = tk.Label(ventana, text="Entrada", font=font_text, bg="#7FBF50")
label_entrada.place(x=50, y=65)
text_widget = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, font=("Arial", 12))
text_widget.place(x=50, y=100, width=400, height=150)
label_salida = tk.Label(ventana, text="Salida", font=font_text, bg="#7FBF50")
label_salida.place(x=50, y=260)
text_widget_output = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, font=("Arial", 12))
text_widget_output.place(x=50, y=290, width=400, height=150)

mostrar_resultado()
cargar_contenido("finca_escogida.txt", text_widget)
cargar_contenido(ruta_archivo, text_widget_output)
ventana.mainloop()
