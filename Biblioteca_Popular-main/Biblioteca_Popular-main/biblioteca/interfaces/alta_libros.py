import tkinter as tk
from tkinter import ttk, messagebox


class AltaLibros:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Biblioteca")
        self.root.geometry("1366x768")
        self.root.resizable(False, False)

        # Colores personalizados
        self.color_naranja = "#ff9933"  # Naranja
        self.color_marron = "#4d2600"    # Marrón oscuro

        # Aplicar color de fondo a toda la ventana
        self.root.configure(bg=self.color_marron)

        # Crear un estilo personalizado para la tabla (Treeview)
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", background=self.color_naranja, fieldbackground=self.color_naranja, foreground="black")
        style.configure("Treeview.Heading", background=self.color_marron, foreground="white")
        style.map('Treeview', background=[('selected', self.color_marron)])

        # Tabla para mostrar los libros
        self.columnas = ("ID", "ISBN", "Título", "Categoría", "Subcategoría", "Autor", "Editorial", "Descripción")
        self.tabla_libros = ttk.Treeview(root, columns=self.columnas, show="headings", style="Treeview")
        for col in self.columnas:
            self.tabla_libros.heading(col, text=col)
            self.tabla_libros.column(col, width=100)

        self.tabla_libros.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Marco para los detalles del libro
        frame = tk.Frame(root, bg=self.color_marron)
        frame.pack(pady=10)

        # Etiquetas y entradas para los detalles del libro
        tk.Label(frame, text="Título:", bg=self.color_marron, fg="white").grid(row=0, column=0, padx=10, pady=5)
        self.entrada_titulo = tk.Entry(frame, bg=self.color_naranja, fg="black")
        self.entrada_titulo.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(frame, text="Autor:", bg=self.color_marron, fg="white").grid(row=1, column=0, padx=10, pady=5)
        self.entrada_autor = tk.Entry(frame, bg=self.color_naranja, fg="black")
        self.entrada_autor.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(frame, text="Editorial:", bg=self.color_marron, fg="white").grid(row=2, column=0, padx=10, pady=5)
        self.entrada_editorial = tk.Entry(frame, bg=self.color_naranja, fg="black")
        self.entrada_editorial.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(frame, text="ISBN:", bg=self.color_marron, fg="white").grid(row=3, column=0, padx=10, pady=5)
        self.entrada_isbn = tk.Entry(frame, bg=self.color_naranja, fg="black")
        self.entrada_isbn.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(frame, text="ID", bg=self.color_marron, fg="white").grid(row=4, column=0, padx=10, pady=5)
        self.entrada_libro_id = tk.Entry(frame, bg=self.color_naranja, fg="black")
        self.entrada_libro_id.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(frame, text="Categoría:", bg=self.color_marron, fg="white").grid(row=5, column=0, padx=10, pady=5)
        self.categoria_var = tk.StringVar()
        self.desplegable_categoria = ttk.Combobox(frame, textvariable=self.categoria_var)
        self.desplegable_categoria['values'] = ("Novela", "Salud", "Tecnología")
        self.desplegable_categoria.grid(row=5, column=1, padx=10, pady=5)
        self.desplegable_categoria.bind("<<ComboboxSelected>>", self.actualizar_subcategorias)

        # Dropdown de Subcategoría
        tk.Label(frame, text="Subcategoría:", bg=self.color_marron, fg="white").grid(row=6, column=0, padx=10, pady=5)
        self.subcategoria_var = tk.StringVar()
        self.desplegable_subcategoria = ttk.Combobox(frame, textvariable=self.subcategoria_var)

        # Etiqueta y campo de texto para la descripción
        tk.Label(frame, text="Descripción:", bg=self.color_marron, fg="white").grid(row=7, column=0, padx=10, pady=5)
        self.entrada_descripcion = tk.Text(frame, height=4, width=30, bg=self.color_naranja, fg="black")
        self.entrada_descripcion.grid(row=7, column=1, padx=10, pady=5)

        # Botones para agregar y eliminar libro
        tk.Button(frame, text="Agregar Libro", bg=self.color_naranja, command=self.agregar_libro).grid(row=8, column=0, padx=10, pady=10)
        tk.Button(frame, text="Eliminar Libro", bg=self.color_naranja, command=self.eliminar_libro).grid(row=8, column=1, padx=10, pady=10)

        # Botón Volver
        tk.Button(frame, text="Volver", bg=self.color_naranja, command=self.volver).grid(row=8, column=2, padx=10, pady=10)

        # Cargar libros al inicio
        

    def show(self):
        self.root.deiconify()

    def hide(self):
        self.root.withdraw()

    def actualizar_subcategorias(self, event):
        categoria = self.categoria_var.get()
        subcategorias = []
        
        if categoria == "Novela":
            subcategorias = ["Novela histórica", "Novela contemporánea", "Ciencia ficción"]
        elif categoria == "Salud":
            subcategorias = ["Nutrición", "Ejercicio", "Medicina"]
        elif categoria == "Tecnología":
            subcategorias = ["Inteligencia Artificial", "Redes", "Desarrollo de Software"]
        
        self.desplegable_subcategoria['values'] = subcategorias
        self.subcategoria_var.set('')  # Reiniciar selección de subcategoría
        self.desplegable_subcategoria.grid(row=6, column=1, padx=10, pady=5)

    def validar_editorial(self, editorial):
        if any(char.isdigit() for char in editorial):
            messagebox.showwarning("Campo inválido", "El campo 'Editorial' no puede contener números.")
            return False
        return True

    def agregar_libro(self):
        libro_id = self.entrada_libro_id.get()
        titulo = self.entrada_titulo.get()
        autor = self.entrada_autor.get()
        editorial = self.entrada_editorial.get()
        categoria = self.categoria_var.get()
        subcategoria = self.subcategoria_var.get()
        descripcion = self.entrada_descripcion.get("1.0", tk.END).strip()
        isbn = self.entrada_isbn.get()

        # Validación de campos
        if not (libro_id and titulo and autor and editorial and categoria and subcategoria and descripcion and isbn):
            messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos antes de agregar un libro.")
            return

        # Validar que el campo editorial no contenga números
        if not self.validar_editorial(editorial):
            return

        # Validar que el ISBN y libro_id sean únicos
        for item in self.tabla_libros.get_children():
            values = self.tabla_libros.item(item)['values']
            if values[1] == isbn or values[0] == libro_id:
                messagebox.showwarning("Duplicado", "El ISBN o el Libro ID ya existe. Por favor, ingresa uno único.")
                return

        # Agregar libro a la tabla
        self.tabla_libros.insert("", "end", values=(libro_id, isbn, titulo, categoria, subcategoria, autor, editorial, descripcion))
        messagebox.showinfo("Libro agregado", "El libro se ha agregado exitosamente.")

        # Guardar en el archivo
        self.guardar_libros()

        # Limpiar entradas
        self.limpiar_entradas()

    def eliminar_libro(self):
        selected_item = self.tabla_libros.selection()
        if not selected_item:
            messagebox.showwarning("Selección inválida", "Por favor, selecciona un libro para eliminar.")
            return

        libro_id = self.tabla_libros.item(selected_item)['values'][0]
        confirm = messagebox.askyesno("Confirmar eliminación", f"¿Estás seguro de que deseas eliminar el libro con ID: {libro_id}?")
        if confirm:
            self.tabla_libros.delete(selected_item)
            messagebox.showinfo("Libro eliminado", "El libro se ha eliminado exitosamente.")

            # Guardar cambios en el archivo
            self.guardar_libros()

    def limpiar_entradas(self):
        self.entrada_titulo.delete(0, tk.END)
        self.entrada_autor.delete(0, tk.END)
        self.entrada_editorial.delete(0, tk.END)
        self.entrada_isbn.delete(0, tk.END)
        self.entrada_libro_id.delete(0, tk.END)
        self.subcategoria_var.set('')
        self.categoria_var.set('')
        self.entrada_descripcion.delete("1.0", tk.END)

    def guardar_libros(self):
        with open('libros.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.columnas)  # Escribir encabezados
            for item in self.tabla_libros.get_children():
                writer.writerow(self.tabla_libros.item(item)['values'])

   

    def volver(self):
        # Aquí debes implementar la función para volver a la ventana anterior
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = AltaLibros(root)
    root.mainloop()
