import os
from random import randrange
import time
argent_joueur = 100
argent_joueur = float(argent_joueur)
print("Vous avez",argent_joueur,"$")

continuer_partie = True

while continuer_partie:
 mise_joueur = input("\nQuelle sera votre mise?\n")
 mise_joueur = float(mise_joueur)

 if mise_joueur>argent_joueur:
		while mise_joueur>argent_joueur:
			mise_joueur = input("\nOn ne joue pas à crédit ici! \nQuelle sera votre mise?\n")
			mise_joueur = float(mise_joueur)
 else:
		print("Très bien!")



 argent_joueur = argent_joueur-mise_joueur

 nombre_choisi = input("\nSur quel nombre misererez-vous?\n")
 nombre_choisi = int(nombre_choisi)


 if nombre_choisi<0 or nombre_choisi>49:
  while nombre_choisi<0 or nombre_choisi>49:
			nombre_choisi = input("\nLa roulette ne comporte que 50 nombres de 0 à 49. \nSur quel nombre misererez-vous?\n")
			nombre_choisi = int(nombre_choisi)
 else:
	  print("Très bien!")
 roulette = randrange(50)
 print("Veuillez patienter, tirage en cours....\n")
 time.sleep(2)
 print("Le numéro gagnant est le: ",roulette)

 if nombre_choisi % 2 == 0:
		est_pair = True
 else:
		est_pair = False

 


 if roulette % 2 == 0:
  est_pair2 = True
 else:
  est_pair2 = False




 mise_joueur2 = mise_joueur/2
 mise_joueur3 = mise_joueur*3


 if nombre_choisi == roulette:
  print("\nBravo vous avez choisi le bon numéro! Voilà votre argent:\n", mise_joueur3,"$")
 elif est_pair == est_pair2:
  print("\nDommage ! Néanmoins les deux numeros ayant la même couleur, voici la moitiée de votre mise:\n \n", mise_joueur2,"$")
 else:
  print("\nDommage, il faudra tenter votre chance à nouveau !\n")


 if nombre_choisi == roulette:
  argent_joueur = argent_joueur+mise_joueur3
 elif est_pair == est_pair2:
  argent_joueur = argent_joueur+mise_joueur2
 else:
  argent_joueur = argent_joueur



 time.sleep(3)

 if argent_joueur<=0:
  print("Vous n'avez plus d'argent! C'est la fin de la partie")
  continuer_partie = False
 else:
  print("Vous avez:",argent_joueur,"$")
  quitter = input("Voulez vous quitter le casino? (o/n)?").upper()
  if quitter == "O":
   print("\nVous quitter le casino avec vos gains.\n")
   continuer_partie = False
  elif quitter == "N":
   continuer_partie = True

os.system("pause")	
