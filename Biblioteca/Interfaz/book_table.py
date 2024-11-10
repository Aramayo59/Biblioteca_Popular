import tkinter as tk
from tkinter import ttk

class BookTable:
    def __init__(self, root, columnas, estilo):
        self.tabla = ttk.Treeview(root, columns=columnas, show="headings", style=estilo)
        self.tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def configurar_tabla(self, color_naranja, color_marron):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", background="white", fieldbackground="white", foreground="black")
        style.configure("Treeview.Heading", background=color_marron, foreground="white", font=('Arial', 10, 'bold'))
        style.map('Treeview', background=[('selected', color_naranja)])

    def cargar_datos(self, datos):
        self.tabla.delete(*self.tabla.get_children())
        for fila in datos:
            self.tabla.insert("", "end", values=fila)

    def obtener_seleccion(self):
        selected_item = self.tabla.selection()
        if selected_item:
            return self.tabla.item(selected_item)['values'][0]
        return None
