#! /usr/bin/env python
 
# Importamos el conector de MySQL
import mysql.connector

def oppen_conection_function(db_host,db_user,db_pass,db_name):
    # Variable con la configuracion de la conexion
    config_mysql = {
        'user': db_user,
        'password': db_pass,
        'host': db_host,
        'database': db_name,
    }
    # conectamos al servidor MySql
    return conector = mysql.connector.connect(**config_mysql)

oppen_conection_function()

