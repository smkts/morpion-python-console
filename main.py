"""
ETAPE 5 — DETECTION DE VICTOIRE ET MATCH NUL
Objectifs :
- Vérifier après chaque coup si le joueur a gagné
- Déclarer victoire ou nul et arrêter la partie
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
    return "O" if joueur_actuel == "X" else "X"

def coup_valide(lig: int, col: int) -> bool:
    return 0 <= lig < 3 and 0 <= col < 3 and plateau[lig][col] == " "

def jouer_coup(lig: int, col: int, joueur: str) -> bool:
    if coup_valide(lig, col):
        plateau[lig][col] = joueur
        return True
    return False

# ------------------------------------------------
# 4) ENTREE UTILISATEUR
# ------------------------------------------------
def lire_coup(joueur: str) -> Tuple[int, int]:
    while True:
        s = input(f"[ETAPE 5] Joueur {joueur}, coup (ligne colonne, ex: 1 2) : ").strip()
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

# ------------------------------------------------
# 5) DETECTION DE VICTOIRE
# ------------------------------------------------
def victoire(joueur: str) -> bool:
    """Retourne True si le joueur a 3 alignés."""
    # lignes
    for i in range(3):
        if all(plateau[i][j] == joueur for j in range(3)):
            return True
    # colonnes
    for j in range(3):
        if all(plateau[i][j] == joueur for i in range(3)):
            return True
    # diagonales
    if all(plateau[i][i] == joueur for i in range(3)):
        return True
    if all(plateau[i][2 - i] == joueur for i in range(3)):
        return True
    return False

def plateau_plein() -> bool:
    """Retourne True si toutes les cases sont remplies."""
    return all(plateau[i][j] != " " for i in range(3) for j in range(3))

# ----------------------------------------
# 6) BOUCLE DE PARTIE AVEC VICTOIRE/NUL
# ----------------------------------------
def partie_1v1() -> None:
    print("[ETAPE 5] Nouvelle partie — X commence.")
    afficher_plateau()
    joueur = "X"

    while True:
        lig, col = lire_coup(joueur)
        jouer_coup(lig, col, joueur)
        print(f"[ETAPE 5] {joueur} a joué ({lig},{col}).")
        afficher_plateau()

        # Vérifier victoire
        if victoire(joueur):
            print(f"[ETAPE 5] 🎉 Joueur {joueur} gagne la partie !")
            break

        # Vérifier nul
        if plateau_plein():
            print("[ETAPE 5] 🤝 Match nul !")
            break

        joueur = joueur_suivant(joueur)

# -------------------------
# 7) Point d'entrée
# -------------------------
def main() -> None:
    partie_1v1()

if __name__ == "__main__":
    main()
