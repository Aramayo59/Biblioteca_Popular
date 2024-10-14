import tkinter as tk
from tkinter import messagebox

def talleres_interface():
    root = tk.Tk()
    root.title("Gestión de Talleres - Biblioteca José H. Porto")
    root.geometry("400x400")

    tk.Label(root, text="Gestión de Talleres", font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text="Nombre del Taller:").pack(pady=5)
    taller_entry = tk.Entry(root)
    taller_entry.pack()

    tk.Label(root, text="Horario:").pack(pady=5)
    horario_entry = tk.Entry(root)
    horario_entry.pack()

    tk.Label(root, text="Profesor:").pack(pady=5)
    profesor_entry = tk.Entry(root)
    profesor_entry.pack()

    tk.Label(root, text="Número de Contacto:").pack(pady=5)
    contacto_entry = tk.Entry(root)
    contacto_entry.pack()

    def registrar_taller():
        taller = taller_entry.get()
        horario = horario_entry.get()
        profesor = profesor_entry.get()
        contacto = contacto_entry.get()
        # Aquí iría la lógica para registrar el taller
       
