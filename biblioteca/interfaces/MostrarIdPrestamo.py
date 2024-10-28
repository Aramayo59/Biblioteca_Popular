from ConexionBDBiblioteca import * 
def mostrar_id_prestamo():
    try: 
            conexion = Cconexion.conexion()
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT

                    p.id_prestamo
                    
                FROM 
                    prestamos p
            """)
            conexion.commit
            miresultado = cursor.fetchall()
            conexion.close()
            return miresultado
    except mysql.connector.Error as error:
            print("Error de muestreo {}".format(error))