import tkinter as tk
from database_connector import DatabaseConnector
from book_table import BookTable
from book_form import BookForm

class AltaLibros:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Biblioteca")
        self.root.geometry("1366x768")
        self.root.resizable(False, False)
        self.color_naranja = "#ff9933"
        self.color_marron = "#4d2600"
        self.root.configure(bg=self.color_marron)

        self.db = DatabaseConnector()
        if not self.db.conectar():
            self.root.destroy()
            return

        self.tabla = BookTable(root, ("ID", "ISBN", "Título", "Categoría", "Subcategoría", "Autor", "Editorial", "Descripción"), "Treeview")
        self.tabla.configurar_tabla(self.color_naranja, self.color_marron)
        
        self.formulario = BookForm(root, self.color_marron, self.color_naranja, self.agregar_libro, self.eliminar_libro, self.volver)
        self.cargar_libros()

    def cargar_libros(self):
        datos = self.db.ejecutar_consulta("SELECT * FROM libros")
        self.tabla.cargar_datos(datos)

    def agregar_libro(self):
        valores = self.formulario.obtener_valores()
        if not valores["Título:"] or not valores["Autor:"] or not valores["ISBN:"]:
            messagebox.showwarning("Campos vacíos", "Complete todos los campos requeridos.")
            return

        nuevo_id = self.db.ejecutar_consulta("SELECT IFNULL(MAX(libro_id), 0) + 1 FROM libros")[0][0]
        self.db.ejecutar_cambio(
            "INSERT INTO libros (libro_id, Titulo, ISBN, Categoria, Subcategoria, Autor, Editorial, Descripcion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (nuevo_id, valores["Título:"], valores["ISBN:"], valores["Categoría:"], valores["Subcategoría:"], valores["Autor:"], valores["Editorial:"], valores["Descripción:"])
        )
        messagebox.showinfo("Éxito", "Libro agregado correctamente.")
        self.cargar_libros()
        self.formulario.limpiar_campos()

    def eliminar_libro(self):
        libro_id = self.tabla.obtener_seleccion()
        if not libro_id:
            messagebox.showwarning("Selección vacía", "Seleccione un libro para eliminar.")
            return
        self.db.ejecutar_cambio("DELETE FROM libros WHERE libro_id = %s", (libro_id,))
        messagebox.showinfo("Éxito", "Libro eliminado correctamente.")
        self.cargar_libros()

    def volver(self):
        self.root.destroy()

    def __del__(self):
        self.db.cerrar()

if __name__ == "__main__":
    root = tk.Tk()
    app = AltaLibros(root)
    root.mainloop()
