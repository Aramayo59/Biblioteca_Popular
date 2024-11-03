import tkinter as tk

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard")
        self.root.geometry("1366x768")
        self.root.configure(bg="#ff9933")  # Main background color

        # Sidebar Frame
        self.sidebar = tk.Frame(self.root, bg="#4d2600", width=250)
        self.sidebar.pack(side="left", fill="y")

        # Header in Sidebar
        header_frame = tk.Frame(self.sidebar, bg="#4d2600")
        header_frame.pack(fill="x", pady=(20, 10))
        tk.Label(header_frame, text="DIRECTOR", bg="#4d2600", fg="white", font=("Helvetica", 16, "bold")).pack()
        tk.Label(header_frame, text="Admin", bg="#4d2600", fg="white", font=("Helvetica", 12)).pack()

        # Menu Buttons
        button_font = ("Helvetica", 14, "bold")
        button_bg = "#ff9933"  # Use orange color for buttons
        button_fg = "#4d2600"  # Dark brown text color
        button_width = 15
        button_height = 2

        # Menu Item: Socios
        socios_button = tk.Button(self.sidebar, text="Socios", font=button_font, bg=button_bg, fg=button_fg,
                                  width=button_width, height=button_height, relief="flat", command=self.open_socios)
        socios_button.pack(pady=10, padx=20, fill="x")

        # Menu Item: Préstamos
        prestamos_button = tk.Button(self.sidebar, text="Préstamos", font=button_font, bg=button_bg, fg=button_fg,
                                     width=button_width, height=button_height, relief="flat", command=self.open_prestamos)
        prestamos_button.pack(pady=10, padx=20, fill="x")

        # Menu Item: Libros
        libros_button = tk.Button(self.sidebar, text="Libros", font=button_font, bg=button_bg, fg=button_fg,
                                  width=button_width, height=button_height, relief="flat", command=self.open_libros)
        libros_button.pack(pady=10, padx=20, fill="x")

        # Main content area
        self.main_content = tk.Frame(self.root, bg="#ff9933")
        self.main_content.pack(side="right", fill="both", expand=True)

    # Placeholder methods for button actions
    def open_socios(self):
        print("Abrir sección de Socios")

    def open_prestamos(self):
        print("Abrir sección de Préstamos")

    def open_libros(self):
        print("Abrir sección de Libros")

# Create and run the Tkinter app
if __name__ == "__main__":
    root = tk.Tk()
    app = Dashboard(root)
    root.mainloop()
