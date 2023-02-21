#Importamos las librerias que vamos a utilizar
import os
import shutil
import ftplib
import datetime
from datetime import date
from cryptography.fernet import Fernet
import subprocess
import base64

#----------BASH------------------
# Obtiene la fecha actual en formato mes-día-año
date = subprocess.run(["date", "+%m-%d-%Y"], capture_output=True, text=True).stdout.strip()

# Crea un nombre de archivo con la fecha actual
filename = "Backup-" + date + ".zip"

# Lee la contraseña cifrada desde un archivo
with open("password_file.txt", "r") as password_file:
    encrypted_password = password_file.read().strip()
print("Contraseña del zip encriptada y desencriptada")
print(encrypted_password)

# Desencripta la contraseña
decrypted_password = base64.b64decode(encrypted_password).decode("utf-8")

print(decrypted_password)
# Comprime el directorio /public_html con la contraseña desencriptada y el nombre de archivo con fecha
subprocess.run(["zip", "--password", decrypted_password, "-r", filename, "/public_html/"])

#-----------PASS FTP------------
with open("password_fileFTP.txt", "r") as password_fileFTP:
    encrypted_passwordFTP = password_fileFTP.read().strip()
print("Contraseña del servidor FTP encriptada y desencriptada")
print(encrypted_passwordFTP)

decrypted_passwordFTP = base64.b64decode(encrypted_passwordFTP).decode("utf-8")
print(decrypted_passwordFTP)

#-----------PASS CORREO------------
with open("key.key", "rb") as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)

with open("password.txt", "rb") as password_file:
    ciphered_password = password_file.read()

password = cipher_suite.decrypt(ciphered_password)
password = password.decode()


#Datos del servidor FTP al que nos vamos a conectar
ftp_servidor = '192.168.1.148'
ftp_usuario  = 'userftp2'
ftp_clave    = decrypted_passwordFTP
#La raiz será el directorio predeterminado del usuario al que nos conectamos
ftp_raiz     = '/'

# Datos del fichero a subir
fichero_origen = f'/home/pablo/{filename}'
fichero_destino = filename 

#Nos conectamos con el servidor
s = ftplib.FTP(ftp_servidor, ftp_usuario, ftp_clave)
f = open(fichero_origen, 'rb')
s.cwd(ftp_raiz)
s.storbinary('STOR ' + fichero_destino, f)
f.close()
s.quit()
print ("El archivo se subió correctamente al servidor FTP")

# Eliminar la copia en el sistema cuando se sube al servidor.
	
os.remove(filename)
print ("Se eliminó la copia de seguridad .zip de este directorio")

#Máximo de 10 copias en el servidor. Se borra la más antigua.
s = ftplib.FTP(ftp_servidor, ftp_usuario, ftp_clave)
#Esto significa que las operaciones siguientes en el servidor FTP se realizarán en el directorio "ftp_raiz"
s.cwd(ftp_raiz) 
lista=s.nlst()
while len(lista) > 9:
	s.delete(lista[0])
	del lista[0]

#Enviamos el correo
from email.message import EmailMessage
import smtplib
remitente = "pperez2311@ieszaidinvergeles.org"
destinatario = "pruebaftpsri@gmail.com"
mensaje = "La copia de seguridad del servidor realizada con el script fue exitosa"
email = EmailMessage()
email["From"] = remitente
email["To"] = destinatario
email["Subject"] = "Copia de seguridad"
email.set_content(mensaje)
smtp = smtplib.SMTP_SSL("smtp.gmail.com")
smtp.login(remitente, password)
smtp.sendmail(remitente, destinatario, email.as_string())
smtp.quit()
print ("Correo enviado con exito")

