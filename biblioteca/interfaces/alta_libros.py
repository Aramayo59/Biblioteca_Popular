import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import os

# Función para actualizar las subcategorías basadas en la categoría seleccionada
def actualizar_subcategorias(event):
    categoria = categoria_var.get()
    subcategorias = []
    
    if categoria == "Novela":
        subcategorias = ["Novela histórica", "Novela contemporánea", "Ciencia ficción"]
    elif categoria == "Salud":
        subcategorias = ["Nutrición", "Ejercicio", "Medicina"]
    elif categoria == "Tecnología":
        subcategorias = ["Inteligencia Artificial", "Redes", "Desarrollo de Software"]
    
    desplegable_subcategoria['values'] = subcategorias
    subcategoria_var.set('')  # Reiniciar selección de subcategoría
    desplegable_subcategoria.grid(row=5, column=1, padx=10, pady=5)  # Mostrar subcategoría después de seleccionar una categoría

# Función para validar que el campo Editorial no contenga números
def validar_editorial(editorial):
    if any(char.isdigit() for char in editorial):
        messagebox.showwarning("Campo inválido", "El campo 'Editorial' no puede contener números.")
        return False
    return True

# Función para agregar un libro a la tabla
def agregar_libro():
    titulo = entrada_titulo.get()
    autor = entrada_autor.get()
    editorial = entrada_editorial.get()  # Obtener el valor de la editorial
    categoria = categoria_var.get()
    subcategoria = subcategoria_var.get()
    descripcion = entrada_descripcion.get("1.0", tk.END).strip()  # Obtener texto completo de la descripción
    isbn = entrada_isbn.get()

    # Validación de campos
    if not (titulo and autor and editorial and categoria and subcategoria and descripcion and isbn):
        messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos antes de agregar un libro.")
        return

    # Validar que el campo editorial no contenga números
    if not validar_editorial(editorial):
        return

    # Validar que el ISBN sea único
    for item in tabla_libros.get_children():
        if tabla_libros.item(item)['values'][0] == isbn:
            messagebox.showwarning("ISBN duplicado", "El ISBN ya existe. Por favor, ingresa uno único.")
            return

    # Agregar libro a la tabla
    tabla_libros.insert("", "end", values=(isbn, titulo, categoria, subcategoria, autor, editorial, descripcion))
    
    # Guardar libro en un archivo JSON
    guardar_libros()

    limpiar_campos()

# Función para limpiar los campos de entrada
def limpiar_campos():
    entrada_titulo.delete(0, tk.END)
    entrada_autor.delete(0, tk.END)
    entrada_editorial.delete(0, tk.END)  # Limpiar el campo de editorial
    entrada_isbn.delete(0, tk.END)
    entrada_descripcion.delete("1.0", tk.END)
    categoria_var.set('')
    subcategoria_var.set('')
    desplegable_subcategoria.grid_forget()  # Ocultar el campo de subcategoría hasta que se seleccione una categoría

# Función para eliminar un libro seleccionado de la tabla
def eliminar_libro():
    seleccionado = tabla_libros.selection()
    if seleccionado:
        confirmacion = messagebox.askyesno("Eliminar libro", "¿Estás seguro de que deseas eliminar el libro seleccionado?")
        if confirmacion:
            for item in seleccionado:
                tabla_libros.delete(item)
            # Guardar cambios después de eliminar
            guardar_libros()
    else:
        messagebox.showwarning("Selección vacía", "Por favor, selecciona un libro para eliminar.")

# Función para guardar los libros en un archivo JSON
def guardar_libros():
    libros = []
    for item in tabla_libros.get_children():
        libros.append(tabla_libros.item(item)['values'])
    
    with open('libros.json', 'w') as f:
        json.dump(libros, f)

# Función para cargar los libros desde el archivo JSON
def cargar_libros():
    if os.path.exists('libros.json'):
        with open('libros.json', 'r') as f:
            libros = json.load(f)
            for libro in libros:
                tabla_libros.insert("", "end", values=libro)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestión de Biblioteca")
