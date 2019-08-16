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
	nombre_choisi = float(nombre_choisi)
	
	
	if nombre_choisi<0 or nombre_choisi>49:
		while nombre_choisi<0 or nombre_choisi>49:
			nombre_choisi = input("\nLa roulette ne comporte que 50 nombres de 0 à 49. \nSur quel nombre misererez-vous?\n")
			nombre_choisi = float(nombre_choisi)
	else:
		print("Très bien!")	
		
	roulette = randrange(50)
	print("Et le numéro est...\n")
	time.sleep(2)
	print(roulette)




	rouge = False
	noir = False

	rouge2 = False
	noir2 = False

	if nombre_choisi % 2 == 0:
		rouge = True 
	else:
		rouge = False


	if rouge:
		noir = False 

	else:
		noir = True

	roulette = randrange(50)


	if roulette % 2 == 0:
		rouge2 = True 
	else:
		rouge2 = False
	
	if rouge2:
		noir2 = False 

	else:
		noir2 = True



	mise_joueur2 = mise_joueur/2
	mise_joueur3 = mise_joueur*3



	if nombre_choisi == roulette:
		print("\nBravo vous avez choisi le bon numéro! Voilà votre argent:\n", mise_joueur3,"$")
	elif noir and noir2:
		print("\nLes deux numeros sont impairs, voici la moitiée de votre mise:\n \n", mise_joueur2,"$")
	elif rouge and rouge2:
		print("\nLes deux numeros sont pairs, voici la moitiée de votre mise:\n \n", mise_joueur2,"$")
	else:
		print("\nDommage, ce n'est pas le bon et il n'a pas la même couleur Perdu \n")



	if nombre_choisi == roulette:
		argent_joueur = argent_joueur+mise_joueur3
	elif noir and noir2:
		argent_joueur = argent_joueur+mise_joueur2
	elif rouge and rouge2:
		argent_joueur = argent_joueur+mise_joueur2
	else:
		argent_joueur = argent_joueur
	
	

	time.sleep(3)

	if argent_joueur<=0:
		print("Vous n'avez plus d'argent! C'est la fin de la partie")
		continuer_partie = False
	else:
		print("Vous avez:",argent_joueur,"$")
		quitter = input("Voulez vous quitter le casino? (o/n)?")
		if quitter == "o" or quitter == "O":
			print("\nVous quitter le casino avec vos gains.\n")
			continuer_partie = False
			
os.system("pause")	
