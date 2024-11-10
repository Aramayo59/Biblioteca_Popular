import tkinter as tk
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from Mostrar import *
from ConexionBDBiblioteca import *
from Mostrar import *
from ModificarPrestamo import modificar_prestamos
from RegistroPrestamos import prestamos_interface

def Formulario_prestamos():
        try: 
                ventana = Tk()
                ventana.geometry ("1230x300")
                ventana.title("Gestion De Prestamos")
                ventana.config (bg="#d35c25")

                marco_grilla= LabelFrame(ventana, text= "Prestamos Registrados", padx=5, pady=5, bg="#d9b38c")
                marco_grilla.grid(row=0, column=0,padx=5,pady=5)
            
                marco_grilla_button = LabelFrame(ventana,padx=5, pady=5, bg="#d9b38c" )
                marco_grilla_button.grid(row = 1,column=0,padx=5,pady=5)
           
                
                grilla_prestamos= ttk.Treeview(marco_grilla,columns=( "Nombre", "apellido","Dni","Isbn","Fecha devolucion", "Estado" ),show='headings', height=5,)
                
                grilla_prestamos.column("#1", anchor=CENTER)
                grilla_prestamos.heading("#1",text="Nombre")
            
                grilla_prestamos.column("#2", anchor=CENTER)
                grilla_prestamos.heading("#2",text="Apellido")

                grilla_prestamos.column("#3", anchor=CENTER)
                grilla_prestamos.heading("# 3", text="DNI")
            
                grilla_prestamos.column("#4", anchor=CENTER)
                grilla_prestamos.heading("# 4", text="ISBN")
            
                grilla_prestamos.column("#5", anchor=CENTER)
                grilla_prestamos.heading("# 5", text="Fecha de devolucion")
            
                grilla_prestamos.column("#6", anchor=CENTER)
                grilla_prestamos.heading("# 6", text="Estado")
           
                dato_prestamo = mostrarPrestamos()
                if dato_prestamo:
                        for row in dato_prestamo:
                                grilla_prestamos.insert("", "end", values=row)
           
                grilla_prestamos.pack()
                def cargar_datos():
                # Limpiar el Treeview antes de la actualización
                        for i in grilla_prestamos.get_children():
                                grilla_prestamos.delete(i)
                        
                        
                        dato_prestamo = mostrarPrestamos()
                        if dato_prestamo:
                                for row in dato_prestamo:
                                 grilla_prestamos.insert("", "end", values=row)

                def actualizar_datos():
                        cargar_datos()  
                        ventana.after(3000, actualizar_datos)  
                def eliminar_prestamo():
                        selected_item = grilla_prestamos.focus()  
                        if not selected_item:
                                messagebox.showwarning("Advertencia", "Seleccione un préstamo para eliminar.")
                                return

                        # Obtener los valores de la fila seleccionada
                        datos_fila = grilla_prestamos.item(selected_item, "values")
                        isbn = f"{datos_fila[3]}"
                        dni = f"{datos_fila[2]}"

                        # Confirmación antes de eliminar
                        if messagebox.askyesno("Confirmación", f"¿Estás seguro de eliminar el préstamo con el dni {dni}?"):
                                conexion = Cconexion.conexion()
                                cursor = conexion.cursor()

                        try:
                                # Consulta para obtener el ID del préstamo basado en el DNI
                                sql = """
                                        SELECT
                                        p.id_libros
                                        FROM 
                                        prestamos p
                                        JOIN 
                                        libros l ON p.id_libros = l.id_libros
                                        WHERE 
                                        l.isbn = %s;"""
                                cursor.execute(sql, (isbn,))
                                id_resultado = cursor.fetchone()  # Devuelve una fila
                                cursor.fetchall()
                                if id_resultado:
                                        libro_id = id_resultado[0]  # Obtener el ID del préstamo
                                        sql = "UPDATE prestamos  SET estado_prestamo = 'inactivo'  WHERE id_libros = %s"
                                        cursor.execute(sql, (libro_id,))
                                        conexion.commit()  # Confirma los cambios
                                        messagebox.showinfo("Éxito", "Préstamo eliminado con éxito.")
                                        grilla_prestamos.delete(selected_item)  # Eliminar la fila del Treeview
                                else:
                                        messagebox.showwarning("Advertencia", "No se encontró el préstamo.")
                        except mysql.connector.Error as err:
                                print(f"Error: {err}")
                        finally:
                                cursor.close()  
                                conexion.close()
                def abrir_modificar():
                        selected_item = grilla_prestamos.focus()  
                        if not selected_item:
                                messagebox.showwarning("Advertencia", "Seleccione un préstamo para modificar.")
                                return
                        
                        datos_fila = grilla_prestamos.item(selected_item, "values")
                        isbn = f"{datos_fila[3]}"
                        fecha_devolucion = f"{datos_fila[4]}"
                        
                        modificar_prestamos( isbn,fecha_devolucion)  
                actualizar_datos()
        except ValueError as error:
            print("Error al mostrar la interfaz, error{}".format(error))
        boton_modificar = tk.Button(
        marco_grilla_button, text="Modificar Préstamo",
        font=("Arial", 12, "bold"), command=abrir_modificar)
        boton_modificar.grid(row= 0, column= 0, pady=10)

        boton_modificar = tk.Button(
        marco_grilla_button, text="Nuevo Prestamo",
        font=("Arial", 12, "bold"), command=prestamos_interface)
        boton_modificar.grid(row= 0, column= 1,pady=10)

        boton_modificar = tk.Button(
        marco_grilla_button, text="Eliminar prestamo",
        font=("Arial", 12, "bold"), command=eliminar_prestamo)
        boton_modificar.grid(row= 0, column= 2,pady=10, )
        
        def eliminar_prestamo():
                selected_item = grilla_prestamos.focus()  
                if not selected_item:
                        messagebox.showwarning("Advertencia", "Seleccione un préstamo para modificar.")
                        return
                datos_fila = grilla_prestamos.item(selected_item, "values")
                isbn = f"{datos_fila[3]}"

                conexion = Cconexion.conexion()
                cursor = conexion.cursor()

                try:
       
                        sql = "SELECT p.id_prestamos FROM prestamos p JOIN libros l ON p.id_libros = l.id_libros WHERE l.isbn = %s;"
                        cursor.execute(sql, (isbn,))
                        id_prestamo = cursor.fetchone()              
                        id_prestamo= cursor.fetchone()  
                        sql = "UPDATE prestamos SET estado = 'inactivo' WHERE id_prestamos = %s"
                        cursor.execute(sql, (id_prestamo,))
                        cursor.close()  
                        
                except mysql.connector.Error as err:
                        print(f"Error: {err}")
                finally:
                        cursor.close()
                        conexion.close()

                
        ventana.mainloop()
Formulario_prestamos()   