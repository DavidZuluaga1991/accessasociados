#! https://www.youtube.com/watch?v=zwiXn7juoOA
#! http://librosweb.es/libro/python/capitulo_12/conectarse_a_la_base_de_datos_y_ejecutar_consultas.html
#! http://codehero.co/python-desde-cero-bases-de-datos/
#! https://www.todavianose.com/conectarse-a-mysql-con-python/
#! https://www.youtube.com/watch?v=gmUq8ydZcuU

#! /usr/bin/env python
 
# Importamos el conector de MySQL
import mysql.connector
 
# Variable con la configuracion de la conexion
config_mysql = {
    'user': 'root',
    'password': '123456',
    'host': 'localhost',
    'database': 'prueba',
}
 
# conectamos al servidor MySql
conector = mysql.connector.connect(**config_mysql)
 
# cursor, clase para el manejo del SQL ???
cursor = conector.cursor()
 
# Creamos la consulta SQL
query = ("SELECT Nombre, Telefono FROM prueba")
 
# Ejecutamos la consula SQL
cursor.execute(query)
 
# Mostramos todos los datos de la consulta
for (Nombre, Telefono) in cursor:
    print("Nombre: " + Nombre + ", Telefono: " + Telefono)
 
# Cerramos cursor
cursor.close()
 
# Cerramos la conexion
conector.close()