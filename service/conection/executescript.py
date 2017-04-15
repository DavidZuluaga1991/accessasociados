# cursor, clase para el manejo del SQL ???
cursor = conector.cursor()
 
# Creamos la consulta SQL
query = ("SELECT Nombre, Telefono FROM prueba")
 
# Ejecutamos la consula SQL
cursor.execute(query)