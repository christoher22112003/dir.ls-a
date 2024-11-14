import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Necesitar�s Pillow para manejar im�genes

# Funci�n para verificar el n�mero de c�dula
def verificar_cedula():
    cedula = entry_cedula.get()
    
    # Aqu� puedes agregar la l�gica para verificar la c�dula
    if len(cedula) == 10 and cedula.isdigit():
        messagebox.showinfo("Exito", "Cedula verificada con exito.")
    else:
        messagebox.showerror("Error", "Cedula invalida. Debe tener 10 digitos.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Inicio de Sesion")

# Abrir en pantalla completa
ventana.attributes('-fullscreen', True)

# Cargar la imagen de fondo
imagen_fondo = Image.open("resources/wallhaven-p97wkj.png")  # Cambia 'fondo.jpg' por el nombre de tu imagen
imagen_fondo = imagen_fondo.resize((ventana.winfo_screenwidth(), ventana.winfo_screenheight()), Image.ANTIALIAS)
fondo = ImageTk.PhotoImage(imagen_fondo)

# Crear un Label para la imagen de fondo
label_fondo = tk.Label(ventana, image=fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Crear un marco para el inicio de sesion
frame_login = tk.Frame(ventana, bg="white", bd=5, relief=tk.RAISED)
frame_login.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Crear el nuevo Label para el mensaje de bienvenida
label_bienvenida = tk.Label(frame_login, text="Bienvenido por favor ingrese su", bg="white", font=("Roboto", 14))
label_bienvenida.pack(pady=10)

# Etiqueta y campo de entrada para la cedula
label_cedula = tk.Label(frame_login, text="Numero de Cedula:", bg="white", font=("Roboto", 24, "bold"))
label_cedula.pack(pady=10)

entry_cedula = tk.Entry(frame_login, font=("Roboto", 14), bd=2, relief=tk.GROOVE)
entry_cedula.pack(pady=10, padx=20)

# Bot�n para verificar la cedula
boton_verificar = tk.Button(frame_login, text="Verificar", command=verificar_cedula, font=("Roboto", 14), bg="#0067b8", fg="white")
boton_verificar.pack(pady=20)

# Iniciar el bucle de la interfaz
ventana.mainloop()