#gestion_socio.py

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from Modificacion_socio import *
from ConexionBD import *

class Formulario_socios:
    
 global base
 base=None
    
 global text_ID
 text_ID=None
    
 global text_apellido
 text_apellido=None
    
 global text_nombre
 text_nombre=None
    
 global text_dni
 text_dni=None
    
 global text_domicilio
 text_domicilio=None
    
 global text_ultimop
 text_ultimop=None
    
 global text_telefono
 text_telefono=None
    
 global combo
 combo=None
    
 global group_box
 group_box=None
    
 global tree 
 tree=None
    
def Formulario():
        
        
  global base
  global text_ID
  global text_nombre
  global text_apellido
  global text_dni
  global text_domicilio
  global text_ultimop
  global text_telefono
  global combo
  global group_box
  global tree
        
        
  try: 
   base=Tk()
            
   base.geometry("1366x798")
   base.config(bg='#ff9933')
   base.title("Gestión Socio")
   
   group_box=LabelFrame(base,text="Alta de Socio", padx=5,pady=5,bg='#ff9933')
            #group_box.config("1366x798")
   group_box.grid(row=1,column=0,padx=5,pady=5,sticky=W)
            
   label_ID=Label(group_box,text=("ID:")).grid(row=0,column=0,padx=5,pady=5,sticky="w")
   text_ID=Entry(group_box)
   #text_ID.grid(row=0,column=1,padx=5,pady=5)
            
   label_apellido=Label(group_box,text=("Nombre:")).grid(row=1,column=0,padx=5,pady=5,sticky="w")
   text_apellido=Entry(group_box)
   text_apellido.grid(row=1,column=1,padx=5,pady=5)
            
   label_nombre=Label(group_box,text=("Apellido:")).grid(row=2,column=0,padx=5,pady=5,sticky="w")
   text_nombre=Entry(group_box)
   text_nombre.grid(row=2,column=1,padx=5,pady=5)
            
   label_dni=Label(group_box,text=("DNI:")).grid(row=3,column=0,padx=5,pady=5,sticky="w")
   text_dni=Entry(group_box)
   text_dni.grid(row=3,column=1,padx=5,pady=5)
    
   label_domicilio=Label(group_box,text=("Domicilio:")).grid(row=4,column=0,padx=5,pady=5,sticky="w")
   text_domicilio=Entry(group_box)
   text_domicilio.grid(row=4,column=1,padx=5,pady=5)
            
            #label_pago=Label(group_box,text=("Pago:")).grid(row=5,column=0,padx=5,pady=5,sticky="w")
            #text_pago=Entry(group_box).grid(row=5,column=1,padx=5,pady=5)
            
   label_ultimop=Label(group_box,text=("Última Fecha de Pago:")).grid(row=6,column=0,padx=5,pady=5,sticky="w")
   text_ultimop=Entry(group_box)
   text_ultimop.grid(row=6,column=1,padx=5,pady=5)
            
   label_telefono=Label(group_box,text=("Teléfono:")).grid(row=7,column=0,padx=5,pady=5,sticky="w")
   text_telefono=Entry(group_box)
   text_telefono.grid(row=7,column=1,padx=5,pady=5)
            
   label_sexo=Label(group_box,text=("Sexo:")).grid(row=8,column=0,padx=5,pady=5,sticky="w")
   seleccion_sexo=tk.StringVar()
   combo=ttk.Combobox(group_box,values=["Masculino", "Femenino"],textvariable=seleccion_sexo)
   combo.grid(row=8,column=1,padx=5,pady=5) 
   seleccion_sexo.set("Masculino")
            
   label_estado=Label(group_box,text=("Estado:")).grid(row=9,column=0,padx=5,pady=5,sticky="w")
   seleccion_estado=tk.StringVar()
   combo=ttk.Combobox(group_box,values=["Activo", "Inactivo"],textvariable=seleccion_estado)
   combo.grid(row=9,column=1,padx=5,pady=5) 
   seleccion_estado.set("Inactivo")
            
   Button(group_box,text="Guardar",command=guardar_registros,bg='#4d2600',foreground='white').grid(row=10,column=0,padx=5,pady=5)
            
   group_box=LabelFrame(base,text="Lista de Socios",padx=5,pady=5)
   group_box.grid(row=0,column=0,padx=5,pady=5)
            
            #Treeview de la Grilla
            
   tree=ttk.Treeview(group_box,columns=("ID","Apellido","Nombre","DNI","Domicilio","Teléfono","Fecha de Pago","Sexo"),show="headings")
   tree.column("#1",anchor=CENTER)
   tree.heading("#1",text="ID")
   tree.column("#2",anchor=CENTER)
   tree.heading("#2",text="Apellido")
   tree.column("#3",anchor=CENTER)
   tree.heading("#3",text="Nombre")
   tree.column("#4",anchor=CENTER)
   tree.heading("#4",text="DNI")
   tree.column("#5",anchor=CENTER)
   tree.heading("#5",text="Domicilio")
   tree.column("#6",anchor=CENTER)
   tree.heading("#6",text="Última Fecha de Pago")
   tree.column("#7",anchor=CENTER)
   tree.heading("#7",text="Teléfono")
   tree.column("#8",anchor=CENTER)
   tree.heading("#8",text="Sexo")
            
            #Agregar datos a la grilla y mostrarlos
            
   for row in Socio.mostrar_socios(): 
       tree.insert("","end",values=row)
   tree.bind("<<TreeviewSelect>>",seleccionregistro)
   
   # Crear scrollbars
   scroll_y = Scrollbar(group_box, orient="vertical", command=tree.yview)
   scroll_x = Scrollbar(group_box, orient="horizontal", command=tree.xview)
   scroll_x.grid(row=2,column=2)
   tree.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

