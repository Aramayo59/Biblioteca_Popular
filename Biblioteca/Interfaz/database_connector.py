import mysql.connector
from tkinter import messagebox

class DatabaseConnector:
    def __init__(self):
        self.conexion = None
        self.cursor = None

    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(
                user='root',
                password='',
                host='127.0.0.1',
                database='bibliodb',
                port='3306'
            )
            self.cursor = self.conexion.cursor()
        except mysql.connector.Error as err:
            messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {err}")
            return False
        return True

    def ejecutar_consulta(self, consulta, parametros=()):
        self.cursor.execute(consulta, parametros)
        return self.cursor.fetchall()

    def ejecutar_cambio(self, consulta, parametros=()):
        self.cursor.execute(consulta, parametros)
        self.conexion.commit()

    def cerrar(self):
        if self.conexion:
            self.conexion.close()
