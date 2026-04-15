import tkinter as tk
from tkinter import messagebox
import random

def generer_tirage():
    return set(random.sample(range(1, 50), 6))

def jouer():
    try:
        # Akhd l'arqam men l'entrée dyal l'utilisateur
        saisie = entry.get()
        choix_user = set(map(int, saisie.replace(',', ' ').split()))
        
        if len(choix_user) != 6:
            messagebox.showwarning("Attention", "il te faut 6 nombres exactement! ")
            return
            
        tirage = generer_tirage()
        bons_numeros = choix_user.intersection(tirage)
        nb_gagnants = len(bons_numeros)
        
        # Affichage dyal l'natija
        res_text = f"Tirage : {sorted(list(tirage))}\n"
        res_text += f"Vos numéros : {sorted(list(choix_user))}\n"
        res_text += f"Bons numéros : {nb_gagnants}\n"
        
        label_resultat.config(text=res_text, fg="#FF69B4") # Rose flashy
        
        if nb_gagnants >= 3:
            messagebox.showinfo("Bravo ! 🌸", f"Gagné ! t'a {nb_gagnants} bons numéros !")
        else:
            messagebox.showinfo("Dommage 🌙", "vous avez pas de chance !")
            
    except ValueError:
        messagebox.showerror("Erreur", "Enter les nombres séparés avec un espace! ")

# --- Interface Design ---
root = tk.Tk()
root.title("Loto Girly Edition ")
root.geometry("400x450")
root.configure(bg="#FFF0F5") # Lavender Blush (Rose très clair)

# Title
title = tk.Label(root, text="🎲 My Loto Game", font=("Helvetica", 20, "bold"), 
                 bg="#FFF0F5", fg="#DB7093") # Pale Violet Red
title.pack(pady=20)

# Instructions
instr = tk.Label(root, text="Entrez 6 numéros (1-49):", bg="#FFF0F5", font=("Helvetica", 10))
instr.pack()

# Input field
entry = tk.Entry(root, font=("Helvetica", 14), justify='center', width=20, 
                 highlightthickness=2, highlightbackground="#FFB6C1", bd=0)
entry.pack(pady=10)

# Play Button
btn_jouer = tk.Button(root, text="Tirer au sort ✨", command=jouer, 
                      bg="#FFB6C1", fg="white", font=("Helvetica", 12, "bold"),
                      relief="flat", padx=20, pady=10)
btn_jouer.pack(pady=20)

# Result Area
label_resultat = tk.Label(root, text="", bg="#FFF0F5", font=("Helvetica", 11), justify="left")
label_resultat.pack(pady=20)

root.mainloop()