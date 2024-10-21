import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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
    if not (titulo, autor, editorial, categoria, subcategoria, descripcion, isbn):
        messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos antes de agregar un libro.")
        return
    
    tabla_libros.insert("", "end", values=(isbn, titulo, categoria, subcategoria, autor, editorial, descripcion))
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

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestión de Biblioteca")
root.geometry("1366x768")
root.resizable(False, False)

# Colores personalizados
color_azul = "#5277FF"
color_celeste = "#38B6FF"
color_amarillo = "#FFF852"

# Aplicar color de fondo a toda la ventana
root.configure(bg=color_azul)

# Crear un estilo personalizado para la tabla (Treeview)
style = ttk.Style()
style.theme_use('clam')
style.configure("Treeview", background=color_amarillo, fieldbackground=color_amarillo, foreground="black")
style.configure("Treeview.Heading", background=color_amarillo, foreground="black")

# Alternar color de las filas
style.map('Treeview', background=[('selected', color_celeste)])

# Tabla para mostrar los libros
columnas = ("ISBN", "Título", "Categoría", "Subcategoría", "Autor", "Editorial", "Descripción")
tabla_libros = ttk.Treeview(root, columns=columnas, show="headings", style="Treeview")
for col in columnas:
    tabla_libros.heading(col, text=col)
    tabla_libros.column(col, width=100)

# Cambiar color de fondo de la tabla
tabla_libros.tag_configure('oddrow', background=color_amarillo)
tabla_libros.tag_configure('evenrow', background=color_celeste)

tabla_libros.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Marco para los detalles del libro
frame = tk.Frame(root, bg=color_azul)
frame.pack(pady=10)

# Etiquetas y entradas para los detalles del libro
tk.Label(frame, text="Título:", bg=color_azul, fg="white").grid(row=0, column=0, padx=10, pady=5)
entrada_titulo = tk.Entry(frame, bg=color_celeste, fg="black")
entrada_titulo.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Autor:", bg=color_azul, fg="white").grid(row=1, column=0, padx=10, pady=5)
entrada_autor = tk.Entry(frame, bg=color_celeste, fg="black")
entrada_autor.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="Editorial:", bg=color_azul, fg="white").grid(row=2, column=0, padx=10, pady=5)
entrada_editorial = tk.Entry(frame, bg=color_celeste, fg="black")
entrada_editorial.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame, text="ISBN:", bg=color_azul, fg="white").grid(row=3, column=0, padx=10, pady=5)
entrada_isbn = tk.Entry(frame, bg=color_celeste, fg="black")
entrada_isbn.grid(row=3, column=1, padx=10, pady=5)

tk.Label(frame, text="Categoría:", bg=color_azul, fg="white").grid(row=4, column=0, padx=10, pady=5)
categoria_var = tk.StringVar()
desplegable_categoria = ttk.Combobox(frame, textvariable=categoria_var)
desplegable_categoria['values'] = ("Novela", "Salud", "Tecnología")  # Agrega más categorías según sea necesario
desplegable_categoria.grid(row=4, column=1, padx=10, pady=5)

# Dropdown de Subcategoría (se actualizará según la categoría seleccionada)
tk.Label(frame, text="Subcategoría:", bg=color_azul, fg="white").grid(row=5, column=0, padx=10, pady=5)
subcategoria_var = tk.StringVar()
desplegable_subcategoria = ttk.Combobox(frame, textvariable=subcategoria_var)

# Cuando se selecciona una categoría, se actualizan las subcategorías
desplegable_categoria.bind("<<ComboboxSelected>>", actualizar_subcategorias)

# Etiqueta y campo de texto para la descripción
tk.Label(frame, text="Descripción:", bg=color_azul, fg="white").grid(row=6, column=0, padx=10, pady=5)
entrada_descripcion = tk.Text(frame, height=4, width=30, bg=color_celeste, fg="black")
entrada_descripcion.grid(row=6, column=1, padx=10, pady=5)

# Botón para agregar libro
boton_agregar = tk.Button(frame, text="Agregar Libro", bg=color_celeste, command=agregar_libro)
boton_agregar.grid(row=7, column=1, padx=10, pady=10)

# Botón para cerrar
boton_cerrar = tk.Button(root, text="Cerrar", bg=color_amarillo, command=root.quit)
boton_cerrar.pack(pady=10)

# Aplicar estilo a las combobox para que también tengan color de fondo
style.configure("TCombobox", fieldbackground=color_celeste, background=color_celeste)

root.mainloop()
