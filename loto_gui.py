import tkinter as tk
from tkinter import messagebox
import random

def generer_tirage():
    # Génère 10 numéros uniques entre 1 et 49
    return set(random.sample(range(1, 50), 10))

def jouer():
    try:
        # Récupération de la saisie utilisateur
        saisie = entry.get()
        # On remplace les virgules par des espaces et on découpe
        choix_user = set(map(int, saisie.replace(',', ' ').split()))
        
        # Vérification du nombre de numéros (Il en faut 10 !)
        if len(choix_user) != 10:
            messagebox.showwarning("Attention", "Il vous faut 10 nombres exactement ! ✨")
            return
            
        tirage = generer_tirage()
        # Utilisation de l'intersection pour trouver les bons numéros
        bons_numeros = choix_user.intersection(tirage)
        nb_gagnants = len(bons_numeros)
        
        # Affichage du résultat dans l'interface
        res_text = f"Tirage : {sorted(list(tirage))}\n"
        res_text += f"Vos numéros : {sorted(list(choix_user))}\n"
        res_text += f"Bons numéros trouvés : {nb_gagnants}\n"
        
        label_resultat.config(text=res_text, fg="#DB7093") # Rose professionnel
        
        # Conditions de victoire
        if nb_gagnants >= 5: # On peut dire que 5 c'est déjà pas mal sur 10
            messagebox.showinfo("Bravo ! 🌸", f"Gagné ! Vous avez {nb_gagnants} bons numéros !")
        else:
            messagebox.showinfo("Dommage 🌙", f"Vous avez {nb_gagnants} bons numéros. Tentez encore !")
            
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des nombres valides séparés par un espace ! 😊")

# --- Design de l'Interface Graphique ---
root = tk.Tk()
root.title("Loto Girly Edition ✨")
root.geometry("450x550") # Augmenté un peu pour que les 10 numéros tiennent bien
root.configure(bg="#FFF0F5")

# Titre
title = tk.Label(root, text="🎲 My Loto Game", font=("Helvetica", 22, "bold"), 
                 bg="#FFF0F5", fg="#DB7093")
title.pack(pady=20)

# Instructions (Corrigé de 6 à 10)
instr = tk.Label(root, text="Entrez 10 numéros (1-49) séparés par un espace :", 
                 bg="#FFF0F5", font=("Helvetica", 10, "italic"))
instr.pack()

# Champ de saisie
entry = tk.Entry(root, font=("Helvetica", 14), justify='center', width=30, 
                 highlightthickness=2, highlightbackground="#FFB6C1", bd=0)
entry.pack(pady=15)

# Bouton Jouer
btn_jouer = tk.Button(root, text="Tirer au sort ✨", command=jouer, 
                      bg="#FFB6C1", fg="white", font=("Helvetica", 12, "bold"),
                      relief="flat", cursor="hand2", padx=20, pady=10)
btn_jouer.pack(pady=20)

# Zone de Résultat
label_resultat = tk.Label(root, text="", bg="#FFF0F5", font=("Helvetica", 11), justify="center")
label_resultat.pack(pady=20)

root.mainloop()
