import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

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
        self.configurar_tabla()

        # Tabla para mostrar los libros
        self.columnas = ("ID", "ISBN", "Título", "Categoría", "Subcategoría", "Autor", "Editorial", "Descripción")
        self.tabla_libros = ttk.Treeview(root, columns=self.columnas, show="headings", style="Treeview")
        self.tabla_libros.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Marco para los detalles del libro
        frame = tk.Frame(root, bg=self.color_marron)
        frame.pack(pady=10)

        # Etiquetas y entradas para los detalles del libro
        self.crear_widgets(frame)

        # Conectar a la base de datos y cargar los libros
        self.conectar_bd()
        self.cargar_libros()

    def configurar_tabla(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", background=self.color_naranja, fieldbackground=self.color_naranja, foreground="black")
        style.configure("Treeview.Heading", background=self.color_marron, foreground="white")
        style.map('Treeview', background=[('selected', self.color_marron)])

    def crear_widgets(self, frame):
        labels = ["Título:", "Autor:", "Editorial:", "ISBN:", "Categoría:", "Subcategoría:", "Descripción:"]
        for i, label in enumerate(labels):
            tk.Label(frame, text=label, bg=self.color_marron, fg="white").grid(row=i, column=0, padx=10, pady=5)

        self.entrada_titulo = tk.Entry(frame, bg=self.color_naranja, fg="black")
        self.entrada_titulo.grid(row=0, column=1, padx=10, pady=5)

        self.entrada_autor = tk.Entry(frame, bg=self.color_naranja, fg="black")
        self.entrada_autor.grid(row=1, column=1, padx=10, pady=5)

        self.entrada_editorial = tk.Entry(frame, bg=self.color_naranja, fg="black")
        self.entrada_editorial.grid(row=2, column=1, padx=10, pady=5)

        self.entrada_isbn = tk.Entry(frame, bg=self.color_naranja, fg="black")
        self.entrada_isbn.grid(row=3, column=1, padx=10, pady=5)

        self.categoria_var = tk.StringVar()
        self.desplegable_categoria = ttk.Combobox(frame, textvariable=self.categoria_var)
        self.desplegable_categoria['values'] = ("Novela", "Salud", "Tecnología")
        self.desplegable_categoria.grid(row=4, column=1, padx=10, pady=5)
        self.desplegable_categoria.bind("<<ComboboxSelected>>", self.actualizar_subcategorias)

        self.subcategoria_var = tk.StringVar()
        self.desplegable_subcategoria = ttk.Combobox(frame, textvariable=self.subcategoria_var)
        self.desplegable_subcategoria.grid(row=5, column=1, padx=10, pady=5)

        self.entrada_descripcion = tk.Text(frame, height=4, width=30, bg=self.color_naranja, fg="black")
        self.entrada_descripcion.grid(row=6, column=1, padx=10, pady=5)

        tk.Button(frame, text="Agregar Libro", bg=self.color_naranja, command=self.agregar_libro).grid(row=7, column=0, padx=10, pady=10)
        tk.Button(frame, text="Eliminar Libro", bg=self.color_naranja, command=self.eliminar_libro).grid(row=7, column=1, padx=10, pady=10)
        tk.Button(frame, text="Volver", bg=self.color_naranja, command=self.volver).grid(row=7, column=2, padx=10, pady=10)

    def conectar_bd(self):
        try:
            self.conexion = mysql.connector.connect(
                user='root',
                password='',
                host='127.0.0.1',
                database='bibliodb',
                port='3306'
            )
            self.cursor = self.conexion.cursor()
        except mysql.connector.Error as err:
            messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {err}")
            self.root.destroy()

    def cargar_libros(self):
        self.tabla_libros.delete(*self.tabla_libros.get_children())  # Limpiar la tabla
        self.cursor.execute("SELECT * FROM libros")
        for fila in self.cursor.fetchall():
            self.tabla_libros.insert("", "end", values=fila)

    def actualizar_subcategorias(self, event):
        categoria = self.categoria_var.get()
        subcategorias = {
            "Novela": ["Novela histórica", "Novela contemporánea", "Ciencia ficción"],
            "Salud": ["Nutrición", "Ejercicio", "Medicina"],
            "Tecnología": ["Inteligencia Artificial", "Redes", "Desarrollo de Software"]
        }.get(categoria, [])
        
        self.desplegable_subcategoria['values'] = subcategorias
        self.subcategoria_var.set('')  # Reiniciar selección de subcategoría

    def obtener_nuevo_id(self):
        self.cursor.execute("SELECT IFNULL(MAX(libro_id), 0) + 1 FROM libros")
        return self.cursor.fetchone()[0]

    def agregar_libro(self):
        try:
            # Obtén los valores de los campos de entrada
            titulo_value = self.entrada_titulo.get()
            isbn_value = self.entrada_isbn.get()
            categoria_value = self.categoria_var.get()
            subcategoria_value = self.subcategoria_var.get()
            autor_value = self.entrada_autor.get()
            editorial_value = self.entrada_editorial.get()
            descripcion_value = self.entrada_descripcion.get("1.0", tk.END).strip()

            # Verificar que los campos requeridos no estén vacíos
            if not titulo_value or not autor_value or not isbn_value or not editorial_value:
                messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos requeridos.")
                return

            # Obtener un nuevo ID para el libro
            id_value = self.obtener_nuevo_id()

            # Inserción en la base de datos
            self.cursor.execute(
                "INSERT INTO libros (libro_id, Titulo, ISBN, Categoria, Subcategoria, Autor, Editorial, Descripcion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (id_value, titulo_value, isbn_value, categoria_value, subcategoria_value, autor_value, editorial_value, descripcion_value)
            )

            self.conexion.commit()  # Confirmar la inserción
            messagebox.showinfo("Éxito", "Libro agregado correctamente.")
            self.cargar_libros()  # Recargar la tabla para mostrar el nuevo libro

            # Limpiar los campos
            self.limpiar_campos()

        except mysql.connector.Error as err:
            messagebox.showerror("Error al agregar libro", f"No se pudo agregar el libro: {err}")

    def limpiar_campos(self):
        self.entrada_titulo.delete(0, tk.END)
        self.entrada_isbn.delete(0, tk.END)
        self.categoria_var.set('')
        self.subcategoria_var.set('')
        self.entrada_autor.delete(0, tk.END)
        self.entrada_editorial.delete(0, tk.END)
        self.entrada_descripcion.delete("1.0", tk.END)

    def eliminar_libro(self):
        selected_item = self.tabla_libros.selection()
        if not selected_item:
            messagebox.showwarning("Selección vacía", "Seleccione un libro para eliminar.")
            return

        libro_id = self.tabla_libros.item(selected_item)['values'][0]
        self.cursor.execute("DELETE FROM libros WHERE libro_id = %s", (libro_id,))

        self.conexion.commit()  # Confirmar la eliminación
        messagebox.showinfo("Éxito", "Libro eliminado correctamente.")
        self.cargar_libros()  # Recargar la tabla

    def volver(self):
        self.root.destroy()

    def __del__(self):
        if hasattr(self, 'conexion'):
            self.conexion.close()  # Asegurarse de cerrar la conexión a la base de datos

if __name__ == "__main__":
    root = tk.Tk()
    app = AltaLibros(root)
    root.mainloop()
