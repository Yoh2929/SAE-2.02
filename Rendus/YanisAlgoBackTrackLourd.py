"""
Programme numéro 3

Permet une intégration complète des demandes clients :
+ Problème des n reines
+ Placer la première reines n'importe où
+ Récupérer les solutions

-Très lourd
"""

def est_valide(plateau, ligne, colonne):
    """
    Vérifie si une reine peut être placée en (ligne, colonne) sur le plateau donné.
    """
    for i in range(ligne):
        # Première conditon ==> vérifier si pas de reine sur la colonne
        if plateau[i] == colonne:
            return False
        # Deuxième conditoon ==> vérifier si il n'y à pas de reine dans les diagonales
        if abs(plateau[i] - colonne) == abs(i - ligne): #Elle stipule que si deux points A et B ont des coordonnées (x1, y1) et (x2, y2) respectivement, alors ils sont sur la même diagonale si et seulement si |x1 - x2| = |y1 - y2|
            return False
    # On retourne True si aucun des cas de non validités n'est constataté
    return True


def n_reines(n, ligne=0, plateau=None, solutions=None):
    """
    Génère toutes les solutions possibles pour le problème des n reines en utilisant la récursion.
    """
    if plateau is None: #La condtion pour savoir si le plateau à été initialisé si c'est égal à none alors il n'a jamais été initialisé
        plateau = []
        for i in range(n):
            plateau.append(-1)

    if solutions is None: #Idem qu'au dessus mais la ici pour la liste de solution
        solutions = []


    if ligne == n:
        solutions.append(list(plateau))
        return #Return important pour la récursivité car quand toutes les lignes on été traité d'un apelle récursive alors on ferme cette "Boite" et on ajoute la solutions 
    
    for colonne in range(n): #Si nous sommes sur la dernière colonne de la ligne actuelle et que est valide renvoit false alors ça veut dire qu'aucune reine ne peut être placée dans la dernière colonne donc l'algorithme retourn 
        if est_valide(plateau, ligne, colonne):
            plateau[ligne] = colonne #Si le placement de la dame à été validé alors on l'ajout au plateau
            n_reines(n, ligne+1, plateau, solutions) #On lance un apelle récursive qui va lancer une nouvelle boite
    return solutions

def affiche_solutions(sol, n, x, y):
    """
    Affiche toutes les solutions pour le problème des n reines qui ont une reine en (x, y).
    Ici est là tout le principe de le façon de trouver les solutions pour une reine imposé
    """
    l = []
    for plateau in sol:
        if plateau[x] == y: #On test ici pour récupérer les solutions avec la reine imposé
            l.append(plateau)
    return l

def TransformerSolutionEnCoordo(liste):
    """
    Permet à une fonction de prendre en paramètre une liste puis de transformer la liste de solution
    en coordonée pour que ça soit plus facile à comprendre. 

    Nous sommes bien dans le modèle (ligne, colonne)
    """
    res = []
    for i in range(0, len(liste)):
        tuple = (i, liste[i])
        res.append(tuple)
    return res


#Ici on demande la taille de l'échiquier
n = int(input("Entrez la taille de l'échiquier: "))

#Ici on demande la ligne à laquelle l'utilisateur veut placer la reine
x = int(input("Entrez la ligne de la première reine: "))
while x < 0 or x >= n:
    print(f"La ligne doit être un entier entre 0 et {n-1}. Veuillez saisir à nouveau.")
    x = int(input("Entrez la ligne de la première reine: "))
        

#Ici on demande la colonne à laquelle l'utilisateur veut placer la reine
y = int(input("Entrez la colonne de la première reine: "))
while y < 0 or y >= n:
    print(f"La colonne doit être un entier entre 0 et {n-1}. Veuillez saisir à nouveau.")
    y = int(input("Entrez la colonne de la première reine: "))

# Les solutions seront stocké dans la variables Solutions
solutions = n_reines(n)

print("\n---------------------------")
print("Tapez 1 : Toutes les solutions + Solution de la reine imposée")
print("Tapez 2 : Solution de la reine imposée seulement ")
valeur = int(input())


if(valeur == 1):
    print(f"Toutes les solutions pour le problème des {n} reines :")
    for i in range(0, len(solutions)):
        print(TransformerSolutionEnCoordo(solutions[i]))
    print(f"\nSolutions qui ont une reine en ({x}, {y}) :")
    listeSoluReine = affiche_solutions(solutions, n, x, y)

    for i in range(0, len(listeSoluReine)):
        print(TransformerSolutionEnCoordo(listeSoluReine[i]))


elif(valeur == 2):
    print(f"\nSolutions qui ont une reine en ({x}, {y}) :")
    listeSoluReine = affiche_solutions(solutions, n, x, y)
    for i in range(0, len(listeSoluReine)):
        print(TransformerSolutionEnCoordo(listeSoluReine[i]))


else:
    print("Error")




