import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry  # Importamos DateEntry para el calendario
import mysql.connector  # Asegúrate de que tienes esta biblioteca
from ConexionBDBiblioteca import *  # Importa la función de conexión a la BD
from ValidacionesPrestamos import *


def prestamos_interface():
    
    ventana_prestamos = tk.Tk()
    ventana_prestamos.title("Nuevo Préstamo")
    ventana_prestamos.geometry("350x700+500+70")
    ventana_prestamos.configure(bg="#ff5100")  

    marco_titulo = tk.Frame(ventana_prestamos, bg="#231c00", height=80)
    marco_titulo.pack(fill="x")

        
    tk.Label(marco_titulo, text="NUEVO", font=("Arial", 18, "bold"), fg="white", bg="#231c00").place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    tk.Label(marco_titulo, text="PRESTAMO", font=("Arial", 16, "bold"), fg="white", bg="#d9b38c").place(relx=0.5, rely=0.7, anchor=tk.CENTER)
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
                        nombre_completo = resultado   # Nombre y Apellido
                        nombre_completo_box['values'] = [nombre_completo]  # Cargar el nombre completo en el combobox
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

        
    def registrar_prestamo():
            socio = nombre_completo_box.get().strip()
            dni = dni_entry.get().strip()
            isbn = isbn_entry.get().strip()
            fecha_prestamo = devolucion_entry1.get()
            fecha_devolucion = devolucion_entry2.get_date()
            
            
            if socio and dni and isbn and fecha_prestamo and fecha_devolucion:
                try:
                    conexion = Cconexion.conexion()
                    cursor = conexion.cursor()
                    
                    cursor.execute("SELECT id_socios FROM socios WHERE DNI = %s",(dni,))
                    id_socio = cursor.fetchone()
                                        
                    if id_socio:
                       
                        cursor.execute("SELECT id_libros FROM libros WHERE isbn = %s",(isbn,))
                        isbn_libro = cursor.fetchone()  

                        if isbn_libro:
                            
                            sql_prestamo = """
                                INSERT INTO prestamos (id_socios, id_libros, fecha_prestamo, fecha_devolucion, estado_prestamo)
                                VALUES (%s, %s, %s, %s, %s)
                            """
                            valores = (id_socio[0], isbn_libro[0], fecha_prestamo, fecha_devolucion, 'Pendiente')
                            cursor.execute(sql_prestamo, valores)
                            conexion.commit()
                            
                            limpiar_campos()
                            messagebox.showinfo("Éxito", "El préstamo ha sido registrado exitosamente.")
                        else:
                            messagebox.showwarning("Error", "No se encontró el libro.")
                    else:
                        messagebox.showwarning("Error", "No se encontró el socio.")

                    conexion.close()
                        
                    

                except mysql.connector.Error as err:
                    messagebox.showerror("Error", f"Error al registrar el préstamo: {err}")
            else:
                messagebox.showwarning("Advertencia", "Por favor complete todos los campos.")
        
        
    tk.Label(ventana_prestamos, text="DNI", font=("Arial", 12, "bold"), bg="#ff5100", fg="white").pack(pady=10)
    dni_entry = tk.Entry(ventana_prestamos, font=("Arial", 12), width=25)
    dni_entry.pack()
       

    tk.Button(ventana_prestamos, text="Buscar Socio", font=("Arial", 10, "bold"), bg="#d9b38c", command=buscar_socio).pack(pady=10)
        
    tk.Label(ventana_prestamos, text="Nombre completo", font=("Arial", 12, "bold"), bg="#ff5100", fg="white").pack(pady=10)
    nombre_completo_box = ttk.Combobox(ventana_prestamos, font=("Arial", 12), width=25, state="readonly")
    nombre_completo_box.pack()

        

    tk.Label(ventana_prestamos, text="Isbn del libro", font=("Arial", 12, "bold"), bg="#ff5100", fg="white").pack(pady=10)
    isbn_entry = tk.Entry(ventana_prestamos, font=("Arial", 12), width=25)
    isbn_entry.pack()

    tk.Button(ventana_prestamos, text="Buscar Libro", font=("Arial", 10, "bold"), bg="#d9b38c", command=buscar_libros).pack(pady=10)

    tk.Label(ventana_prestamos, text="Fecha Préstamo", font=("Arial", 12, "bold"), bg="#ff5100", fg="white").pack(pady=10)
    fecha_hoy1 = datetime.now().strftime('%d/%m/%Y')
    devolucion_entry1 = ttk.Combobox(ventana_prestamos, font=("Arial", 12), state="readonly")
    devolucion_entry1['values'] = (fecha_hoy1,)  # Asignar la fecha de hoy como el único valor
    devolucion_entry1.current(0)  # Seleccionar el primer (y único) elemento en la lista
    devolucion_entry1.pack(pady=20)
        
    tk.Label(ventana_prestamos, text="Fecha Devolución", font=("Arial", 12, "bold"), bg="#ff5100", fg="white").pack(pady=10)
    fecha_hoy2 = datetime.now()

    devolucion_entry2 = DateEntry(ventana_prestamos, font=("Arial", 12), width=23, background="lightgreen", foreground="black", borderwidth=2, locale="es_Es",  date_pattern='dd/MM/yyyy', mindate=fecha_hoy2, state="readonly")
    devolucion_entry2.pack(pady=20)

    def limpiar_campos():
        dni_entry.delete(0, tk.END)  
        nombre_completo_box.set("")  
        isbn_entry.delete(0, tk.END) 
        devolucion_entry2.set_date(datetime.now())

    # Botón para registrar el préstamo
    tk.Button(ventana_prestamos, text="Ingresar", font=("Arial", 12, "bold"), bg="#d9b38c", fg="black", command=registrar_prestamo).pack(pady=20)
    tk.Button(ventana_prestamos, text="Cancelar", font= ("Arial",12,"bold"),bg="#d9b38c", fg= "black",command=salir).pack(pady=10)

    ventana_prestamos.mainloop()


