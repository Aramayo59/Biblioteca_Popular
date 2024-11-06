

import tkinter as tk
from PIL import Image, ImageTk

# Crear la ventana principal
root = tk.Tk()
root.geometry('1366x798')

root.title("Grilla de imágenes con botones")

# Cargar la imagen
image_path = "imagen_biblioteca2.jpg"  # Cambia esto por la ruta de tu imagen
img = Image.open(image_path)
img = img.resize((100, 100))  # Redimensionar la imagen para que se ajuste a la grilla
photo = ImageTk.PhotoImage(img)

# Crear una grilla de 2x2 con imágenes
'''for i in range(1):
    for j in range(1):
        label = tk.Label(root, image=photo)  # Crear un label con la imagen
        label.grid(row=i, column=j, padx=10, pady=10)  # Posicionar la imagen en la grilla'''


label = tk.Label(root, image=photo)  # Crear un label con la imagen
label.grid()  # Posicionar la imagen en la grilla
# Funciones para los botones
def mostrar_socios():
    print("Botón Socios presionado")

def mostrar_libros():
    print("Botón Libros presionado")

def mostrar_prestamos():
    print("Botón Préstamos presionado")

# Crear los botones y posicionarlos debajo de la grilla
boton_socios = tk.Button(root, text="Socios", command=mostrar_socios)
boton_libros = tk.Button(root, text="Libros", command=mostrar_libros)
boton_prestamos = tk.Button(root, text="Préstamos", command=mostrar_prestamos)

# Ubicar los botones en la grilla, debajo de las imágenes (en la fila 2)
boton_socios.grid(row=2, column=0, padx=10, pady=10)
boton_libros.grid(row=3, column=0, padx=10, pady=10)
boton_prestamos.grid(row=4, column=0, padx=10, pady=10)

# Ejecutar el bucle principal de la ventana
root.mainloop()
