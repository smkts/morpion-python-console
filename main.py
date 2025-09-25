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
"""
ETAPE 3 — SAISIE D'UN COUP ET MISE A JOUR DU PLATEAU
Objectifs :
- Demander un coup au joueur au format "ligne colonne" (indices 0..2)
- Vérifier que le coup est valide : dans la grille + case vide
- Placer le symbole du joueur sur la case choisie
- Réafficher le plateau après le coup
"""

from typing import List

# -----------------------------
# 1) MODELE : plateau 3x3 vide
# -----------------------------
plateau: List[List[str]] = [[" " for _ in range(3)] for _ in range(3)]

# -----------------------------------
# 2) AFFICHAGE : grille lisible 0..2
# -----------------------------------
def afficher_plateau() -> None:
    """Affiche la grille avec les indices de lignes/colonnes."""
    print("   0   1   2")
    for i, ligne in enumerate(plateau):
        print(i, " | ".join(ligne))
        if i < 2:
            print("  ---+---+---")

# ---------------------------------------------------
# 3) LOGIQUE : alternance de joueurs et vérif de coup
# ---------------------------------------------------
def joueur_suivant(joueur_actuel: str) -> str:
    """Retourne 'O' si c’était 'X', sinon 'X'."""
    return "O" if joueur_actuel == "X" else "X"

def coup_valide(lig: int, col: int) -> bool:
    """
    Un coup est valide si :
    - lig et col ∈ {0,1,2}
    - la case (lig, col) est vide " "
    """
    return 0 <= lig < 3 and 0 <= col < 3 and plateau[lig][col] == " "

def jouer_coup(lig: int, col: int, joueur: str) -> bool:
    """
    Joue le coup si valide (écrit 'X' ou 'O' dans la case).
    Retourne True si le coup a été joué, False sinon.
    """
    if coup_valide(lig, col):
        plateau[lig][col] = joueur
        return True
    return False

# ------------------------------------------------
# 4) ENTREE UTILISATEUR : lire "ligne colonne"
# ------------------------------------------------
def lire_coup(joueur: str) -> tuple[int, int]:
    """
    Demande à l'utilisateur "ligne colonne" (0..2 0..2).
    - Re-demande tant que le format est mauvais ou le coup invalide.
    - Retourne (lig, col) sous forme d'entiers.
    """
    while True:
        s = input(f"[ETAPE 3] Joueur {joueur}, entre ton coup (ligne colonne, ex: 1 2) : ").strip()
        parts = s.split()
        if len(parts) != 2:
            print("  → Format attendu : 2 nombres (ex: 0 2).")
            continue
        try:
            lig, col = int(parts[0]), int(parts[1])
        except ValueError:
            print("  → Merci d'entrer des nombres entiers (0, 1 ou 2).")
            continue

        if not coup_valide(lig, col):
            print("  → Coup invalide (hors limites ou case occupée).")
            continue
        return lig, col

# -------------------------
# 5) DEMO : un tour jouable
# -------------------------
def main() -> None:
    print("[ETAPE 3] Création du plateau et premier coup.")
    afficher_plateau()

    joueur = "X"  # on commence avec X
    lig, col = lire_coup(joueur)
    ok = jouer_coup(lig, col, joueur)

    if ok:
        print(f"[ETAPE 3] Coup joué : {joueur} en ({lig},{col}) ✅")
    else:
        print("[ETAPE 3] (improbable) coup refusé ❌")

    print("[ETAPE 3] Plateau après le coup :")
    afficher_plateau()

    # Petit aperçu : passage au joueur suivant
    joueur = joueur_suivant(joueur)
    print(f"[ETAPE 3] Prochain joueur : {joueur}")

if __name__ == "__main__":
    main()
"""
ETAPE 4 — BOUCLE DE JEU 1v1 (sans détection de victoire)
Objectifs :
- Alterner automatiquement entre 'X' et 'O'
- Demander et valider les coups à chaque tour
- Arrêter quand 9 coups ont été joués (plateau plein)
"""

from typing import List, Tuple

# -----------------------------
# 1) MODELE : plateau 3x3 vide
# -----------------------------
plateau: List[List[str]] = [[" " for _ in range(3)] for _ in range(3)]

# -----------------------------------
# 2) AFFICHAGE : grille lisible 0..2
# -----------------------------------
def afficher_plateau() -> None:
    """Affiche la grille avec les indices de lignes/colonnes."""
    print("   0   1   2")
    for i, ligne in enumerate(plateau):
        print(i, " | ".join(ligne))
        if i < 2:
            print("  ---+---+---")

# -------------------------------------------
# 3) LOGIQUE : alternance + validation de coup
# -------------------------------------------
def joueur_suivant(joueur_actuel: str) -> str:
    """Retourne 'O' si c’était 'X', sinon 'X'."""
    return "O" if joueur_actuel == "X" else "X"

def coup_valide(lig: int, col: int) -> bool:
    """Vrai si (lig,col) dans la grille ET case vide."""
    return 0 <= lig < 3 and 0 <= col < 3 and plateau[lig][col] == " "

def jouer_coup(lig: int, col: int, joueur: str) -> bool:
    """Pose le symbole si le coup est valide. Renvoie True/False."""
    if coup_valide(lig, col):
        plateau[lig][col] = joueur
        return True
    return False

# ------------------------------------------------
# 4) ENTREE UTILISATEUR : lire "ligne colonne"
# ------------------------------------------------
def lire_coup(joueur: str) -> Tuple[int, int]:
    """
    Demande "ligne colonne" (0..2 0..2).
    Re-demande tant que le format est mauvais ou la case invalide.
    """
    while True:
        s = input(f"[ETAPE 4] Joueur {joueur}, coup (ligne colonne, ex: 1 2) : ").strip()
        parts = s.split()
        if len(parts) != 2:
            print("  → Format attendu : 2 nombres (ex: 0 2)."); continue
        try:
            lig, col = int(parts[0]), int(parts[1])
        except ValueError:
            print("  → Merci d'entrer des nombres entiers (0, 1 ou 2)."); continue
        if not coup_valide(lig, col):
            print("  → Coup invalide (hors limites ou case occupée)."); continue
        return lig, col

# ----------------------------------------
# 5) BOUCLE DE PARTIE (sans victoire)
# ----------------------------------------
def partie_1v1_simple() -> None:
    print("[ETAPE 4] Nouvelle partie — X commence.")
    afficher_plateau()
    joueur = "X"
    coups_joues = 0

    while coups_joues < 9:      # 9 cases → plateau plein
        lig, col = lire_coup(joueur)
        if jouer_coup(lig, col, joueur):
            coups_joues += 1
            print(f"[ETAPE 4] {joueur} a joué ({lig},{col}).")
            afficher_plateau()
            joueur = joueur_suivant(joueur)   # on passe la main
        else:
            print("[ETAPE 4] Coup refusé, réessaie.")

    print("[ETAPE 4] Fin — le plateau est plein (victoire/nul à l'étape 5).")

# -------------------------
# 6) Point d'entrée
# -------------------------
def main() -> None:
    partie_1v1_simple()

if __name__ == "__main__":
    main()
