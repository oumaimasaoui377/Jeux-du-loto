import random

def generer_tirage():
    """Génère 10 numéros uniques entre 1 et 49."""
    return sorted(random.sample(range(1, 50), 10))

def saisir_numeros():
    """Demande à l'utilisateur 10 numéros valides."""
    numeros = set()

    # Correction hna: sddina les guillemets u l'parenthèse
    print("Saisissez 10 numéros entre 1 et 49 😊")

    while len(numeros) < 10:
        try:
            n = int(input(f"Numéro {len(numeros)+1} : "))
            if n < 1 or n > 49:
                print("❌ Le numéro doit être entre 1 et 49.")
            elif n in numeros:
                print("❌ Vous avez déjà saisi ce numéro.")
            else:
                numeros.add(n)
        except ValueError:
            print("❌ Veuillez entrer un nombre valide.")

    return sorted(numeros)

def comparer(tirage, choix):
    """Retourne une liste indiquant si chaque numéro est gagnant."""
    return [num in tirage for num in choix]

def compter_gagnants(resultats):
    """Compte le nombre de True dans la liste."""
    return sum(resultats)

def recompense(nb):
    """Retourne une récompense selon le nombre de bons numéros."""
    if nb <= 2:
        return "Aucune récompense 😕"
    elif nb <= 4:
        return "Petit lot 🍬"
    elif nb <= 6:
        return "Lot moyen 🧸"
    elif nb <= 8:
        return "Gros lot 🎁"
    elif nb <= 9:
        return "Super lot 🌟"
    else:
        return "JACKPOT !!! 💰💰💰"

def main():
    print("🎲 Bienvenue dans le jeu du Loto !\n")

    # Tirage automatique
    tirage = generer_tirage()
    
    # Choix de l'utilisateur
    choix = saisir_numeros()
    
    print("\n--- Résultats du Tirage ---")
    print("Le tirage était :", tirage)
    print("Vos numéros    :", choix)

    resultats = comparer(tirage, choix)

    print("\nAnalyse détaillée 😊")
    for num, ok in zip(choix, resultats):
        status = "✅ Gagnant" if ok else "❌ Perdu"
        print(f"{num} → {status}")

    nb_gagnants = compter_gagnants(resultats)
    print(f"\nTotal: Vous avez {nb_gagnants} numéro(s) gagnant(s).")
    print(f"🎁 Récompense : {recompense(nb_gagnants)}")

if __name__ == "__main__":
    main()