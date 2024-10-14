import tkinter as tk
from tkinter import messagebox

def prestamos_interface():
    root = tk.Tk()
    root.title("Gestión de Préstamos - Biblioteca José H. Porto")
    root.geometry("400x400")

    tk.Label(root, text="Gestión de Préstamos", font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text="Nombre:").pack(pady=5)
    nombre_entry = tk.Entry(root)
    nombre_entry.pack()

    tk.Label(root, text="DNI:").pack(pady=5)
    dni_entry = tk.Entry(root)
    dni_entry.pack()

    tk.Label(root, text="Título del Libro:").pack(pady=5)
    libro_entry = tk.Entry(root)
    libro_entry.pack()

    tk.Label(root, text="Autor:").pack(pady=5)
    autor_entry = tk.Entry(root)
    autor_entry.pack()

    def registrar_prestamo():
        nombre = nombre_entry.get()
        dni = dni_entry.get()
        libro = libro_entry.get()
        autor = autor_entry.get()
        # Aquí iría la lógica para registrar el préstamo
        messagebox.showinfo("Préstamo", f"Préstamo de '{libro}' registrado exitosamente")

    tk.Button(root, text="Registrar Préstamo", command=registrar_prestamo).pack(pady=10)
    root.mainloop()

if __name__ == "__main__":
    prestamos_interface()
