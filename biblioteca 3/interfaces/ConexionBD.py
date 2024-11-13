#ConexionDB.py

import mysql.connector

class conexion:
    
    def conexionBaseDatos():
        try:
            Conexion=mysql.connector.connect(user='root',password='',
                                             host='127.0.0.1',
                                             database='bibliodb',
                                             port='3306')
            
            print("Conexion a BD correcta")
            return Conexion
            
        except mysql.connector.Error as error:
            print("Error al conectarse a la base de datos{}".format(error))
            return Conexion
    
    conexionBaseDatos()    