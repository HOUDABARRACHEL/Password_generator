import sys #Cette bibliothèque permet d'interagir avec l'interpréteur Python
import string # Fournit des constantes et des fonctions pour manipuler des chaînes de caractères
import random #  Générer des nombres aléatoires pour diverses applications
import math #Fournit des fonctions mathématiques
import argparse # Gérer les arguments de ligne de commande

def main():
    args = parse_args() #Appelle une fonction parse_args qui analyse et retourne les arguments de ligne de commande.

    if args is None: # Verfie si args est none
        interactive() #Appelle une fonction nommée interactive
    else:
        automatic(args) #Si des arguments de ligne de commande ont été fournis, le programme doit fonctionner en mode automatique.
#génère des mots de passe basés sur les paramètres passés en arguments  depuis la ligne de commande.