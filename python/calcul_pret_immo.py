#!/usr/bin/python

print "calcul des interets d'un pret immobilier"

taux_annuel = 0.04
taux_mensuel = taux_annuel/12

somme_initiale = 35000 # euros
mensualite = 700 # euros

print "taux annuel =", taux_annuel, "- mensualité =", mensualite

def calcul_mensuel(somme_qui_reste) :
	global taux_mensuel, mensualite
	reste = somme_qui_reste*(1+taux_mensuel) - mensualite
	if reste > 0 :
		versement = mensualite
	else :
		versement = somme_qui_reste*(1+taux_mensuel)
		reste = 0
	return reste, versement

somme_qui_reste = somme_initiale
remboursement = 0
n = 1
while somme_qui_reste > 0 :
	if n % 12 == 0 or n<12 :
		print "mois n°", n, ":", "Reste a payer", somme_qui_reste
	somme_qui_reste, versement = calcul_mensuel(somme_qui_reste)
	remboursement = remboursement + versement
	n = n+1

print "cout total =", remboursement - somme_initiale
