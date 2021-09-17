import os
import fonctions
import donnees

os.system("color F0")
print("        *****************************************************************************************")
print("        *                                                                                       *")
print("        *___--||=========================  BIENVENU AU PENDU  ===========================||--___*")
print("        *                                                                                       *")
print("        * Regle: Trouvez le mot mystere en",donnees.nombres_chances,"tentatives selon le niveau de difficulte          *")
print("        * Astuce: Les mots sont des chiffres(facile),fruits(medium) ou n'importe quoi(dif..)    *")
print("        *****************************************************************************************")
continuer = 1
nom = input("Entrer votre nom svp >>  ")
while fonctions.verifie_nom(nom):
    nom = input("Entrer un nom valide svp >>  ")
nom = nom.upper()
score = int(fonctions.recherche_nom(nom))
score1 = 0
liste_mots = fonctions.choisit_niveau()
while continuer == 1:
    mot = fonctions.genere_mot(liste_mots)
    mystere = mot
    dico = ("*" * len(mot))
    print("Le mot mystere compte", len(mot), "lettres")
    oui = 0
    verif = []
    for i in range(donnees.nombres_chances+1):
        if mot == dico:
            print("Vous avez trouve le mot mystere en ",i,"coups \U0001F917" + "\U0001F917" + "\U0001F917")
            print("Votre score totale: ", score1 + score)
            oui = 1
            break
        else:
            print("Voici le mot mystere ", dico,"Il vous reste",donnees.nombres_chances-i,"tentatives")
            lettre = input("Entrer une lettre >> ")
            if len(lettre) == 1:
                if lettre in verif:
                    pass
                else:
                    lettre = lettre.lower()
                    pos = 0
                    for j in mot:
                        if lettre == j:
                            dico = list(dico)
                            mot = list(mot)
                            for y in range(len(dico)):
                                if pos == y:
                                    dico[y] = lettre
                                    verif.append(lettre)
                            print("Vous avez trouver la lettre '" + lettre + "' , vous etes sur la bonne voie")
                            score1 = int(score1) + (donnees.nombres_chances - i)
                            print("Votre score: ", score1, "\n")
                        pos = pos + 1
    if oui == 0:
        print("Le mot mystere etait: " + "'" + mystere + "'")
        print("Vous ne l'avez pas trouvez :( Essayez encore")
        score1 = 0000
    print("\nVoulez vous continuer a jouer ?")
    print("1- Oui\U0001F607    2-Non\U0001F608")
    continuer = int(input())
    fonctions.mets_nom(nom, score + score1)
print("Merci d'avoir jouer \U0001F603 "+nom+" J'espere te revoir bientot \U0001F633")

