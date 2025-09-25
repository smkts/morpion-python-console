"""
ETAPE 1 — SQUELETTE DU PROGRAMME
Objectif :
- Vérifier que Python exécute bien le fichier.
- Créer un point d'entrée `main()` pour la suite.
"""

def main():
    print("[ETAPE 1] Bienvenue dans le jeu du Morpion (Tic-Tac-Toe) !")
    print("[ETAPE 1] Ce message confirme que Python exécute bien main.py.")

if __name__ == "__main__":
    main()
"""
ETAPE 2 — CREATION DU PLATEAU ET CHANGEMENT DE JOUEUR
Objectifs :
- Créer un plateau de 3x3 sous forme de liste de listes
- Pouvoir afficher le plateau
- Alterner entre les joueurs 'X' et 'O'
"""

# On initialise le plateau : 3 lignes et 3 colonnes vides
plateau = [[" " for _ in range(3)] for _ in range(3)]

def afficher_plateau():
    """Affiche le plateau sous forme lisible."""
    print("   0   1   2")
    for i, ligne in enumerate(plateau):
        print(i, " | ".join(ligne))
        if i < 2:
            print("  ---+---+---")

def joueur_suivant(joueur_actuel):
    """Retourne le joueur suivant : si X joue, alors O, et inversement."""
    return "O" if joueur_actuel == "X" else "X"

def main():
    print("[ETAPE 2] Création du plateau et gestion des joueurs")
    afficher_plateau()

    joueur = "X"
    print(f"[ETAPE 2] Le joueur actuel est : {joueur}")
    joueur = joueur_suivant(joueur)
    print(f"[ETAPE 2] Après changement, le joueur est : {joueur}")

if __name__ == "__main__":
    main()
