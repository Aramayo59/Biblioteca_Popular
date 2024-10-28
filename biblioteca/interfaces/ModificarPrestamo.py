import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry  # Importamos DateEntry para el calendario
import mysql.connector  # Asegúrate de que tienes esta biblioteca
from ConexionBDBiblioteca import *  # Importa la función de conexión a la BD
from ValidacionesPrestamos import *  

def modificar_prestamos(nombreyapellido, dni, isbn):

    ventana_prestamos = tk.Tk()
    ventana_prestamos.title("Nuevo Préstamo")
    ventana_prestamos.geometry("350x700+500+70")
    ventana_prestamos.configure(bg="#ff5100")  

    marco_titulo = tk.Frame(ventana_prestamos, bg="#231c00", height=80)
    marco_titulo.pack(fill="x")

        
    tk.Label(marco_titulo, text="Modificar", font=("Arial", 18, "bold"), fg="white", bg="#231c00").place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    tk.Label(marco_titulo, text="Prestamo", font=("Arial", 16, "bold"), fg="white", bg="#d9b38c").place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    def salir():
        resp = messagebox.askquestion("Salir", "¿Desea Cancelar?")
        if resp == "yes":
                ventana_prestamos.destroy()
        
    def buscar_socio():
            dni_busqueda = dni_entry.get().strip()
            if not validar_dni(dni_busqueda):
                return

            try:
                    conexion = Cconexion.conexion()
                    cursor = conexion.cursor()

                    
                    sql =  ("SELECT Nombre, Apellido FROM socios WHERE DNI = %s")
                    cursor.execute(sql,(dni_busqueda,))
                    
                    resultado = cursor.fetchone()

                    if resultado:
                        nombre_completo_box.delete(0, tk.END)
                        nombre_completo = resultado
                        nombre_completo_box['values'] = [nombre_completo]  
                        nombre_completo_box.set(nombre_completo)
                    else:
                        messagebox.showinfo("Buscar", f"No se encontró ningún socio con el DNI: {dni_busqueda}")

                    cursor.close()
                    

            except mysql.connector.Error as err:
                    messagebox.showerror("Error", f"Error en la búsqueda: {err}")

        
    def buscar_libros():
            isbn = isbn_entry.get().strip()  
            if not validar_isbn(isbn):
                return
            try:
                conexion = Cconexion.conexion()
                cursor = conexion.cursor()
                
                sql = ("SELECT titulo FROM libros WHERE isbn = %s")
                cursor.execute(sql,(isbn,))
                resultado = cursor.fetchone()

                if resultado:
                    
                    messagebox.showinfo("Buscar", f"Libro encontrado: {resultado}")
                else:
                    
                    messagebox.showinfo("Buscar", f"No se encontró ningún libro con el título: {isbn}")

                
                cursor.close()
                conexion.close()

            except mysql.connector.Error as err:

                messagebox.showerror("Error", f"Error en la búsqueda de libros: {err}")

        
    def ingresar_prestamo_modificado():
            

            socio = nombre_completo_box.get().strip()
            dni = dni_entry.get().strip()
            isbn = isbn_entry.get().strip()
            fecha_prestamo = devolucion_entry1.get_date()
            fecha_devolucion = devolucion_entry2.get_date()
            
            
            if socio and dni and isbn and fecha_prestamo and fecha_devolucion:
                try:
                    conexion = Cconexion.conexion()
                    cursor = conexion.cursor()
                    
                    cursor.execute("SELECT id_socios FROM socios WHERE DNI = %s",(dni,))
                    id_socios = cursor.fetchone()   
                    if not id_socios:
                        messagebox.showerror("Error", f"No se encontró un socio con el DNI: {dni}")
                        return  
                                     
                    if id_socios:
                       
                        cursor.execute("SELECT id_libros FROM libros WHERE isbn = %s", (isbn,))
                        id_libro = cursor.fetchone()
                        if not id_libro:
                            messagebox.showerror("Error", f"No se encontró un libro con el ISBN: {isbn}")
                            return
                        id_libro = id_libro[0]
                        if id_libro:
                            
                            
                            sql = """
                                    UPDATE prestamos 
                                    SET id_socios = %s, isbn = %s, fecha_prestamo = %s, fecha_devolucion = %s
                                    , id_libro = %s 
                                    WHERE dni = %s;
                                """
                            valores = (id_socios, isbn, fecha_prestamo, fecha_devolucion, dni)
                            
                            # Ejecutar la consulta
                            cursor.execute(sql, valores)
                            limpiar_campos()
                            
                            messagebox.showinfo("Éxito", "El préstamo ha sido registrado exitosamente.")
                        else:
                            messagebox.showwarning("Error", "No se encontró el libro.")
                    else:
                        messagebox.showwarning("Error", "No se encontró el prestamo asociado")

                    conexion.close()
                        
                    

                except mysql.connector.Error as err:
                    messagebox.showerror("Error", f"Error al registrar el préstamo: {err}")
            else:
                messagebox.showwarning("Advertencia", "Por favor complete todos los campos.")
        
    tk.Label(ventana_prestamos, text="DNI", font=("Arial", 12, "bold"), bg="#ff5100", fg="white").pack(pady=10)
    dni_entry = tk.Entry(ventana_prestamos, font=("Arial", 12), width=25)
    dni_entry.insert(0, dni)
    dni_entry.pack()
       

    tk.Button(ventana_prestamos, text="Buscar Socio", font=("Arial", 10, "bold"), bg="#d9b38c", command=buscar_socio).pack(pady=10)
        
    tk.Label(ventana_prestamos, text="Nombre completo", font=("Arial", 12, "bold"), bg="#ff5100", fg="white").pack(pady=10)
    nombre_completo_box = ttk.Combobox(ventana_prestamos, font=("Arial", 12), width=25, state="readonly")
    nombre_completo_box.insert(0, nombreyapellido)
    nombre_completo_box.pack()
   
    
        

    tk.Label(ventana_prestamos, text="Isbn del libro", font=("Arial", 12, "bold"), bg="#ff5100", fg="white").pack(pady=10)
    isbn_entry = tk.Entry(ventana_prestamos, font=("Arial", 12), width=25)
    isbn_entry.insert(0, isbn)
    isbn_entry.pack()
    

    tk.Button(ventana_prestamos, text="Buscar Libro", font=("Arial", 10, "bold"), bg="#d9b38c", command=buscar_libros).pack(pady=10)

    tk.Label(ventana_prestamos, text="Fecha Préstamo", font=("Arial", 12, "bold"), bg="#ff5100", fg="white").pack(pady=10)
    fecha_hoy1 = datetime.now()
    devolucion_entry1 = DateEntry(ventana_prestamos, font=("Arial", 12), width=23, background="lightgreen", foreground="black", borderwidth=2,locale="es_Es", date_pattern='dd/MM/yyyy', mindate=fecha_hoy1, state="readonly")
    devolucion_entry1.pack(pady=5)
    
    tk.Label(ventana_prestamos, text="Fecha Devolución", font=("Arial", 12, "bold"), bg="#ff5100", fg="white").pack(pady=10)
    fecha_hoy2 = datetime.now()

    def limpiar_campos():
        dni_entry.delete(0, tk.END)  
        nombre_completo_box.set("")  
        isbn_entry.delete(0, tk.END) 
        devolucion_entry1.set_date(datetime.now())  
        devolucion_entry2.set_date(datetime.now())

    devolucion_entry2 = DateEntry(ventana_prestamos, font=("Arial", 12), width=23, background="lightgreen", foreground="black", borderwidth=2, locale="es_Es",  date_pattern='dd/MM/yyyy', mindate=fecha_hoy2, state="readonly")
    devolucion_entry2.pack(pady=5)

    # Botón para registrar el préstamo
    tk.Button(ventana_prestamos, text="Registrar", font=("Arial", 12, "bold"), bg="#d9b38c", fg="black", command=ingresar_prestamo_modificado).pack(pady=20)
    tk.Button(ventana_prestamos, text="Cancelar", font= ("Arial",12,"bold"),bg="#d9b38c", fg= "black",command=salir).pack(pady=10)

    ventana_prestamos.mainloop()
