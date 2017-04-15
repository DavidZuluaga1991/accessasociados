
#!/usr/bin/env python3
# importamos la libreria smtplib (no es necesario instalarlo)
import smtplib 
# importamos librerias  para construir el mensaje
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# definimos los correo de remitente y receptor
##se envia un mail a
addr_to   = 'angelica.accexasociadossas@gmail.com'#'davidzuluaga1991@gmail.com'
##el mail sale desde el correo
addr_from = 'davidzuluaga1991@gmail.com'#'angelica.accexasociadossas@gmail.com'

# Define SMTP email server details
# smtp_server = 'mail.gmail.com'
smtp_user   = "davidzuluaga1991@gmail.com"
smtp_pass   = '19910808Dz'
 
# Construimos el mail
msg = MIMEMultipart() 
msg['To'] = addr_to
msg['From'] = addr_from
msg['Subject'] = 'Ingresaron a un Formulario'
#cuerpo del mensaje en HTML y si fuera solo text puede colocar en el 2da parametro 'plain'
msg.attach(MIMEText('<div> Para:  '+ addr_to +'</div> <div><br></div> <div> + De:  '+ addr_from + '</div><div><br></div> <div>Asunto: Hola<div></div> <br></div> ','html'))


# inicializamos el stmp para hacer el envio
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
#logeamos con los datos ya seteamos en la parte superior
server.login(smtp_user,smtp_pass)
#el envio
server.sendmail(addr_from, addr_to, msg.as_string())
#apagamos conexion stmp
server.quit()