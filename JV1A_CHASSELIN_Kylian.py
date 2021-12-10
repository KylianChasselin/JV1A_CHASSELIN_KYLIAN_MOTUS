from colorama import init
init()
from colorama import Fore, Back, Style

import random

mots = ["castor", "cinema", "cypres", "citron", "whisky", "joyaux", "abimes", "stereo", "sabres", "psycho"]

def motAtrouver(mot_1,mot_joueur):
    for i in range (0,6):
        mot_joueur[i-1] = input("trouve une lettre :  ")
    return mot_joueur

def mot_vrai(mot_1,mot_joueur):
        if mot_joueur == mot_1 :
            print("bravo ! vous avez trouver le mot")
        if mot_joueur != mot_1 :
            print("essayer encore")

def lettre_bonne(mot_1, mot_joueur):
    for i in range (0,6):
        if mot_joueur[i] == mot_1[i]:
            print(Back.RED + mot_joueur[i], end=" ")
    return lettre_bonne

def mot_mauvaise_place(mot_1, mot_joueur):
    for i in range (0,6):
        if mot_joueur[i] != mot_1[i]:
            print(Back.YELLOW + mot_joueur[i], end=" ")
        
def lettre_pas_presente(mot_1, mot_joueur):
    for i in range (0,6):
        if mot_joueur[i] != mot_1[i]:
            print(Back.BLUE + mot_joueur[i], end=" ")
    return lettre_pas_presente

def tentative(tour):
    if tour > 7:
        print("la partie est fini")
    else :
        tour += 1

# test      --------------------------------------------------------------------------------------------------------------------



# fin test ---------------------------------------------------------------------------------------------------------------------

# mot de base

mot_1 =['c','a','s','t','o','r']
mot_2 =['c','i','n','e','m','a']
mot_3 =['c','y','p','r','e','s']
mot_4 =['c','i','t','r','o','n']
mot_5 =['w','h','i','s','k','y']
mot_6 =['j','o','y','a','u','x']
mot_7 =['a','b','i','m','e','s']
mot_8 =['s','t','e','r','e','o']
mot_9 =['s','a','b','r','e','s']
mot_10 =['p','s','y','c','h','o']

mot_joueur=[' ',' ',' ',' ',' ',' ']


# programme principale

motMystere = random.randint(mots)

tour = 0     # debut de partie

print("bienvenue au motus, vous avez 8 chance pour trouver le mot mystere")

while tour != 7 :
    motAtrouver(mot_1,mot_joueur)
    mot_vrai(mot_1,mot_joueur)
    lettre_bonne(mot_1,mot_joueur)
    lettre_pas_presente(mot_1,mot_joueur)

    print(motAtrouver(mot_1,mot_joueur))

    tentative(tour)

from colorama import init
init()
print(Style.RESET_ALL)

input()

#---------------------------------------------------------------------------------------------------------------------

#liste probleme ===>

# probleme 1 -->  la premiere lettre entrée sera affiche comme la derniere dans la liste mais le reste est dans l'ordre

#probleme 2 --> le jaune ne fonctionne pas

#probleme 3 --> les tentatives ne fonctionnent pas ou sont infini

#probleme 4 --> on ne peut pas vraiment choisir de mot

#probleme 5 --> detection de la victoire mais le programme s'arrete pas

