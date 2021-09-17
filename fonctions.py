from random import randrange
from donnees import *
from re import *

def choisit_niveau():
    print("Choisisez un niveau")
    while 1:
        print("1-Facile \U0001F633    2-Meduim \U0001F633   3-Difficile \U0001F620")
        niveau = int(input())
        if niveau == 1:
            print("\nVous avez choisit le niveau FACILE")
            print("Astuce: Mots en rapport avec les chiffres\n")
            return liste_facile
        elif niveau == 2:
            print("\nVous avez choisit le niveau MEDIUM")
            print("Astuce: Mots en rapport avec les fruits\n")
            return liste_medium
        if niveau == 3:
            print("\nVous avez choisit le niveau DIFFICILE")
            print("Astuce: Mots n'ayant aucun rapport ensembles, peux etres de objets,noms,lieu...\n")
            return liste_difficile
        else:
            print("Veuillez choisir un niveau valide")


def genere_mot(liste_mots):
     rand = random
     rand = rand - 5
     rand = rand + randrange(0,5)
     aleatoire = randrange(0,rand)
     mot = liste_mots[aleatoire]
     return mot


def recherche_nom(nom):
    with open("scores.txt","r") as fichier:
       ligne = fichier.readline()
       ligne = ligne.strip()
       i=0
       oui=0
       while i<1000 and ligne!= " ":
           if ligne == nom:
               score = fichier.readline().strip()
               ligne = fichier.readline().strip()
               oui = 1
           elif oui == 0:
               score = "0000"
               ligne = fichier.readline()
           i= i+1
    if oui == 1:
        print("\n"+"Ravi de vous revoir "+nom+" \U0001F603")
        print("Votre ancien score: "+score+"\n")
    else:
        print("\n"+"Bienvenu au pendu "+nom+"!")
        print("Votre score: "+score+"\n")

    return score

def mets_nom(nom,score):
    with open("scores.txt","a") as fic:
        fic.writelines(nom+"\n"+str(score)+"\n")

def verifie_nom(nom):
    re_nom = compile(regex_nom)
    if match(re_nom,nom):
        return 0
    else:
        return 1


  
           

    