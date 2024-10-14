import tkinter as tk
from tkinter import messagebox

def login_interface():
    root = tk.Tk()
    root.title("Iniciar Sesión - Biblioteca José H. Porto")
    root.geometry("400x300")

    tk.Label(root, text="Iniciar Sesión", font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text="Usuario:").pack(pady=5)
    user_entry = tk.Entry(root)
    user_entry.pack()

    tk.Label(root, text="Contraseña:").pack(pady=5)
    pass_entry = tk.Entry(root, show="*")
    pass_entry.pack()

    def iniciar_sesion():
        user = user_entry.get()
        password = pass_entry.get()
        # Lógica para verificar usuario y contraseña
        if user == "admin" and password == "1234":
            messagebox.showinfo("Login", "Inicio de sesión exitoso")
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    tk.Button(root, text="Iniciar Sesión", command=iniciar_sesion).pack(pady=10)
    tk.Button(root, text="Registrarse", command=lambda: messagebox.showinfo("Registro", "Ir a la pantalla de registro")).pack(pady=5)
    root.mainloop()

if __name__ == "__main__":
    login_interface()
