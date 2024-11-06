import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Dashboard:
    def __init__(self, root, on_open_alta_libros=None):
        self.root = root
        self.window = tk.Toplevel(self.root)
        self.window.title("Dashboard")
        self.window.geometry("1366x768")
        self.window.resizable(False, False)
        self.window.configure(bg="#ff9933")  # Color de fondo principal
        self.on_open_alta_libros = on_open_alta_libros  # Callback para abrir alta_libros
        self.window.protocol("WM_DELETE_WINDOW", self.root.quit)

        # Marco de la barra lateral
        self.sidebar = tk.Frame(self.window, bg="#4d2600", width=250)
        self.sidebar.pack(side="left", fill="y")

        # Encabezado en la barra lateral
        header_frame = tk.Frame(self.sidebar, bg="#4d2600")
        header_frame.pack(fill="x", pady=(20, 10))
        tk.Label(header_frame, text="DIRECTOR", bg="#4d2600", fg="white", font=("Helvetica", 16, "bold")).pack()
        tk.Label(header_frame, text="Admin", bg="#4d2600", fg="white", font=("Helvetica", 12)).pack()

        # Botones del menú
        button_font = ("Helvetica", 14, "bold")
        button_bg = "#ff9933"
        button_fg = "#4d2600"
        button_width = 15
        button_height = 2

        # Crear botones con efectos hover
        self.create_button("Socios", self.open_socios, button_font, button_bg, button_fg, button_width, button_height)
        self.create_button("Préstamos", self.open_prestamos, button_font, button_bg, button_fg, button_width, button_height)
        self.create_button("Libros", self.open_libros, button_font, button_bg, button_fg, button_width, button_height)

        # Área de contenido principal
        self.main_content = tk.Frame(self.window, bg="#ff9933")
        self.main_content.pack(side="right", fill="both", expand=True)

        # Cargar y mostrar la imagen del logo en el área principal
        self.load_logo()

    def load_logo(self):
        # Cargar la imagen desde la ruta local
        image_path = "C:/Users/yamil/OneDrive/Escritorio/Biblioteca/imagen_biblioteca2.jpg"  # Ruta local
        try:
            logo = Image.open(image_path)
            logo = logo.resize((800, 700), Image.LANCZOS)
            logo_img = ImageTk.PhotoImage(logo)

            # Muestra la imagen en una etiqueta (label) en el área principal
            logo_label = tk.Label(self.main_content, image=logo_img, bg="#ff9933")
            logo_label.image = logo_img  # Mantener referencia
            logo_label.place(relx=0.5, rely=0.5, anchor="center")
            logo_label.lift()
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo en {image_path}.")

    def create_button(self, text, command, font, bg, fg, width, height):
        button = tk.Button(self.sidebar, text=text, font=font, bg=bg, fg=fg,
                           width=width, height=height, relief="flat", command=command)
        button.pack(pady=10, padx=20, fill="x")
        button.bind("<Enter>", lambda e: button.config(bg="#d9b38c"))
        button.bind("<Leave>", lambda e: button.config(bg=bg))

    def open_socios(self):
        print("Abrir sección de Socios")

    def open_prestamos(self):
        print("Abrir sección de Préstamos")

    def open_libros(self):
        self.libros_button = tk.Button(self.root, text="Libros", command=self.abrir_alta_libros)
        self.libros_button.pack(pady=20)
        print("Abrir sección de Libros")

    def abrir_alta_libros(self):
        # Crear una nueva ventana para AltaLibros
        alta_libros_window = tk.Toplevel(self.root)
        AltaLibros(alta_libros_window)

    def show(self):
        self.window.deiconify()

    def hide(self):
        self.window.withdraw()
