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
        
def interactive():
   
    print()

    charset = ask_charset(True, True, True, True, True, "", "")
    length = ask_length(12)
    max_duplicate_chars = ask_max_duplicate_chars(0, len(charset), length)

    while True:
        password = generate_password(charset, length, max_duplicate_chars)

        print("Voila votre mot de passe :")
        print("+-" + len(password) * "-" + "-+")
        print("| " + password + " |")
        print("+-" + len(password) * "-" + "-+")

        if not ask_yn("Est-ce que vous voullez generer un autre mot de passe avec les memes conditio que vous avez choisi ?", True):
            break

    print("Merci d'avoir utiliser ce programme!")
    
def parse_args():
    if len(sys.argv) <= 1:
        # no arguments --> interactive mode
        return None

    parser = argparse.ArgumentParser(description="Générateur de mots de passe aléatoires hautement personnalisable",
                                     epilog="Lancez-le sans aucun argument pour le mode interactif.")

    parser.add_argument("length", action="store", type=int,
                        help="Quelle est la longueur du mot de passe que vous voulez générer ?")
    parser.add_argument("-n", "--amount", action="store", type=int, dest="amount", default=1,
                        help="Combien de mots de passe voulez-vous créer ?")
    parser.add_argument("-m", "--max-duplicate-chars", action="store", dest="max_dupe", default=0, metavar="LIMIT",
                        help="Combien de fois un caractère peut-il se répéter dans votre mot de passe ?")

    parser.add_argument("-q", "--quiet", action="store_true", dest="quiet",
                        help="Mode silencieux (aucun message affiché)")

    p_charset = parser.add_argument_group("Spécification de l'ensemble de caractères")
    p_charset.add_argument("-u", "--uppercase", action="store_true", dest="use_upper",
                           help="Le mot de passe peut contenir des lettres majuscules de A à Z.")
    p_charset.add_argument("-l", "--lowercase", action="store_true", dest="use_lower",
                           help="Le mot de passe peut contenir des lettres minuscules de a à z.")
    p_charset.add_argument("-d", "--digits", action="store_true", dest="use_digits",
                           help="Le mot de passe peut contenir des chiffres.")
    p_charset.add_argument("-p", "--punctuation", action="store_true", dest="use_punctuation",
                           help="Inclure la ponctuation dans l'ensemble de caractères disponible.")
    p_charset.add_argument("-s", "--space", action="store_true", dest="use_space",
                           help="Inclure l'espace standard dans l'ensemble de caractères disponible.")

    p_charset.add_argument("-a", "--additional", action="store", default="", dest="additional",
                           help="Caractères supplémentaires à inclure dans l'ensemble de caractères disponible.")
    p_charset.add_argument("-b", "--blacklist", action="store", default="", dest="blacklist",
                           help="Caractères à exclure de l'ensemble de caractères disponible.")

    args = parser.parse_args()
    if not any([args.use_upper, args.use_lower, args.use_digits, args.use_punctuation, args.use_space,
               args.additional]):
        parser.error("Vous devez activer au moins une classe de caractères ou ajouter des caractères personnalisés !")
    return args

def ask_yn(message, default):
    if not isinstance(message, str) or not isinstance(default, bool):
        raise TypeError

    msg = message + (" (O/n) " if default else " (o/N) ")
    while True:
        answer = input(msg).lower().strip()
        if not answer:
            return default
        if answer in "on":
            return answer == "o"
        print("Désolé, veuillez entrer uniquement [o] ou [n] ou laisser vide pour accepter la valeur par défaut. Essayez encore!")