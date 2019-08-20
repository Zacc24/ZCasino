import os 
from random import randrange
import time


continuer_partie = True


print("Bonjour et bienvenu au ZCasino, la première simulation de la roulette au monde!\n")
time.sleep(3)
print("La roulette est composée de 50 nombres de 0 à 49\n")
time.sleep(3)
print("Les nombres pair sont rouge tandis que les nombres impairs sont noirs.\nSi vous misez sur le bon numéro je vous donne 3 fois votre mise!!!\n")
time.sleep(5)
print("Si le numéro choisi est de la même couleur que le numéro sortant, je vous rend la moitiée de votre mise\n")
time.sleep(4)
print("En revanche si vous avez tout faux tant sur la couleur que sur le numéro vous perdez toute votre mise!\n")
time.sleep(3)

argent_joueur = 100
argent_joueur = float(argent_joueur)
print("Vous avez",argent_joueur,"$\n")
time.sleep(2)

while continuer_partie:
 
	mise_joueur = input("\nQuelle sera votre mise?\n")
 
	try:
		mise_joueur = float(mise_joueur)	
	except ValueError:
		print("Vous ne savez pas faire la difference entre un nombre et des lettres!?\n")
		time.sleep(2)
		print("Le programme va s'arreter!\n")
		os.system("pause")
			
	
	if mise_joueur>argent_joueur:
		while mise_joueur>argent_joueur:
			mise_joueur = input("\nOn ne joue pas à crédit ici! \nQuelle sera votre mise?\n")
			mise_joueur = float(mise_joueur)
	else:
		print("\nTrès bien!\n")
	
	argent_joueur = argent_joueur-mise_joueur	
	nombre_choisi = input("\nSur quel nombre misererez-vous?\n")
	
	try:
		nombre_choisi = float(nombre_choisi)	
	except ValueError:
		print("\nHé non! Premiere nouvelle:", nombre_choisi,"n'est pas un nombre\n")
		time.sleep(4)
		print("C'est malin maintenant le programme va s'arreter!\n")
		os.system("pause")
	
		
	if nombre_choisi<0 or nombre_choisi>49:
		while nombre_choisi<0 or nombre_choisi>49:
			nombre_choisi = input("\nLa roulette ne comporte que 50 nombres de 0 à 49. \nSur quel nombre misererez-vous?\n")
			nombre_choisi = float(nombre_choisi)
	else:
	  print("\nExcellent choix!\n")
	  
	roulette = randrange(50)
	print("Veuillez patienter, tirage en cours....\n\n")
	time.sleep(3)
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
	elif argent_joueur==0:
		print("\nDommage, vous avez tout perdu!")
	else:
		print("\nDommage, il faudra tenter votre chance à nouveau !\n")
	

	if nombre_choisi == roulette:
		argent_joueur = argent_joueur+mise_joueur3
	elif est_pair == est_pair2:
		argent_joueur = argent_joueur+mise_joueur2
	else:
		argent_joueur = argent_joueur
	
	

	time.sleep(3)

	print("\nVous avez", argent_joueur,"$\n")

	if argent_joueur<=0:
		print("\nVous êtes ruiné! C'est la fin de la partie\n")
		continuer_partie = False
	else:
		quitter='X'
		while quitter.upper()!='O' and quitter.upper()!='N':
			quitter=input("Voulez vous quitter le casino? (o/n)?").upper()
		if quitter.upper() == "O":
			continuer_partie = False
			if argent_joueur<100:
				print("\nVous quitter le casino avec vos pertes:\n", argent_joueur-100,"$\n")
			else:	
				print("\nVous quittez le casino avec vos gains:\n", argent_joueur-100,"$\n")
			
			
os.system("pause")	
