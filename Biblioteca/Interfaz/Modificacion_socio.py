from ConexionBD import *

class Socio:
    
    def mostrar_socios():
        try:   
         cone = conexion.conexionBaseDatos()
         cursor= cone.cursor()
         cursor.execute("select * from socios;")
         miresultado = cursor.fetchall()
         #cone.commit()
         cone.close()
         return miresultado
            
        except mysql.connector.Error as error:
            print("Error de mostrar datos{}".format(error))
            return []
    
    
    def Ingresar_Socios(Apellido,Nombre,DNI,Domicilio,FechadePago,Teléfono,Sexo):
        
        try:
         cone = conexion.conexionBaseDatos()
         cursor= cone.cursor()
         sql="insert into socios values(null,%s,%s,%s,%s,%s,%s,%s);"
            
         valores=(Apellido,Nombre,DNI,Domicilio,FechadePago,Teléfono,Sexo)
            
         cursor.execute(sql,valores)
         cone.commit()
         print(cursor.rowcount,"Registro Ingresado")
         cone.close()
            
        except mysql.connector.Error as error:
            print("Error de ingreso de datos{}".format(error))
            
    def Modificar_Socios(ID,Apellido,Nombre,DNI,Domicilio,FechadePago,Teléfono,Sexo):
        
        try:
            cone = conexion.conexionBaseDatos()
            cursor= cone.cursor()
            sql="UPDATE socios set Apellido = %s ,Nombre = %s ,DNI = %s,Domicilio = %s,FechadePago = %s,Teléfono = %s,Sexo = %s where ID = %s;"
            
            valores=(Apellido,Nombre,DNI,Domicilio,FechadePago,Teléfono,Sexo,ID)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Actualizado")
            cone.close()
            
        except mysql.connector.Error as error:
            print("Error de modificacion de datos{}".format(error))