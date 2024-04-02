import tkinter as tk
from tkinter import StringVar, filedialog, messagebox, scrolledtext
import shutil
import os
from PIL import ImageTk, Image

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
y = int((altura_pantalla - 450) / 2)
ventana.geometry(f"500x450+{x}+{y}")

# Estilo de la interfaz
font_title = ("Times New Roman", 20, "bold")
font_text = ("Times New Roman", 16, "bold", "italic")
font_button = ("Times New Roman", 12, "bold")

# Variable para el menú desplegable
select_var = StringVar(ventana)
select_var.set('Elige un algoritmo')
file = None

def mostrar_bienvenida():
    mensaje = "Bienvenido, por favor, selecciona tu finca"
    label_bienvenida.config(text=mensaje)

#Para abrir el explorador de archivos y seleccionar el archivo que se usará.
def seleccionar_archivo():
    global file
    archivo = filedialog.askopenfilename(title="Seleccionar archivo")
    file = archivo
    if archivo:
        confirmar_sobrescritura(archivo)

#Para copiar el archivo seleccionado en el archivo que se usará.
def confirmar_sobrescritura(archivo):
    global file
    confirmar = tk.messagebox.askyesno("Confirmar sobrescritura", f"¿Deseas sobrescribir el archivo?")
    if confirmar:
        shutil.copy2(archivo, "./finca_escogida.txt")
        nombre_archivo = os.path.basename(archivo)
        cuadro_info.delete("nombre_archivo")
        cuadro_info.create_text(200, 160, text=f'Finca seleccionada: { nombre_archivo}', width=400, font=("Arial-Black", 10), tag="nombre_archivo")
        tk.messagebox.showinfo("Sobrescritura exitosa", f"El archivo ha sido sobrescrito")
        # Cargar el contenido del archivo en el widget de texto
        cargar_contenido(archivo)
    else:
        file = None

# Cargar el contenido del archivo en el widget de texto
def cargar_contenido(archivo):
    with open(archivo, 'r') as f:
        contenido = f.read()
        text_widget.delete('1.0', tk.END)
        text_widget.insert(tk.END, contenido)

def on_select_change(event):
    selected_option = select_var.get()
    # Para ejecutar el archivo correspondiente al algoritmo seleccionado.
    comando = f"python {selected_option}.py"

    if selected_option and file:
        continuar(comando)
    else:
        select_var.set('Elige un algoritmo')
        messagebox.showerror("Error", "Debes seleccionar un archivo")

# Destruye la ventana actual y ejecuta el comando correspondiente.
def continuar(comando):
    ventana.destroy()
    os.system(comando)

cuadro_info = tk.Canvas(ventana, width=400, height=50, bg="#7FBF50", highlightbackground="#7FBF50")
cuadro_info.place(x=50, y=5, width=400, height=500)

label_bienvenida = tk.Label(ventana, text="", font=font_text, bg="#7FBF50")
label_bienvenida.place(x=250, y=50, relwidth=1, anchor="center")

# Botón para seleccionar archivo
btn_seleccionar = tk.Button(ventana, text="Seleccionar Finca", command=seleccionar_archivo, font=font_button, relief="raised", bg="#0FA644",
                            highlightbackground="#0FA644", activebackground="#0FA644")
btn_seleccionar.place(x=170, y=100, width=160, height=40)

# Menú desplegable para seleccionar algoritmo
select_options = ['Fuerza_Bruta', 'Voraz', 'Dinamico']
select_menu = tk.OptionMenu(ventana, select_var, *select_options, command=on_select_change)
select_menu.place(x=170, y=180, width=160, height=40)
select_menu.config(font=font_button, bg="#0FA644", fg="BLACK", activebackground="#0FA644", activeforeground="BLACK")
select_menu["menu"].config(bg="#0FA644", fg="BLACK", activebackground="#7EC34C", activeforeground="BLACK")

text_widget = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, font=("Arial", 12))
text_widget.place(x=50, y=270, width=400, height=150)
label_entrada = tk.Label(ventana, text="Entrada", font=font_text, bg="#7FBF50")
label_entrada.place(x=50, y=240)

mostrar_bienvenida()

ventana.mainloop()
