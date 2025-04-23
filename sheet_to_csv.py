# By WAHYUDI MUHAMMAD IRFAN
import requests

# l'ID de fichier Google Sheets
sheet_id = "ID docs"
# Nom exact de la feuille (onglet) à exporter
sheet_name = "Ex : (Feuille 1)"

# Générer l’URL d’export
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

# Télécharger et enregistrer en CSV
response = requests.get(url)
if response.status_code == 200:
    with open("test.csv", "wb") as f:
        f.write(response.content)
    print("✅ Fichier CSV enregistré sous 'exported_sheet.csv'")
else:
    print("❌ Erreur lors du téléchargement :", response.status_code)
