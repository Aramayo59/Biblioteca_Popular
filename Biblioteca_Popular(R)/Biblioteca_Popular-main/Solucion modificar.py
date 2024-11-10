####Solucion Modificar
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
