import smtplib 
from email.message import EmailMessage

message = EmailMessage()

quien_envia = "paco@mail.paco.com"
quien_recibe = "correonormal"

message['Subject'] = "Asunto" 
message['From'] = quien_envia
message['To'] = quien_recibe
message.set_content("Hola paco que tal estas?")

server = smtplib.SMTP("pablo@mail.pmred.es", "587")
server.ehlo()
server.starttls()

server.login(quien_envia, "contraseña") 
server.send_message(message)
server.quit()
