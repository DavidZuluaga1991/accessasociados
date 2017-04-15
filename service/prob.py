#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "David Zuluaga"
__date__ = "$12/03/2017 08:09:12 PM$"

import smtplib
import socket
import sys
import getpass
 
def main():
 
 # Conexion con el servidor 
 try:
  smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
  smtpserver.ehlo()
  smtpserver.starttls()
  smtpserver.ehlo()
  print ("Conexion exitosa con Gmail")
  #print "Concectado a Gmail"
  # Datos 
  gmail_user = ""
  gmail_pwd = ""
  to = ""
  msg = ""
  header = ""
  bodymsg = ""
  try:
   gmail_user = "davidzuluaga1991@gmail.com"
   gmail_pwd =  "19910808Dz"# getpass.getpass("19910808Dz").strip()
   smtpserver.login(gmail_user, gmail_pwd)
  except smtplib.SMTPException:
   print ("Autenticacion incorrecta" + "\n")
   smtpserver.close()
   getpass.getpass("Presione ENTER para continuar...")
   sys.exit(1)
 
 
 except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException):
  print ("Fallo en la conexion con Gmail")
  print (getpass.getpass("Presione ENTER para continuar..."))
  sys.exit(1)
 
 
 while True:
  # to = str(raw_input("produccion1@softpymes.com.co")).lower().strip()
  to = "produccion1@softpymes.com.co"
  print (to)
  if to != "":
   break
  else:
   print ("El correo es necesario!!!")
 
 sub = "pro"
 bodymsg = "Mensaje: hola como estas realizando pruebas con python desde email"
 header = "<div> Para: " + to +"</div> <div><br></div> <div>" + "De: " + gmail_user + "</div><div><br></div> <div>" + "Asunto: " + sub + "<div></div> <br></div> "
 print (header)
 msg = header + bodymsg + "\n\n"
 print (msg)
 
 try:
  smtpserver.sendmail(gmail_user, to, header)
 except smtplib.SMTPException:
  print ("El correo no pudo ser enviado" + "\n")
  smtpserver.close()
  getpass.getpass("Presione ENTER para continuar...")
  sys.exit(1)
 
 print ("El correo se envio correctamente" + "\n")
 smtpserver.close()
 getpass.getpass("Presione ENTER para continuar")
 sys.exit(1)
 
 
main()