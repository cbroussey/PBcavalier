#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 11:10:56 2023

@author: cbroussey
"""

from time import *

def cavalier(lig, col, w = 8, h = 8, cases = []):
    cases = cases + [[lig, col]]
    solution = []
    # Il s'agit d'additions en fonction de la position actuelle (les différents mouvements en L)
    # Par exemple, en 3 3, l'algorithme va commencer par aller sur la case 3+(-2) 3+1
    # Les différents mouvements sont dans le sens des aiguilles d'une montre, en partant de haut-droite
    voisins = [[0, 0], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]] # [+lignes, +colonnes]
    if len(cases) == w * h: # Si on a parcouru toutes les cases
        solution = cases
    elif (cases[-1][0] <= w and cases[-1][0] > 0 and cases[-1][1] <= h and cases[-1][0] > 0):
        for i in voisins: # Parcours de tous les voisins possibles
            # Calcul de la nouvelle case en utilisant la position de l'ancienne
            nouveau = [cases[-1][0] + i[0], cases[-1][1] + i[1]]
            if (
                    not solution # Va immédiatement retourner si une solution a été trouvée
                    and nouveau not in cases
                    and nouveau[0] > 0
                    and nouveau[0] <= w
                    and nouveau[1] > 0
                    and nouveau[1] <= h
                ):
                solution = cavalier(nouveau[0], nouveau[1], w, h, cases)
    return solution

def cavIte(lig, col, long = 8, larg = 8):
    # On remplis la grille de vide
    solution = [[0, 0] for i in range(long * larg)]
    solution[0] = [lig, col]
    index = 0 # Indique la case actuelle
    voisins = [[0, 0], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]] # [+lignes, +colonnes]
    while index < len(solution) and index >= 0: # Si index < 0, alors pas de solution
        if (
            solution[index] not in solution[0:index]
            and solution[index][0] > 0
            and solution[index][0] <= long
            and solution[index][1] > 0
            and solution[index][1] <= larg
            ):
            # Permet de dire qu'on recommence la boucle des voisins ([0, 0] = premier index de la liste des voisins)
            lig = 0
            col = 0
        else:
            index -= 1 # Backtrack
            # Ici on calcule à quel étape de la liste des voisins on était en soustrayant la position actuelle à l'ancienne position
            # [lig, col] va donc correspondre à un élément de la liste des voisins
            # On peut ensuite utiliser voisins.index pour retrouver cet élément dans la liste
            # Ce qui va donc nous retourner un index de liste, nous permettant ainsi d'y ajouter 1 et de passer au voisin suivant
            lig = solution[index + 1][0] - solution[index][0]
            col = solution[index + 1][1] - solution[index][1]
            # On répète tant qu'on est arrivé au bout de la liste des voisins
            # Grace au recalcul de l'élément dans la liste des voisins qui a été utilisé pour trouver la nouvelle position
            while index >= 0 and voisins.index([lig, col]) == len(voisins) - 1 :
                index -= 1
                lig = solution[index + 1][0] - solution[index][0]
                col = solution[index + 1][1] - solution[index][1]
            if index < 0: # Si il n'y a pas de solution
                solution = []
        if index >= 0 and index < len(solution) - 1:
            # On définit le prochain élément dans la liste solution en utilisant la liste des voisins :
            # Grâce à lig et col, ont peut exécuter un voisins.index([lig, col]) ce qui va nous donner un index de liste
            # On va ensuite ajouter un à cet index de liste pour trouver le prochain élément dans la liste des voisins
            # Grâce à cet élément, on va ajouter à l'ancienne position y,x les valeurs respectives de l'élément
            # Exemple depuis 3, 3 : si lig = 0 et col = 0, alors voisins.index([lig, col]) + 1 = 1, et voisins[1] = [-2, 1]
            # Ainsi, 3 + (-2) = 1 et 3 + 1 = 4, donc la nouvelle position sera en [1, 4]
            solution[index + 1] = [solution[index][0] + voisins[voisins.index([lig, col]) + 1][0], solution[index][1] + voisins[voisins.index([lig, col]) + 1][1]]
        index += 1
    return solution

t1 = time()
a = cavalier(3, 3, 5, 5)
print(time() - t1)
print(a)
t2 = time()
b = cavIte(3, 3, 5, 5)
print(time() - t2)
print(b)