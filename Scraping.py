#Importamos las librerías necesarias para el web scraping
import csv
import requests
import sys
import os
from bs4 import BeautifulSoup

#Comprobamos que se pase el enlace como argumento
if len(sys.argv) < 2 :
	print ('Tienes que pasar un enlace de un canal de YouTube')
	sys.exit()

#Asignamos el enlace a una variable y hacemos un cut para obtener el código fuente
url = sys.argv[1]
os.system(f"curl {url} > pagina.txt")


#Abrimos el archivo con el código fuente y hacemos un bucle para obtener el id de cada vídeo

with open("pagina.txt", "r") as archivo:
    contenido = archivo.read()

    index = 0
    while True:
        #Busca la cadena videoId
        index = contenido.find('"videoId":', index)
        if index == -1:
            break

        #Busca la siguiente aparición
        index_comilla = contenido.find('"', index + len('"videoId":') + 1)
        if index_comilla == -1:
            break

        #Guarda el texto en el archivo videoId.txt
        video_id = contenido[index + len('"videoId":')+1 : index_comilla]
        with open("videoId.txt", "a") as archivo_video_id:
            archivo_video_id.write(video_id + "\n")

        index = index_comilla

#Ordenamos los ids y eliminamos las duplicidades, luego añadimos la URL faltante
os.system("sort -u videoId.txt > videoId1.txt")
os.system("sed -i 's/^/https:\/\/www.youtube.com\/watch?v=/' videoId1.txt")


#Definimos los archivos de entrada y salida para el CSV
input_file = "videoId1.txt"
output_file = "webScraping.csv"

#Hacemos un bucle para hacer un request a cada enlace y obtener el título de cada vídeo
with open(input_file, "r") as f_input, open(output_file, "w", newline="") as f_output:
    csv_writer = csv.writer(f_output)

    #Iteramos sobre cada línea en el archivo de entrada
    for line in f_input:

        #Hacemos un request a la URL en la línea
        url = line.strip()
        response = requests.get(url)

        #Parseamos el contenido HTML utilizando BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        #Buscamos el título en la etiqueta <title>
        title = soup.find("title").get_text()

        #Escribimos el enlace y el título en el archivo CSV
        csv_writer.writerow([url, title])

#Eliminamos los archivos temporales
os.system("rm pagina.txt videoId.txt videoId1.txt")
