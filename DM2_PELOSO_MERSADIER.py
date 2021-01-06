#PELOSO
#MERSADIER

#Tout d'abord, les imports:

import matplotlib.pyplot as plt
import numpy as np



#On commence par lire le fichier texte et on stocke chaque ligne dans une liste:

fichier="photomosaic_input.txt"

with open(fichier,"r",encoding="utf8") as input_mozaic:

    donnees=[]

    for ligne in input_mozaic:

        donnees.append(ligne.strip("\n"))       '''ajout à la liste chaque
                                                    ligne du fichier texte en
                                                    les délimitant par les
                                                    sauts de lignes notés par
                                                    le sigle /n '''



#On détermine le plus grand élément de la 1ère "colonne" et de la 2ème "colonne";

x,y,z=donnees[0].split(", ")    '''affectation simultanée des nombres découpés
                                    par une virgule et un espace'''

for l in donnees:               '''parcourt de toutes les
                                    composantes de donnees'''

    i,j,k=l.split(", ")         '''affectation simultanée des nombres
                                    de chaque ligne une à une'''

    if int(i)>int(x):           '''comparaison de la plus grade valeur actuelle
                                    avec la valeur suivante de la 1ère colonne'''

        x=i                     '''affectation de la nouvelle plus grande
                                    valeur si True et rien si False'''

    if int(j)>int(y):           '''idem pour la 2ème colonne'''

        y=j
                                '''On obtient x=107 et y=179
                                    à la fin de la boucle for'''



#On crée une matrice avec le numéro des imagettes aux bonnes "coordonnées":

M=np.zeros((int(x)+1,int(y)+1),'uint8') '''création d'une matrice vide'''

for l in donnees:                       '''parcourt de toutes les
                                            composantes de donnees'''

    i,j,k=l.split(", ")                 '''affectation simultanée des nombres
                                            de chaque ligne une à une'''

    M[int(i),int(j)]=int(k)             '''remplissage de la matrice avec
                                            le numéro des imagettes en
                                            position [i,j]'''



#On déssine une page blanche:

blanc=[255,255,255]                 '''pixel blanc'''

N=[]                                '''future matrice de pixels blancs'''

for p in range((int(x)+1)*32):      '''les imagettes ont pour
                                        dimension 32x32'''

    P=[]                            '''liste vide que l'on vide
                                        à chaque itération'''
    for q in range((int(y)+1)*32):
        P.append(blanc)             '''remplissage de la liste
                                        avec des pixels blancs'''

    N.append(P)                     '''ajout de la liste à la liste
                                    pricipale pour faire la matrice'''



#On remplit la feuille blanche avec chaque pixel de chaque imagette:

for r in range (int(x)+1):          '''parcourt de toutes les lignes''''

    for s in range (int(y)+1):      '''et toutes les colonnes de M'''

                                    '''ajout de 0 inutiles pour la lecture
                                        de chaque imagette, pour que leur
                                        numéro soit composé de 3 digits'''

        if M[r,s]<10:

            L=plt.imread("imagettes/00"+str(M[r,s])+".png", 'uint8')

        elif M[r,s]>=10 and M[r,s]<100:

            L=plt.imread("imagettes/0"+str(M[r,s])+".png", 'uint8')

        else:

            L=plt.imread("imagettes/"+str(M[r,s])+".png", 'uint8')

        for p in range(32):

            for q in range(32):

                N[32*r+p][32*s+q]=L[p][q]       '''codage pixel par pixel
                                                    de N avec chaque imagette'''

#On affiche la photomosaïque:

plt.figure()
plt.imshow(N, interpolation='nearest')
plt.axis('off')
plt.title('photomosaïque')
plt.show()