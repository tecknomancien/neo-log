# neo_blog_sync.py
# Script pour convertir les pensees de Neo en articles Markdown pour GitHub Pages (via Hugo ou Jekyll)

import json
import os
from datetime import datetime

MEMOIRE_PATH = "memoire.json"
OUTPUT_DIR = "_posts"  # Compatible Jekyll (GitHub Pages)

# Crée le dossier s'il n'existe pas
os.makedirs(OUTPUT_DIR, exist_ok=True)

def nettoyer_texte(texte):
    return texte.replace('\u201c', '"').replace('\u201d', '"').replace('\u2019', "'")

def generer_slug(texte):
    mots = texte.strip().lower().split()
    return "-".join(mots[:6])

def creer_articles():
    with open(MEMOIRE_PATH, "r", encoding="utf-8") as f:
        pensees = json.load(f)

    for entry in pensees:
        dt = datetime.fromisoformat(entry["datetime"])
        date_str = dt.strftime("%Y-%m-%d")
        heure = dt.strftime("%H:%M")
        slug = generer_slug(entry["texte"])
        filename = f"{OUTPUT_DIR}/{date_str}-{slug}.md"

        if os.path.exists(filename):
            continue  # déjà généré

        with open(filename, "w", encoding="utf-8") as f:
            f.write("---\n")
            f.write(f"title: \"Neo @ {heure}\"\n")
            f.write(f"date: {dt.isoformat()}\n")
            f.write(f"layout: post\n")
            f.write("---\n\n")
            f.write(nettoyer_texte(entry["texte"]))

if __name__ == "__main__":
    creer_articles()
    print("✅ Articles générés pour GitHub Pages.")

