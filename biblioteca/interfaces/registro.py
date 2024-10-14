import tkinter as tk
from tkinter import messagebox

def registro_interface():
    root = tk.Tk()
    root.title("Registro de Socios - Biblioteca José H. Porto")
    root.geometry("400x400")

    tk.Label(root, text="Registro de Socios", font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text="Nombre:").pack(pady=5)
    nombre_entry = tk.Entry(root)
    nombre_entry.pack()

    tk.Label(root, text="Apellido:").pack(pady=5)
    apellido_entry = tk.Entry(root)
    apellido_entry.pack()

    tk.Label(root, text="DNI:").pack(pady=5)
    dni_entry = tk.Entry(root)
    dni_entry.pack()

    tk.Label(root, text="Fecha de Nacimiento:").pack(pady=5)
    fecha_entry = tk.Entry(root)
    fecha_entry.pack()

    def registrar():
        nombre = nombre_entry.get()
        apellido = apellido_entry.get()
        dni = dni_entry.get()
        fecha_nacimiento = fecha_entry.get()
        # Aquí iría la lógica para guardar el socio registrado
        messagebox.showinfo("Registro", f"Socio {nombre} {apellido} registrado exitosamente")

    tk.Button(root, text="Registrar", command=registrar).pack(pady=10)
    tk.Button(root, text="Volver al inicio", command=root.destroy).pack(pady=5)
    root.mainloop()

if __name__ == "__main__":
    registro_interface()
