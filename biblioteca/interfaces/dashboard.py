import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Panel de Control")
root.geometry("1366x768")
root.resizable(False, False)

# Colores personalizados
color_pastel = "#d9b38c"  # Color pastel
color_marron = "#231c00"  # Marrón
color_naranja = "#ff5100"  # Naranja

# Frame lateral (parte izquierda)
frame_lateral = tk.Frame(root, bg=color_pastel, width=200)
frame_lateral.pack(side="left", fill="y")

# Sección del perfil del usuario (dentro del frame lateral)
frame_perfil = tk.Frame(frame_lateral, bg=color_marron, height=100)
frame_perfil.pack(fill="x")

# Nombre del usuario y rol
nombre_perfil = tk.Label(frame_perfil, text="DIRECTOR", font=("Arial", 14, "bold"), bg=color_marron, fg="white")
nombre_perfil.pack(pady=10)

rol_perfil = tk.Label(frame_perfil, text="Admin", font=("Arial", 10), bg=color_marron, fg="white")
rol_perfil.pack()

# Función para mostrar un mensaje al hacer clic en los botones
def mostrar_mensaje(item):
    if item == "Libros":
        alta_libros()
    else:
        print(f"Has seleccionado: {item}")

# Función para mostrar la sección de alta_libros
def alta_libros():
    # Limpiar el frame_principal
    for widget in frame_principal.winfo_children():
        widget.destroy()

    # Texto en el área principal
    label_alta_libros = tk.Label(frame_principal, text="Sección de Alta de Libros", font=("Arial", 18), bg=color_naranja)
    label_alta_libros.pack(pady=20)

    # Aquí puedes agregar más widgets específicos para la sección de alta_libros
    # Ejemplo de entrada para el título del libro
    label_titulo = tk.Label(frame_principal, text="Título del Libro:", font=("Arial", 14), bg=color_naranja)
    label_titulo.pack(pady=5)

    entrada_titulo = tk.Entry(frame_principal, font=("Arial", 12))
    entrada_titulo.pack(pady=5)

# Opciones del menú lateral
items_menu = [("Socios", "👥"), ("Préstamos", "📚"), ("Libros", "📖")]

for item, icono in items_menu:
    btn = tk.Button(frame_lateral, text=f"{icono} {item}", font=("Arial", 12), bg=color_pastel, bd=0, anchor="w",
                    command=lambda item=item: mostrar_mensaje(item))
    btn.pack(fill="x", pady=5, padx=10)

# Frame principal (parte derecha)
frame_principal = tk.Frame(root, bg=color_naranja)
frame_principal.pack(side="right", fill="both", expand=True)

# Texto en el área principal
label_bienvenida = tk.Label(frame_principal, text="Bienvenido a la Biblioteca José H. Porto", font=("Arial", 18), bg=color_naranja)
label_bienvenida.pack(pady=20)

# Iniciar la aplicación
root.mainloop()
