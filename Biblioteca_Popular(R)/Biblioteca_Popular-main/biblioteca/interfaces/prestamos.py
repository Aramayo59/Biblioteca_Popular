import tkinter as tk
from tkinter import messagebox

def prestamos_interface():
    root = tk.Tk()
    root.title("Gestión de Préstamos - Biblioteca José H. Porto")
    
    # Definir tamaño fijo y que no se pueda cambiar
    root.geometry("1080x640+100+40")
    root.resizable(True, True)
    root.configure(bg="lightblue")


    # Crear un marco con dos colores divididos
    marco_dividido = tk.Frame(root, bd=5, relief=tk.RAISED)
    marco_dividido.grid(row=0, column=0, columnspan=2, pady=0, sticky='ew')

    # Color superior
    top_color = tk.Label(marco_dividido, bg="salmon", height=3)
    top_color.pack(side=tk.TOP, fill=tk.X)

    # Color inferior
    bottom_color = tk.Label(marco_dividido, bg="gray2", height=3)
    bottom_color.pack(side=tk.BOTTOM, fill=tk.X)

    # Título centrado en el marco
    tk.Label(marco_dividido, text="Gestión de Préstamos", font=("Arial", 24), fg="gray4").place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Campo Nombre
    tk.Label(root, text="Nombre:", font=("Arial", 14), bg= "lightblue").grid(row=1, column=0, sticky='e', padx=10, pady=10)
    nombre_entry = tk.Entry(root, font=("Arial", 14), width=20)
    nombre_entry.grid(row=1, column=1, sticky='w', padx=10)

    # Campo Apellido
    tk.Label(root, text="Apellido:", font=("Arial", 14), bg= "lightblue").grid(row=2, column=0, sticky='e', padx=10, pady=10)
    apellido_entry = tk.Entry(root, font=("Arial", 14), width=20)
    apellido_entry.grid(row=2, column=1, sticky='w', padx=10)

    # Campo DNI
    tk.Label(root, text="DNI:", font=("Arial", 14), bg= "lightblue").grid(row=3, column=0, sticky='e', padx=10, pady=10)
    dni_entry = tk.Entry(root, font=("Arial", 14), width=20)
    dni_entry.grid(row=3, column=1, sticky='w', padx=10)

    # Campo Título del Libro
    tk.Label(root, text="Título del Libro:", font=("Arial", 14), bg= "lightblue").grid(row=4, column=0, sticky='e', padx=10, pady=10)
    libro_entry = tk.Entry(root, font=("Arial", 14), width=30)
    libro_entry.grid(row=4, column=1, sticky='w', padx=10)

    # Campo Autor
    tk.Label(root, text="Autor:", font=("Arial", 14), bg= "lightblue").grid(row=5, column=0, sticky='e', padx=10, pady=10)
    autor_entry = tk.Entry(root, font=("Arial", 14), width=25)
    autor_entry.grid(row=5, column=1, sticky='w', padx=10)

    # Función para registrar el préstamo con validación
    def registrar_prestamo():
        nombre = nombre_entry.get().strip()
        apellido = apellido_entry.get().strip()
        dni = dni_entry.get().strip()
        libro = libro_entry.get().strip()
        autor = autor_entry.get().strip()

        if not nombre or not apellido or not dni or not libro or not autor:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
        else:
            messagebox.showinfo("Préstamo", f"Préstamo de '{libro}' registrado exitosamente")

    # Función para limpiar los campos y permitir un nuevo préstamo
    def nuevo_prestamo():
        nombre_entry.delete(0, tk.END)
        apellido_entry.delete(0, tk.END)
        dni_entry.delete(0, tk.END)
        libro_entry.delete(0, tk.END)
        autor_entry.delete(0, tk.END)

    # Botón para registrar el préstamo
    tk.Button(root, text="Registrar Préstamo", font=("Arial", 14), command=registrar_prestamo).grid(row=6, column=0, columnspan=2, pady=20)

    # Botón para limpiar los campos y hacer un nuevo préstamo
    tk.Button(root, text="Nuevo Préstamo", font=("Arial", 14), command=nuevo_prestamo).grid(row=7, column=0, columnspan=2, pady=10)

    # Botón para cerrar la ventana
    tk.Button(root, text="Cerrar", font=("Arial", 14), command=root.quit).grid(row=8, column=0, columnspan=2, pady=10)

    # Configurar la expansión de filas y columnas
    for i in range(8):
        root.grid_rowconfigure(i, weight=1)  # Configurar el peso de las filas
    for j in range(2):
        root.grid_columnconfigure(j, weight=1)  # Configurar el peso de las columnas

    root.mainloop()

if __name__ == "__main__":
    prestamos_interface()
