import tkinter as tk
from tkinter import ttk, messagebox

class BookForm:
    def __init__(self, root, color_marron, color_naranja, callback_agregar, callback_eliminar, callback_volver):
        frame = tk.Frame(root, bg=color_marron)
        frame.pack(pady=10)

        labels = ["Título:", "Autor:", "Editorial:", "ISBN:", "Categoría:", "Subcategoría:", "Descripción:"]
        self.entries = {}
        for i, label in enumerate(labels):
            tk.Label(frame, text=label, bg=color_marron, fg="white").grid(row=i, column=0, padx=10, pady=5)
            if i == 6:  # Descripción (usar Text)
                self.entries[label] = tk.Text(frame, height=4, width=30, bg=color_naranja, fg="black")
                self.entries[label].grid(row=i, column=1, padx=10, pady=5)
            else:
                entry = tk.Entry(frame, bg=color_naranja, fg="black") if i != 4 and i != 5 else ttk.Combobox(frame)
                entry.grid(row=i, column=1, padx=10, pady=5)
                self.entries[label] = entry

        self.entries["Categoría:"].bind("<<ComboboxSelected>>", callback_agregar)

        tk.Button(frame, text="Agregar Libro", bg=color_naranja, command=callback_agregar).grid(row=7, column=0, padx=10, pady=10)
        tk.Button(frame, text="Eliminar Libro", bg=color_naranja, command=callback_eliminar).grid(row=7, column=1, padx=10, pady=10)
        tk.Button(frame, text="Volver", bg=color_naranja, command=callback_volver).grid(row=7, column=2, padx=10, pady=10)

    def obtener_valores(self):
        valores = {label: self.entries[label].get() if label != "Descripción:" else self.entries[label].get("1.0", tk.END).strip() for label in self.entries}
        return valores

    def limpiar_campos(self):
        for label, widget in self.entries.items():
            if isinstance(widget, tk.Entry) or isinstance(widget, ttk.Combobox):
                widget.delete(0, tk.END)
            elif isinstance(widget, tk.Text):
                widget.delete("1.0", tk.END)
