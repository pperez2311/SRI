contadorIP=10
with open('IP_Fijas_19102022.txt', 'r') as f:
        for host_name in f:
                #print (contadorIP)
                #host_name_replace = host_name.replace("----------", ";")
                #print (host_name_replace)
                datos_host=host_name.split('----------')
                #print (datos_host)

                print("Host" , datos_host[0] ,"{")
                print("\t#Asignación estática")
                print("\t hardware ethernet ", datos_host[1] , "; # Dirección MAC del host", datos_host[0], "El dispositivo es", datos_host[2])
                print('\t fixed-address 192.168.100.%d' %contadorIP,  "; # IP asignada al host", datos_host[0])
                print("}")
                contadorIP += 1