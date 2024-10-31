import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry  # Importamos DateEntry para el calendario
import mysql.connector  # Asegúrate de que tienes esta biblioteca
from ConexionBDBiblioteca import *  # Importa la función de conexión a la BD
from ValidacionesPrestamos import *  
from datetime import date

def modificar_prestamos( isbn, fecha_devolucion):

    ventana_prestamos = tk.Toplevel()
    ventana_prestamos.title("Nuevo Préstamo")
    ventana_prestamos.geometry("350x600+500+70")
    ventana_prestamos.configure(bg="#ff5100")  

    marco_titulo = tk.Frame(ventana_prestamos, bg="#231c00", height=80)
    marco_titulo.pack(fill="x")

        
    tk.Label(marco_titulo, text="Modificar", font=("Arial", 18, "bold"), fg="white", bg="#231c00").place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    tk.Label(marco_titulo, text="Prestamo", font=("Arial", 16, "bold"), fg="white", bg="#d9b38c").place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    def salir():
        resp = messagebox.askquestion("Salir", "¿Desea Cancelar?")
        if resp == "yes":
                ventana_prestamos.destroy()

        
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
        isbn = isbn_entry.get().strip()
        fecha_prestamo = devolucion_entry1.get()
        fecha_devolucion = devolucion_entry2.get_date()
        
        if isbn and fecha_prestamo and fecha_devolucion:
            try:
                conexion = Cconexion.conexion()
                cursor = conexion.cursor()
                
                # Obtén el id del libro basado en el ISBN
                cursor.execute("SELECT id_libros FROM libros WHERE isbn = %s", (isbn,))
                id_libro = cursor.fetchone()
                
                if not id_libro:
                    messagebox.showerror("Error", f"No se encontró un libro con el ISBN: {isbn}")
                    return
                
                # Obtén el ID del préstamo asociado al libro
                cursor.execute("SELECT id_prestamos FROM prestamos WHERE id_libros = %s AND estado_prestamo = 'pendiente'", (id_libro[0],))
                id_prestamo = cursor.fetchone()
                
                if not id_prestamo:
                    messagebox.showwarning("Error", "No se encontró el préstamo asociado.")
                    return
                
                # Actualiza el préstamo
                sql = """
                    UPDATE prestamos 
                    SET fecha_prestamo = %s, fecha_devolucion = %s, estado_prestamo = 'Pendiente'
                    WHERE id_prestamos = %s;
                """
                valores = (fecha_prestamo, fecha_devolucion, id_prestamo[0])
                
                cursor.execute(sql, valores)
                conexion.commit()  # Asegúrate de confirmar los cambios
                limpiar_campos()
                messagebox.showinfo("Éxito", "El préstamo ha sido registrado exitosamente.")
                
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error al registrar el préstamo: {err}")
            finally:
                cursor.close()
                conexion.close()
        else:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos.")
    def limpiar_campos():
        isbn_entry.delete(0, tk.END) 
        devolucion_entry2.set_date(datetime.now())    
  

    tk.Label(ventana_prestamos, text="Isbn del libro", font=("Arial", 12, "bold"), bg="#ff5100", fg="white").pack(pady=10)
    isbn_entry = tk.Entry(ventana_prestamos, font=("Arial", 12), width=25)
    isbn_entry.insert(0, isbn)
    isbn_entry.pack()
    

    tk.Button(ventana_prestamos, text="Buscar Libro", font=("Arial", 10, "bold"), bg="#d9b38c", command=buscar_libros).pack(pady=10)
    

    tk.Label(ventana_prestamos, text="Fecha Préstamo", font=("Arial", 12, "bold"), bg="#ff5100", fg="white").pack(pady=10)
    fecha_hoy = datetime.now().strftime('%d/%m/%Y')
    devolucion_entry1 = ttk.Combobox(ventana_prestamos, font=("Arial", 12), state="readonly")
    devolucion_entry1['values'] = (fecha_hoy,)  # Asignar la fecha de hoy como el único valor
    devolucion_entry1.current(0)  # Seleccionar el primer (y único) elemento en la lista
    devolucion_entry1.pack(pady=20)
    
    
    tk.Label(ventana_prestamos, text="Fecha Devolución", font=("Arial", 12, "bold"), bg="#ff5100", fg="white").pack(pady=10)
    fecha_hoy2 = datetime.now()
    devolucion_entry2 = DateEntry(ventana_prestamos, font=("Arial", 12), width=23, background="lightgreen", foreground="black", borderwidth=2, locale="es_Es",  date_pattern='dd/MM/yyyy', mindate=fecha_hoy2, state="readonly")
    devolucion_entry2.pack(pady=20)

   

    
    tk.Button(ventana_prestamos, text="Registrar", font=("Arial", 12, "bold"), bg="#d9b38c", fg="black", command=ingresar_prestamo_modificado).pack(pady=20)
    tk.Button(ventana_prestamos, text="Cancelar", font= ("Arial",12,"bold"),bg="#d9b38c", fg= "black",command=salir).pack(pady=10)
    

  
    

    ventana_prestamos.mainloop()
