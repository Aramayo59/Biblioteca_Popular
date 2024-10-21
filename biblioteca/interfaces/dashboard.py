import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Panel de Control")
root.geometry("1366x768")
root.resizable(False, False)



# Colores personalizados
color_azul = "#5277FF"
color_celeste = "#38B6FF"
color_amarillo = "#FFF852"

# Frame lateral (parte izquierda)
frame_lateral = tk.Frame(root, bg=color_celeste, width=200)
frame_lateral.pack(side="left", fill="y")

# Sección del perfil del usuario (dentro del frame lateral)
frame_perfil = tk.Frame(frame_lateral, bg=color_azul, height=100)
frame_perfil.pack(fill="x")

# Nombre del usuario y rol
nombre_perfil = tk.Label(frame_perfil, text="DIRECTOR", font=("Arial", 14, "bold"), bg=color_azul, fg="white")
nombre_perfil.pack(pady=10)

rol_perfil = tk.Label(frame_perfil, text="Admin", font=("Arial", 10), bg=color_azul, fg="white")
rol_perfil.pack()

# Opciones del menú lateral
items_menu = [("Socios", "👥"), ("Préstamos", "📚"), ("Libros", "📖")]

for item, icono in items_menu:
    btn = tk.Button(frame_lateral, text=f"{icono} {item}", font=("Arial", 12), bg=color_celeste, bd=0, anchor="w")
    btn.pack(fill="x", pady=5, padx=10)

# Frame principal (parte derecha)
frame_principal = tk.Frame(root, bg=color_amarillo)
frame_principal.pack(side="right", fill="both", expand=True)

# Texto en el área principal
label_bienvenida = tk.Label(frame_principal, text="Bienvenido a la Biblioteca José H. Porto", font=("Arial", 18), bg=color_amarillo)
label_bienvenida.pack(pady=20)

# Iniciar la aplicación
root.mainloop()
