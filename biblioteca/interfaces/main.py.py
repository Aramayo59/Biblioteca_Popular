import tkinter as tk
from login import Login
from dashboard import Dashboard
from alta_libros import AltaLibros


class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Ocultar la ventana principal inicialmente

       
        self.show_login()

    def show_login(self):
        self.login_window = Login(self.root, self.on_login_success)
        

    def on_login_success(self):
        self.login_window.hide()
        self.show_dashboard()

    def show_dashboard(self):
        self.dashboard_window = Dashboard(self.root, self.on_open_alta_libros)
        self.dashboard_window.show()

    def on_open_alta_libros(self):
        self.dashboard_window.hide()
        self.show_alta_libros()

    def show_alta_libros(self):
        self.alta_libros_window = AltaLibros(self.root)
        self.alta_libros_window.show()

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = MainApp()
    app.run()
