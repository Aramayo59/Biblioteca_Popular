import tkinter as tk
from tkinter import messagebox

def libros_interface():
    root = tk.Tk()
    root.title("Gestión de Libros - Biblioteca José H. Porto")
    root.geometry("400x400")

    tk.Label(root, text="Gestión de Libros", font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text="Título:").pack(pady=5)
    titulo_entry = tk.Entry(root)
    titulo_entry.pack()

    tk.Label(root, text="Autor:").pack(pady=5)
    autor_entry = tk.Entry(root)
    autor_entry.pack()

    tk.Label(root, text="Editorial:").pack(pady=5)
    editorial_entry = tk.Entry(root)
    editorial_entry.pack()

    tk.Label(root, text="Edición:").pack(pady=5)
    edicion_entry = tk.Entry(root)
    edicion_entry.pack()

    def registrar_libro():
        titulo = titulo_entry.get()
        autor = autor_entry.get()
        editorial = editorial_entry.get()
        edicion = edicion_entry.get()
        # Aquí iría la lógica para registrar el libro
        messagebox.showinfo("Registro de Libro", f"Libro '{titulo}' registrado exitosamente")

    tk.Button(root, text="Registrar Libro", command=registrar_libro).pack(pady=10)
    root.mainloop()

if __name__ == "__main__":
    libros_interface()
