import tkinter as tk
from tkinter import messagebox

class Login:
    def __init__(self, root, on_success):
        self.root = root
        self.window = tk.Toplevel(self.root)
        self.window.title("Login")
        self.on_success = on_success
        self.window.geometry("1366x768")
        self.window.resizable(False, False)

        # Fondo de color naranja
        self.window.configure(bg="#ff9933")  # Fondo naranja

        # Encabezado
        tk.Label(self.window, text="¡BIENVENIDO!", font=("Helvetica", 48, "bold"), fg="white", bg="#ff9933").place(relx=0.5, y=50, anchor="center")
        tk.Label(self.window, text="BIBLIOTECA JOSE H. PORTO", font=("Helvetica", 32, "bold"), fg="white", bg="#ff9933").place(relx=0.5, y=150, anchor="center")
        tk.Label(self.window, text="INGRESA TUS DATOS", font=("Helvetica", 18, "bold"), fg="white", bg="#ff9933").place(relx=0.5, y=220, anchor="center")

        # Frame para campos de entrada con fondo pastel y bordes redondeados
        self.login_frame = tk.Frame(self.window, bg="#d9b38c", bd=2, relief="groove")
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center", width=350, height=200)

        # Campo de entrada para usuario
        tk.Label(self.login_frame, text="Usuario:", font=("Helvetica", 14, "bold"), bg="#d9b38c", fg="#231c00").pack(pady=(10, 5))
        self.username_entry = tk.Entry(self.login_frame, font=("Helvetica", 14), bd=2, relief="flat", width=30)
        self.username_entry.pack()

        # Campo de entrada para contraseña
        tk.Label(self.login_frame, text="Contraseña:", font=("Helvetica", 14, "bold"), bg="#d9b38c", fg="#231c00").pack(pady=(10, 5))

        # Variable para controlar la visibilidad de la contraseña
        self.password_visible = False
        self.password_entry = tk.Entry(self.login_frame, show="*", font=("Helvetica", 14), bd=2, relief="flat", width=30)
        self.password_entry.pack()

        # Botón para mostrar/ocultar la contraseña
        self.toggle_button = tk.Button(self.login_frame, text="Mostrar", font=("Helvetica", 10), command=self.toggle_password, bg="#4d2600", fg="white", relief="flat")
        self.toggle_button.pack(pady=5)

        # Botón de login en color marrón oscuro
        login_button = tk.Button(
            self.window, text="INICIAR SESIÓN", command=self.validate_login, font=("Helvetica", 14, "bold"),
            bg="#4d2600", fg="white", activebackground="#4d2600", activeforeground="white", width=15
        )
        login_button.place(relx=0.5, y=600, anchor="center")

    def toggle_password(self):
        """Función para mostrar u ocultar la contraseña."""
        if self.password_visible:
            self.password_entry.config(show="*")
            self.toggle_button.config(text="Mostrar")
            self.password_visible = False
        else:
            self.password_entry.config(show="")
            self.toggle_button.config(text="Ocultar")
            self.password_visible = True

    def validate_login(self):
        if self.username_entry.get() == "admin" and self.password_entry.get() == "1234":
            messagebox.showinfo("Login", "Ingreso exitoso")
            self.on_success()  # Llamar a la función de éxito para abrir el dashboard
        else:
            messagebox.showerror("Login", "Usuario o contraseña incorrectos")

    def show(self):
        self.window.deiconify()

    def hide(self):
        self.window.withdraw()
