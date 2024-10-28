import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from ConexionBDBiblioteca import *
from FilaSeleccionada import *
  # Importa la función de fila seleccionada

def Modificar_Prestamos():
    # Obtener los valores de la fila seleccionada
    valores_fila = get_fila_seleccionada

    # Verificar que haya valores seleccionados
    if not valores_fila:
        messagebox.showwarning("Advertencia", "No se ha seleccionado ninguna fila.")
        return

    nombre, apellido, dni, isbn, fecha_devolucion, estado = valores_fila

    ventana_prestamos = tk.Tk()
    ventana_prestamos.title("Modificar Préstamo")
    ventana_prestamos.geometry("350x700+500+70")
    ventana_prestamos.configure(bg="#ff5100")

    # Encabezado
    marco_titulo = tk.Frame(ventana_prestamos, bg="#231c00", height=80)
    marco_titulo.pack(fill="x")
    tk.Label(marco_titulo, text="Modificar", font=("Arial", 18, "bold"), fg="white", bg="#231c00").place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    tk.Label(marco_titulo, text="Préstamo", font=("Arial", 16, "bold"), fg="white", bg="#d9b38c").place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    # Campos del formulario
    tk.Label(ventana_prestamos, text="Nombre completo", font=("Arial", 12, "bold"), bg="#ff5100", fg="white").pack(pady=10)
    nombre_completo_box = ttk.Combobox(ventana_prestamos, font=("Arial", 12), width=25, state="readonly", values=[f"{nombre} {apellido}"])
    nombre_completo_box.set(f"{nombre} {apellido}")
    nombre_completo_box.pack()

    tk.Label(ventana_prestamos, text="DNI", font=("Arial", 12, "bold"), bg="#ff5100", fg="white").pack(pady=10)
    dni_entry = tk.Entry(ventana_prestamos, font=("Arial", 12), width=25)
    dni_entry.insert(0, dni)
    dni_entry.pack()

    tk.Label(ventana_prestamos, text="ISBN del libro", font=("Arial", 12, "bold"), bg="#ff5100", fg="white").pack(pady=10)
    isbn_entry = tk.Entry(ventana_prestamos, font=("Arial", 12), width=25)
    isbn_entry.insert(0, isbn)
    isbn_entry.pack()

    tk.Label(ventana_prestamos, text="Fecha Devolución", font=("Arial", 12, "bold"), bg="#ff5100", fg="white").pack(pady=10)
    devolucion_entry = tk.Entry(ventana_prestamos, font=("Arial", 12), width=25)
    devolucion_entry.insert(0, fecha_devolucion)
    devolucion_entry.pack()

    # Función para modificar el préstamo
    def modificar_prestamo():
        nuevo_dni = dni_entry.get().strip()
        nuevo_isbn = isbn_entry.get().strip()
        nueva_fecha_devolucion = devolucion_entry.get().strip()

        if nuevo_dni and nuevo_isbn and nueva_fecha_devolucion:
            try:
                conexion = Cconexion.conexion()
                cursor = conexion.cursor()

                # Obtener id_prestamo a partir del ISBN original de la fila seleccionada
                cursor.execute("SELECT id_prestamos FROM prestamos WHERE isbn = %s", (isbn,))
                id_prestamo = cursor.fetchone()

                if id_prestamo:
                    # Actualizar los datos del préstamo
                    sql_update = """
                    UPDATE prestamos
                    SET fecha_devolucion = %s, id_socios = (SELECT id_socios FROM socios WHERE DNI = %s), id_libros = (SELECT id_libros FROM libros WHERE isbn = %s)
                    WHERE id_prestamos = %s;
                    """
                    valores = (nueva_fecha_devolucion, nuevo_dni, nuevo_isbn, id_prestamo[0])
                    cursor.execute(sql_update, valores)
                    conexion.commit()

                    messagebox.showinfo("Éxito", "El préstamo ha sido modificado exitosamente.")
                    ventana_prestamos.destroy()

                else:
                    messagebox.showwarning("Error", "No se encontró el préstamo.")

                conexion.close()

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error al modificar el préstamo: {err}")

        else:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos.")

    # Botón para modificar
    tk.Button(ventana_prestamos, text="Modificar", font=("Arial", 12, "bold"), bg="#d9b38c", command=modificar_prestamo).pack(pady=20)
    tk.Button(ventana_prestamos, text="Cancelar", font=("Arial", 12, "bold"), bg="#d9b38c", command=ventana_prestamos.destroy).pack(pady=10)

    ventana_prestamos.mainloop()