# Posicionar Treeview y Scrollbars usando grid
   tree.grid(row=0, column=0)
   scroll_y.grid(row=0, column=10)
   scroll_x.grid(row=2, column=0)
   
   
   
   
   tree.grid()
                       
   group_box=LabelFrame(base)
   group_box.config(bg='#4d2600')
   group_box.grid(row=1,column=0)
   Button(group_box,text="Modificar",command=modificar_registros,bg='#4d2600',foreground='white').grid(row=0,column=0,padx=5,pady=5)
   Button(group_box,text="Volver",bg='#4d2600',foreground='white').grid(row=0,column=1,padx=5,pady=5)
 
            
            
            
   base.mainloop()
        
        
  except ValueError as error:
     print("Error al mostrar la interfaz, error: {} ".format(error)) 
 
def guardar_registros():
        
  global text_apellido,text_nombre,text_dni,text_domicilio,text_ultimop,text_telefono,combo,group_box
        
  try:
      
     if text_apellido is None or text_nombre is None or text_dni is None or text_domicilio is None or text_ultimop is None or text_telefono is None or combo is None:
        print("Los widgets no estan inicializados") 
        return
            
     apellido=text_apellido.get()
     nombre=text_nombre.get()
     dni=text_dni.get()
     domicilio=text_domicilio.get()
     ultimop=text_ultimop.get()
     telefono=text_telefono.get()
     sexo=combo.get()
            
     Socio.Ingresar_Socios(apellido,nombre,dni,domicilio,ultimop,telefono,sexo)
     messagebox.showinfo("Informacion","Los datos fueron guardados")
                
     actualizarTreeView()
            
     text_apellido.delete(0,END)
     text_nombre.delete(0,END)
     text_dni.delete(0,END)
     text_domicilio.delete(0,END)
     text_ultimop.delete(0,END)
     text_telefono.delete(0,END)
     combo.delete(0,END)
            
  except ValueError as error:
      print("Error al ingresar los datos{}".format(error))
                
def actualizarTreeView():
     
    global tree
    try:
        tree.delete(*tree.get_children())
        datos =Socio.mostrar_socios()
        for row in Socio.mostrar_socios():
         tree.insert("","end",values=row)
             
    except ValueError as error:
        print("Error al actualizar tabla{}".format(error))
            
def seleccionregistro(event):
  try:
      itemselecionado=tree.focus()
      if itemselecionado:
       values=tree.item(itemselecionado)['values']
       text_ID.delete(0,END)
       text_ID.insert(0,values[0])
       text_apellido.delete(0,END)
       text_apellido.insert(0,values[1])
       text_nombre.delete(0,END)
       text_nombre.insert(0,values[2])
       text_dni.delete(0,END)
       text_dni.insert(0,values[3])
       text_domicilio.delete(0,END)
       text_domicilio.insert(0,values[4])
       text_ultimop.delete(0,END)
       text_ultimop.insert(0,values[5])
       text_telefono.delete(0,END)
       text_telefono.insert(0,values[6])
       combo.set(0,values[7])
            
  except ValueError as error: 
      print("Error al seleccionar registro{}".format(error))      
            


def modificar_registros():
  global text_apellido,text_nombre,text_dni,text_domicilio,text_ultimop,text_telefono,combo,group_box
        
  try:
      if text_ID is None or text_apellido is None or text_nombre is None or text_dni is None or text_domicilio is None or text_ultimop is None or text_telefono is None or combo is None:
          print("Los widgets no estan inicializados") 
          return
      
      ID=text_ID.get()      
      apellido=text_apellido.get()
      nombre=text_nombre.get()
      dni=text_dni.get()
      domicilio=text_domicilio.get()
      ultimop=text_ultimop.get()
      telefono=text_telefono.get()
      sexo=combo.get()
            
      Socio.Modificar_Socios(ID,apellido,nombre,dni,domicilio,ultimop,telefono,sexo)
      messagebox.showinfo("Informacion","Los datos fueron actualizados")
                
      actualizarTreeView()
      
      text_ID.delete(0,END)      
      text_apellido.delete(0,END)
      text_nombre.delete(0,END)
      text_dni.delete(0,END)
      text_domicilio.delete(0,END)
      text_ultimop.delete(0,END)
      text_telefono.delete(0,END)
      combo.delete(0,END)
            
  except ValueError as error:
                print("Error al ingresar los datos{}".format(error))


      
              
Formulario()         
