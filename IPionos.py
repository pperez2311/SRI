#Importa librerias
import urllib.request
#proporciona funciones del sistema operativo
import os

#Creamos la variable "ip_actual" indicando que busque en la url indicada nuestra direccion IP
Ip_actual=urllib.request.urlopen('https://ident.me').read().decode('utf8')
print(Ip_actual)

#Creamos otra variable que se llame IP antigua que consulte el txt creado con nuestra IP
Ip_antigua=file=open("antigua_IP.txt","r").readline(20)
print(Ip_antigua)



#Creamos un if en el que compruebe si las variables creadas anteriormente tienen el mismo valor
if Ip_actual==Ip_antigua:
    print ("la IP no ha cambiado")
#Indicamos que si no tienen el mismo valor, abrirá el txt y escribirá la IP actual
else:
    file=open("antigua_IP.txt", "w")    
    file.write(Ip_actual)
    file.close()
    print ("cambiada con éxito")
    #Por último indicamos el link proporcionado por IONOS para poder actualizar la IP.
    os.system('curl -X GET https://ipv4.api.hosting.ionos.com/dns/v1/')
