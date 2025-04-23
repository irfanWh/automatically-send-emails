# 📧 Envoi d'e-mails automatiques depuis un fichier CSV

Ce script Python permet d'envoyer automatiquement des e-mails personnalisés à une liste de contacts stockés dans un fichier CSV, en utilisant le protocole SMTP (avec Gmail).

---

## ⚙️ Fonctionnalités

- Lecture de noms et d'e-mails depuis un fichier `CSV`
- Envoi d'e-mails un par un pour éviter les spams
- Personnalisation du message avec les noms
- Pause entre les envois pour rester dans les limites de Gmail

---

## 📝 Format attendu du fichier CSV (`test.csv`)

Le fichier csv doit contenir les colonnes suivantes :
name, email


> 📌 Le script lit chaque ligne, extrait les noms et les adresses e-mails, puis envoie un message à chaque contact.

---

## 🔐 Configuration

Avant d'exécuter le script :

1. Active le SMTP pour ton compte Gmail.
2. Active l’**authentification avec mot de passe d’application** (recommandé) si tu as l’authentification à deux facteurs.
3. Remplis tes informations dans le script :

```python
    sender_email = 'ton_email@gmail.com'
    sender_password = 'ton_mot_de_passe_app' Découvrez comment créer un mot de passe de application si vous ne savez pas comment procéder.
    message['Subject'] = 'Ton Sujet ici'
    body = f""" 
            Bonjour {names[i]},
            Corps de message ici
            """

Bibliothèques requises : 
    smtplib
    MIMEMultipart
    MIMEText
    csv
    time
    requests

# 📄 Exporter une Google Sheet en fichier CSV
# sheet_to_csv.py
Ce script Python permet de télécharger automatiquement une feuille de calcul Google Sheets et de l'enregistrer localement au format `.csv`.

> 🧠 Utile pour automatiser des extractions de données de feuilles Google.

---
# Paramètres à définir
sheet_id = "votre_id_google_sheet"
sheet_name = "Nom de la feuille"

# Où trouver ces infos ?
ID de la feuille : présent dans l'URL entre /d/ et /edit :
https://docs.google.com/spreadsheets/d/**VOTRE_ID**/edit#gid=0
Nom de la feuille : visible dans le bas de votre Google Sheet (ex: Feuille 1)