#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 16:30:11 2023

@author: ymear
"""

def resoudre_reines(n):
    """
    Trouve toutes les solutions au problème des n-reines pour un échiquier de taille n x n.

    La fonction utilise un algorithme de backtracking pour trouver toutes les configurations possibles
    de reines sur l'échiquier qui respectent les contraintes du problème (aucune paire de reines ne doit menacer
    une autre). La colonne de la 1ère dame doit êtreChaque solution est représentée par une liste de colonnes, où la valeur de chaque élément
    est le numéro de la colonne où se trouve la reine sur la ligne.

    La fonction retourne une liste de toutes les solutions possibles, si l'utilisateur veut les afficher, ou uniquement le nombre de solutions.
    """

    premiere_dame = int(input("Veuillez saisir la colonne de la 1ère dame : "))
    while (premiere_dame < 0 or premiere_dame >= n): # Vérifie que la première dame est comprise entre la première et dernière colonne
        print(f"La colonne de la 1ère dame doit être entre 0 et {n-1}. Veuillez réessayer.")
        premiere_dame = int(input())

    def est_valide(plateau, ligne, colonne):
        """
        Permet de vérifier si une reine peut être placée dans la case (ligne, colonne) du plateau.

        La fonction vérifie si la case est menacée par une autre reine déjà placée sur le plateau, et, si elle est menacée, la fonction renvoie False.
        """
        valide = True 
        for i in range(ligne):
            if (plateau[i] == colonne) or (plateau[i] - i == colonne - ligne) or (plateau[i] + i == colonne + ligne): ## Verifie s'il y'a déjà une reine dans la colonne, dans la diagonale d'en bas à gauche vers en haut à droite ou d'en haut à gauche vers en bas à droite
                valide = False ## Le booléen prend la valeur faux
        return valide

    def backtrack(plateau, ligne):
        """
        Fonction récursive qui utilise le principe du backtracing pour explorer toutes les possibilités du plateau.

        Cette fonction commence par placer une reine sur la première ligne à la colonne spécifiée par l'utilisateur, puis place une reine sur chacune des lignes suivantes en vérifiant si l'on peut en placer une avec la fonction est_valide. Si l'algorithme a parcouru toutes les lignes, une solution valide est ajoutée au tableau res. Sinon, la fonction explore toutes les configurations possibles pour la ligne suivante.
        """
        if ligne == n: # Si la ligne est égale à l'échiquier (donc si elle est arrivée au bout de l'échiquier), renvoie les solutions possibles
            return [plateau.copy()]
        
        res = [] # Crée un tableau pour stocker les résultats
        
        if ligne == 0: # Vérifie si la 1ère dame n'a pas encore été placée
            colonne = premiere_dame # La colonne prend la valeur saisie par l'utilisateur
            plateau[ligne] = colonne # Stocke la colonne où la reine est placée sur ligne
            res += backtrack(plateau, ligne+1) # Ajoute les solutions pour la ligne : ligne + 1
        else:
            for colonne in range(n):
                if est_valide(plateau, ligne, colonne): # Utilise la méthode définie avant pour vérifier que la reine ne gène pas les autres
                    plateau[ligne] = colonne 
                    res += backtrack(plateau, ligne+1) 
        return res
    

    
    plateau = [-1] * n ## Crée les cases vides du plateau

    solutions = backtrack(plateau, 0)
    print(f"Nombre de solutions pour un échiquier de taille {n}x{n}: {len(solutions)}") ## Renvoie le nombre de solutions pour un échiquier de n*n
    affiche = input("Voulez vous afficher toutes les solutions ?\n Tapez oui si vous voulez :") ## Demande la saisie pour afficher les solutions
    if (affiche == "oui" or affiche == "Oui"):  
        for i, sol in enumerate(solutions): ## Parcours toute les solutions
                print(f"Solution {i+1}: ") ## Affiche la prochaine solution
                for ligne in range(n):
                    resultat_ligne = ""
                    for colonne in range(n): ## On utilise une double boucle pour parcourir les colonnes de chaque ligne
                        resultat_ligne += "|"
                        if sol[ligne] == colonne:
                            resultat_ligne += "R" ## Ajoute la reine (représentée par R) sur la case où elle peut être placée.
                        else:
                            resultat_ligne += "." ## Autrement, une case avec un . est ajouté à cet emplacement.
                        resultat_ligne += "|"    
                    print(resultat_ligne)
        return solutions
    else :
        print("Fin du programme, vous n'avez pas voulu afficher les solutions") ## Cas où l'utilisateur n'a pas saisi oui ou Oui

# Créer le graphe pour un échiquier de taille 8x8

s = resoudre_reines(8)
print(s)
