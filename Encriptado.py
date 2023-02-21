import sys
import hashlib

# Variables:
# directorio, index, usuario, password, listar
directorio = sys.argv[1]
index = sys.argv[2]
usuario = sys.argv[3]
contrasena = sys.argv[4]
listar = sys.argv[5]

if(len(sys.argv) == 6):
    print ("El directorio indicado sera: " + directorio)
    print ("El fichero index por defecto sera: " + index)
    print ("El usuario del directorio sera: " + usuario)
    print ("La contraseña del directorio sera: " + contrasena)
    print ("Listar parametros del directorio (S=Si N=No): " + listar)
    
    file=open(directorio+"/.htaccess","w")
    file.write(str("DirectoryIndex "+ index + "\n#Protect Directory\nAuthName \"Dialog prompt\"\nAuthType Basic\nAuthUserFile /home/username/example.com/.htpasswd\nRequire valid-user\n"))
    file.write(hashlib.md5(contrasena.encode('utf-8')).hexdigest())

else:
    print ("Necesario ejecutar con 6 parámetros")
    print ( "Ejemplo: ./script.py /htdocs/asir index-asir.php asir 123456 N")
