import tkinter as tk
from tkinter import messagebox

def socios_interface():
    root = tk.Tk()
    root.title("Gestión de Socios - Biblioteca José H. Porto")
    root.geometry("400x400")

    tk.Label(root, text="Gestión de Socios", font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text="Nombre:").pack(pady=5)
    nombre_entry = tk.Entry(root)
    nombre_entry.pack()

    tk.Label(root, text="Apellido:").pack(pady=5)
    apellido_entry = tk.Entry(root)
    apellido_entry.pack()

    tk.Label(root, text="DNI:").pack(pady=5)
    dni_entry = tk.Entry(root)
    dni_entry.pack()

    tk.Label(root, text="Fecha Último Pago:").pack(pady=5)
    pago_entry = tk.Entry(root)
    pago_entry.pack()

    def actualizar_socio():
        nombre = nombre_entry.get()
        apellido = apellido_entry.get()
        dni = dni_entry.get()
        pago = pago_entry.get()
        # Aquí iría la lógica para actualizar la información del socio
        messagebox.showinfo("Actualizar", f"Socio {nombre} actualizado exitosamente")

    tk.Button(root, text="Actualizar Socio", command=actualizar_socio).pack(pady=10)
    root.mainloop()

if __name__ == "__main__":
    socios_interface()


