import tkinter as tk
from tkinter import messagebox

class Login:
    def __init__(self, root, on_success):
        self.root = root
        self.window = tk.Toplevel(self.root)
        self.window.title("Login")
        self.on_success = on_success
        self.window.geometry("1366x768")  # Tamaño expandido de la ventana
        self.window.resizable(False, False)  # Hacer que la ventana no se pueda redimensionar

        # Fondo de color naranja sólido
        self.window.configure(bg="#ff9933")  # Fondo naranja

        # Encabezado
        self.header = tk.Frame(self.window, bg="#4d2600", height=80)  # Marrón oscuro para contraste
        self.header.place(relwidth=1, y=0)
        tk.Label(self.header, text="Login", bg="#4d2600", fg="white", font=("Helvetica", 32, "bold")).pack(pady=15)

        # Campos de entrada y etiquetas con posiciones y fuente actualizadas para la ventana grande
        tk.Label(self.window, text="Usuario:", font=("Helvetica", 18, "bold"), bg="#ff9933").place(x=533, y=250)
        self.username_entry = tk.Entry(self.window, font=("Helvetica", 18), width=30)
        self.username_entry.place(x=533, y=290)

        tk.Label(self.window, text="Contraseña:", font=("Helvetica", 18, "bold"), bg="#ff9933").place(x=533, y=350)
        self.password_entry = tk.Entry(self.window, show="*", font=("Helvetica", 18), width=30)
        self.password_entry.place(x=533, y=390)

        # Botón de login con efectos de hover
        login_button = tk.Button(
            self.window, text="Ingresar", command=self.validate_login, font=("Helvetica", 18, "bold"),
            bg="#4d2600", fg="white", activebackground="#7a4b2a", activeforeground="white", width=15
        )
        login_button.place(x=616, y=470)

    def validate_login(self):
        if self.username_entry.get() == "admin" and self.password_entry.get() == "1234":
            messagebox.showinfo("Login", "Ingreso exitoso")
            self.on_success()
        else:
            messagebox.showerror("Login", "Usuario o contraseña incorrectos")

    def show(self):
        self.window.deiconify()

    def hide(self):
        self.window.withdraw()
