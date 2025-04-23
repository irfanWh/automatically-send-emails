# By WAHYUDI MUHAMMAD IRFAN
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv
import time

# Configuration du serveur SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'ton_email@gmail.com'
sender_password = 'ton_mot_de_passe_app'

# Lire le fichier CSV 
with open("test.csv", mode="r", newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row if there is one
    for row in reader:
        emails=row[1].splitlines()
        names=row[0].splitlines()
        for i in range(len(emails)):
            # Création du message
            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = emails[i]
            message['Subject'] = 'Ton Sujet ici'
            # Corps du message
            body = f"""
            Bonjour {names[i]},      

            Corps du message ici.
            
            Bien à vous,
            WAHYUDI Muhammad irfan
            muhammadiw456t@gmail.com
            """
            message.attach(MIMEText(body, 'plain'))

            # Envoi du message
            try :
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.starttls()
                    server.login(sender_email, sender_password)
                    server.sendmail(message['From'], message['To'], message.as_string())
                    print(f"Email {i+1} envoyé avec succès !")
            except Exception as e:
                print(f"Une erreur s'est produite lors de l'envoi de l'e-mail : {e}")
            time.sleep(5)  # Pause de 5 secondes entre les envois d'e-mails