root.geometry("1366x768")
root.resizable(False, False)

# Colores personalizados
color_pastel = "#d9b38c"  # Color pastel
color_marron = "#231c00"  # Marrón
color_naranja = "#ff5100"  # Naranja

# Aplicar color de fondo a toda la ventana
root.configure(bg=color_pastel)

# Crear un estilo personalizado para la tabla (Treeview)
style = ttk.Style()
style.theme_use('clam')
style.configure("Treeview", background=color_naranja, fieldbackground=color_naranja, foreground="black")
style.configure("Treeview.Heading", background=color_naranja, foreground="black")

# Alternar color de las filas
style.map('Treeview', background=[('selected', color_marron)])

# Tabla para mostrar los libros
columnas = ("ISBN", "Título", "Categoría", "Subcategoría", "Autor", "Editorial", "Descripción")
tabla_libros = ttk.Treeview(root, columns=columnas, show="headings", style="Treeview")
for col in columnas:
    tabla_libros.heading(col, text=col)
    tabla_libros.column(col, width=100)

tabla_libros.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Marco para los detalles del libro
frame = tk.Frame(root, bg=color_pastel)
frame.pack(pady=10)

# Etiquetas y entradas para los detalles del libro
tk.Label(frame, text="Título:", bg=color_pastel, fg="black").grid(row=0, column=0, padx=10, pady=5)
entrada_titulo = tk.Entry(frame, bg=color_naranja, fg="black")
entrada_titulo.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Autor:", bg=color_pastel, fg="black").grid(row=1, column=0, padx=10, pady=5)
entrada_autor = tk.Entry(frame, bg=color_naranja, fg="black")
entrada_autor.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="Editorial:", bg=color_pastel, fg="black").grid(row=2, column=0, padx=10, pady=5)
entrada_editorial = tk.Entry(frame, bg=color_naranja, fg="black")
entrada_editorial.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame, text="ISBN:", bg=color_pastel, fg="black").grid(row=3, column=0, padx=10, pady=5)
entrada_isbn = tk.Entry(frame, bg=color_naranja, fg="black")
entrada_isbn.grid(row=3, column=1, padx=10, pady=5)

tk.Label(frame, text="Categoría:", bg=color_pastel, fg="black").grid(row=4, column=0, padx=10, pady=5)
categoria_var = tk.StringVar()
desplegable_categoria = ttk.Combobox(frame, textvariable=categoria_var)
desplegable_categoria['values'] = ("Novela", "Salud", "Tecnología")  # Agrega más categorías según sea necesario
desplegable_categoria.grid(row=4, column=1, padx=10, pady=5)

# Dropdown de Subcategoría (se actualizará según la categoría seleccionada)
tk.Label(frame, text="Subcategoría:", bg=color_pastel, fg="black").grid(row=5, column=0, padx=10, pady=5)
subcategoria_var = tk.StringVar()
desplegable_subcategoria = ttk.Combobox(frame, textvariable=subcategoria_var)

# Cuando se selecciona una categoría, se actualizan las subcategorías
desplegable_categoria.bind("<<ComboboxSelected>>", actualizar_subcategorias)

# Etiqueta y campo de texto para la descripción
tk.Label(frame, text="Descripción:", bg=color_pastel, fg="black").grid(row=6, column=0, padx=10, pady=5)
entrada_descripcion = tk.Text(frame, height=4, width=30, bg=color_naranja, fg="black")
entrada_descripcion.grid(row=6, column=1, padx=10, pady=5)

# Botón para agregar libro
boton_agregar = tk.Button(frame, text="Agregar Libro", bg=color_naranja, command=agregar_libro)
boton_agregar.grid(row=7, column=0, padx=10, pady=10)

# Botón para eliminar libro
boton_eliminar = tk.Button(frame, text="Eliminar Libro", bg=color_naranja, command=eliminar_libro)
boton_eliminar.grid(row=7, column=1, padx=10, pady=10)


cargar_libros()

root.mainloop()
