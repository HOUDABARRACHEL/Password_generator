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

def automatic(args): 
    charset = make_charset(args.use_upper, args.use_lower, args.use_digits, args.use_punctuation, args.use_space,
                           args.additional, args.blacklist)
    # Appelle une fonction make_charset avec plusieurs arguments pour créer un ensemble de caractères à utiliser pour générer les mots de passe.
    if not args.quiet: #(c'est-à-dire si l'utilisateur souhaite voir les messages d'information).
        print("Générateur de Mots de Passe par Houda Barrachel")
   
        print("→{}←".format("".join(sorted(charset))))
        print("Il peut y avoir au maximum {} occurrences du même caractère par mot de passe.".format(args.max_dupe)
              if args.max_dupe > 0 else "Il n'y a pas de limite de caractères en double.")
        print()
        print("Génération de {} mot{} de passe de longueur {} :".format(args.amount, "s" if args.amount > 1 else "", args.length))
        print()

    for _ in range(args.amount):
        password = generate_password(charset, args.length, args.max_dupe)
        print(password)