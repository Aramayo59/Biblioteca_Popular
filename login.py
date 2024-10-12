from tkinter import *


#wb = Workbook()
#ws = wb.active
#ws.append(["Nombre", "Edad","Email", "Teléfono", "Dirección"])
#wb.save('datos.xlsx')

ventana_login = Tk()
ventana_login.title("Formulario de entrada de Datos")
#ventana_login.config(bg='#4B6587')
ventana_login.geometry("400x300")
ventana_login.resizable(0,0)

frame0=Frame(ventana_login, width=300, height=400,bg='#4B6587')
frame0.grid()



label_style = {"bg": "#4B6587", "fg": "white"}
entry_style = {"bg": "#D3D3D3", "fg": "black"} 

label_apellido = Label(frame0,text="Apellido", **label_style)
label_apellido.grid(row=0,column=0,padx=10,pady=5,)
entry_apellido = Entry(frame0,**entry_style)
entry_apellido.grid(row=0,column=1,padx=10,pady=5)

label_nombre = Label(frame0,text="Nombre", **label_style)
label_nombre.grid(row=1,column=0,padx=10,pady=5)
entry_nombre = Entry(frame0,**entry_style)
entry_nombre.grid(row=1,column=1,padx=10,pady=5)

label_edad = Label(frame0,text="Edad", **label_style)
label_edad.grid(row=2,column=0,padx=10,pady=5)
entry_edad = Entry(frame0,**entry_style)
entry_edad.grid(row=2,column=1,padx=10,pady=5)

label_email = Label(frame0,text="Email", **label_style)
label_email.grid(row=3,column=0,padx=10,pady=5)
entry_email = Entry(frame0,**entry_style)
entry_email.grid(row=3,column=1,padx=10,pady=5)

label_telefono = Label(frame0,text="Teléfono", **label_style)
label_telefono.grid(row=4,column=0,padx=10,pady=5)
entry_telefono = Entry(frame0,**entry_style)
entry_telefono.grid(row=4,column=1,padx=10,pady=5)

label_direccion = Label(frame0,text="Dirección", **label_style)
label_direccion.grid(row=5,column=0,padx=10,pady=5)
entry_direccion = Entry(frame0,**entry_style)
entry_direccion.grid(row=5,column=1,padx=10,pady=5)

boton_guardar = Button(frame0, text="Guardar",bg="#6D8299",fg="white")
boton_guardar.grid(row=6,column=0,columnspan=1,padx=10,pady=5)

boton_modificar = Button(frame0, text="Modificar",bg="#6D8299",fg="white")
boton_modificar.grid(row=6,column=1,columnspan=1,padx=10,pady=5)

boton_borrar = Button(frame0, text="Borrar",bg="#6D8299",fg="white")
boton_borrar.grid(row=6,column=2,columnspan=1,padx=10,pady=5)

ventana_login.mainloop()