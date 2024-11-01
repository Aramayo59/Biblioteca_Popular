#dash.py

import tkinter as tk

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

class Board:
    def principal():
        try:

            root=Tk()
            root.geometry("1366x798")
            
            imagen="imagen_biblioteca2.jpg"
            img=Image.open(imagen)
            img=img.resize((150,200))
            photo=ImageTk.PhotoImage(img)
            label = tk.Label(root, image=photo)  # Crear un label con la imagen
            label.grid(row=0,column=3,columnspan=4) 
            
            #imagen = ImageTk.PhotoImage(Image.open('imagen_biblioteca2.jpg'))
            #imagen=imagen.resize((100,100))
            #label=Label(image=imagen)
            #label.grid(row=0,column=0)
            
            """image_path = "imagen_biblioteca2.jpg"  # Cambia esto por la ruta de tu imagen
            img = Image.open(image_path)
            img = img.resize((100, 100))  # Redimensionar la imagen para que se ajuste a la grilla
            photo = ImageTk.PhotoImage(img)
            
            for i in range(1):
                for j in range(1):
                    label = tk.Label(root, image=photo)  # Crear un label con la imagen
                    label.grid(row=i, column=j, padx=10, pady=10)  """# Posicionar la imagen en la grilla
            
            group_box=LabelFrame(root,text="Principal", padx=5,pady=5,bg='#ff5001')
            group_box.grid(row=0,column=1,padx=5,pady=5,sticky=W)
            
            
            
            Button(group_box,text="Socios").grid(row=1,column=0,padx=5,pady=5,sticky=W)
            Button(group_box,text="Libros").grid(row=2,column=0,padx=5,pady=5,sticky=W)
            Button(group_box,text="Prestamos").grid(row=3,column=0,padx=5,pady=5,sticky=W)  
            
            root.mainloop()
            
        except ValueError as error:
            print("Error al mostrar la interfaz, error:{}".format(error))    

      
        
    principal()    