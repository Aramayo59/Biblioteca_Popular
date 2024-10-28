import tkinter as tk
from tkinter import messagebox

def login_interface():
    root = tk.Tk()
    root.title("Iniciar Sesión - Biblioteca José H. Porto")
    root.geometry("1366x768")
    root.resizable(False, False)

    # Colores
    fondo_color = "#ff5100"  
    boton_color = "#d9b38c"   
    boton_hover = "#ff8533"   
    texto_color = "#231c00"   

    root.config(bg=fondo_color)

    tk.Label(root, text="Iniciar Sesión", font=("Arial", 24), fg=texto_color, bg=fondo_color).pack(pady=30)

    tk.Label(root, text="Usuario:", font=("Arial", 14), fg=texto_color, bg=fondo_color).pack(pady=10)
    user_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="solid")
    user_frame.pack(pady=5)
    user_entry = tk.Entry(user_frame, font=("Arial", 12), bg="white", width=30, bd=0)
    user_entry.pack(pady=5)

    tk.Label(root, text="Contraseña:", font=("Arial", 14), fg=texto_color, bg=fondo_color).pack(pady=10)
    pass_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="solid")
    pass_frame.pack(pady=5)
    pass_entry = tk.Entry(pass_frame, show="*", font=("Arial", 12), bg="white", width=30, bd=0)
    pass_entry.pack(pady=5)

    show_pass_var = tk.IntVar()
    def toggle_password():
        pass_entry.config(show="" if show_pass_var.get() else "*")

    tk.Checkbutton(root, text="Mostrar contraseña", variable=show_pass_var, command=toggle_password, bg=fondo_color, fg=texto_color).pack(pady=10)

    def open_control_panel():
        root.destroy()  # Cerrar la ventana de inicio de sesión
        
        panel = tk.Tk()
        panel.title("Panel de Control")
        panel.geometry("1366x768")
        panel.resizable(False, False)

        color_pastel = "#d9b38c"  
        color_marron = "#231c00"  
        color_naranja = "#ff5100"  

        frame_lateral = tk.Frame(panel, bg=color_pastel, width=200)
        frame_lateral.pack(side="left", fill="y")

        frame_perfil = tk.Frame(frame_lateral, bg=color_marron, height=100)
        frame_perfil.pack(fill="x")

        nombre_perfil = tk.Label(frame_perfil, text="DIRECTOR", font=("Arial", 16, "bold"), bg=color_marron, fg="white")
        nombre_perfil.pack(pady=10)

        rol_perfil = tk.Label(frame_perfil, text="Admin", font=("Arial", 12), bg=color_marron, fg="white")
        rol_perfil.pack()

        items_menu = [("Socios", "👥"), ("Préstamos", "📚"), ("Libros", "📖")]
        for item, icono in items_menu:
            btn = tk.Button(frame_lateral, text=icono + " " + item, font=("Arial", 14), bg=color_pastel, bd=0, anchor="w", width=20)
            btn.pack(fill="x", pady=10, padx=10)

        frame_principal = tk.Frame(panel, bg=color_naranja)
        frame_principal.pack(side="right", fill="both", expand=True)

        label_bienvenida = tk.Label(frame_principal, text="Bienvenido a la Biblioteca José H. Porto", font=("Arial", 20), bg=color_naranja)
        label_bienvenida.pack(pady=20)

        panel.mainloop()

    def iniciar_sesion():
        user = user_entry.get()
        password = pass_entry.get()

        if not user or not password:
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos")
            return
        
        if user == "admin" and password == "1234":
            messagebox.showinfo("Login", "Inicio de sesión exitoso")
            open_control_panel()  # Abrir el panel de control
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    login_button = tk.Button(root, text="Iniciar Sesión", font=("Arial", 14), bg=boton_color, fg="black", width=20, height=2, command=iniciar_sesion, bd=2, relief="solid", highlightbackground="#231c00")
    login_button.pack(pady=20)

    def on_enter(e):
        login_button.config(bg=boton_hover)

    def on_leave(e):
        login_button.config(bg=boton_color)

    login_button.bind("<Enter>", on_enter)
    login_button.bind("<Leave>", on_leave)

    root.mainloop()

if __name__ == "__main__":
    login_interface()
