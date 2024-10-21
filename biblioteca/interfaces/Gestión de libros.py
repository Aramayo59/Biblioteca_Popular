import tkinter as tk
from tkinter import messagebox

def libros_interface():
    root = tk.Tk()
    root.title("Gestión de Libros - Biblioteca José H. Porto")
    root.geometry("1366x768")
    root.resizable(False, False)  # Desactivar la opción de redimensionar la ventana

    # Colores
    fondo_color = "#5277FF"  # Azul de fondo
    texto_color = "#FFF852"   # Amarillo para texto
    boton_color = "#38B6FF"   # Celeste para botones

    # Configurar color de fondo de la ventana
    root.config(bg=fondo_color)

    # Etiqueta de título
    tk.Label(root, text="Gestión de Libros", font=("Arial", 24), fg=texto_color, bg=fondo_color).pack(pady=20)

    # Campo de título
    tk.Label(root, text="Título:", font=("Arial", 14), fg=texto_color, bg=fondo_color).pack(pady=5)
    titulo_entry = tk.Entry(root, font=("Arial", 12), bg="white")
    titulo_entry.pack(pady=5)

    # Campo de autor
    tk.Label(root, text="Autor:", font=("Arial", 14), fg=texto_color, bg=fondo_color).pack(pady=5)
    autor_entry = tk.Entry(root, font=("Arial", 12), bg="white")
    autor_entry.pack(pady=5)

    # Campo de editorial
    tk.Label(root, text="Editorial:", font=("Arial", 14), fg=texto_color, bg=fondo_color).pack(pady=5)
    editorial_entry = tk.Entry(root, font=("Arial", 12), bg="white")
    editorial_entry.pack(pady=5)

    # Campo de edición
    tk.Label(root, text="Edición:", font=("Arial", 14), fg=texto_color, bg=fondo_color).pack(pady=5)
    edicion_entry = tk.Entry(root, font=("Arial", 12), bg="white")
    edicion_entry.pack(pady=5)

    # Función para registrar el libro
    def registrar_libro():
        titulo = titulo_entry.get()
        autor = autor_entry.get()
        editorial = editorial_entry.get()
        edicion = edicion_entry.get()

        # Aquí iría la lógica para registrar el libro
        messagebox.showinfo("Registro de Libro", f"Libro '{titulo}' registrado exitosamente")

    # Botón para registrar el libro
    tk.Button(root, text="Registrar Libro", font=("Arial", 14), bg=boton_color, command=registrar_libro).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    libros_interface()

