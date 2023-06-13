# PBcavalier
Solution au problème du cavalier
La fonction cavalier() correspond à une solution récursive, et la fonction cavIte() correspond à une solution itérative

## Le projet
Nous avons été missionnés d'analyser un problème mathématique et de coder deux versions d'un programme permettant d'y trouver la solution automatiquement : une version itérative (avec des boucles) et une version récursive (qui s'appelle elle-même)

## Ce que nous avons réalisé
Après avoir analysé le problème mathématique nous avons pensé à beaucoup d'algorithme avant de choisir d'utiliser du backtracking : Cela consiste, à chaque nouveau mouvement, de se souvenir de la position précédente, ce qui va nous permettre de revenir en arrière si jamais on se trouve bloqué. En effet, notre algorithme va tester tous les chemins possibles et a donc besoin de retourner en arrière si un chemin est sans issue. Une fois le chemin trouvé, la foncion retourne une liste contenant toutes les positions du cavalier afin de résoudre le problème.
