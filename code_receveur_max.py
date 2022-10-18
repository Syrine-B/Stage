#!/usr/bin/python3
###############
########### Utilisation
########### Python3 code.py [uts complet] [arbre complet] [arbre prune] [numero de gene]
###########
###############

from ete3 import Tree
import argparse
import sys

arbre_zombi= Tree(sys.argv[2],format=1) #grand
arbre_vivant = Tree(sys.argv[3],format =1) #petit

liste = []

liste_feuille_vivante = [i.name for i in arbre_vivant]
liste_feuille = [i.name for i in arbre_zombi]
liste_morte = list(set(liste_feuille)-set(liste_feuille_vivante))

ale = open(sys.argv[1],"r")

transfert = ale.readlines()

transfert_donneur = []
transfert_receveur = []
score=[]

num_gene = sys.argv[4]

nouveau_transfert = open("new_transfert_receveur.txt","a")

try: 
    info = transfert[1].split()

except:
	nouveau_transfert.write("null")
	exit()

del transfert[0]
for line in transfert:
	events = line.split()
	donneur_a = events[0].split("(")
	receveur_a = events[1].split("(")
	transfert_donneur.append(donneur_a[0])
	transfert_receveur.append(receveur_a[0])
	score.append(events[2])



#########PARTIE 2 : transformer ces deux listes (donneur receveur) en donneur-receveur dans l'arbre réduit
new_transfert_donneur = []

for d in transfert_donneur:
	node = arbre_zombi&d
	leaves = [i.name for i in node]
	descornot = len(list(set(liste_feuille_vivante) & set(leaves)))
	while (descornot==0 and node.is_root()!=True):
		node=node.up
		leaves = [i.name for i in node]
		descornot = len(list(set(liste_feuille_vivante) & set(leaves)))
	if (descornot==1):
		new_transfert_donneur.append(list(set(liste_feuille_vivante) & set(leaves))[0])
	else:
		new_transfert_donneur.append(arbre_vivant.get_common_ancestor(list(set(liste_feuille_vivante) & set(leaves))).name)

new_transfert_receveur = []

for d in transfert_receveur:
	node = arbre_zombi&d
	leaves = [i.name for i in node]
	descornot = len(list(set(liste_feuille_vivante) & set(leaves)))
	if (descornot==0):
		new_transfert_receveur.append("none")
	elif (descornot==1):
		new_transfert_receveur.append(list(set(liste_feuille_vivante) & set(leaves))[0])
	else:
		new_transfert_receveur.append(arbre_vivant.get_common_ancestor(list(set(liste_feuille_vivante) & set(leaves))).name)

transfert_new = []

transfert_disparu = []

for k in range(len(new_transfert_donneur)):
	if (new_transfert_receveur[k]!="none"):
		transfert_new.append(new_transfert_donneur[k] + " - " + new_transfert_receveur[k]+ " - "+ score[k])
	elif(new_transfert_receveur[k]=="none"):
		transfert_disparu.append(transfert_receveur[k] + ";" + "null" + ";" + str(score[k]) + ";" + "0")


mes_transferts = []

for i in range(len(transfert_new)):
	for j in range(len(transfert_new)):
		if(i!=j):
			transfert_1 = transfert_new[i].split("-")
			transfert_2 = transfert_new[j].split("-")

			if (str(transfert_1[0]) == str(transfert_2[0]) and str(transfert_1[1])==str(transfert_2[1])):
				if (float(transfert_1[2])>float(transfert_2[2])):
					mes_transferts.append(transfert_new[i])
					liste.append(j)
					liste.append(i)
				elif(float(transfert_1[2])<float(transfert_2[2])):
					mes_transferts.append(transfert_new[j])
					liste.append(j)
					liste.append(i)



for i in range(len(transfert_new)):
	if i not in liste:
		mes_transferts.append(transfert_new[i])
		liste.append(i)

nouveau_transfert = open("new_transfert_receveur.txt","a")


transfert_new_final = list(set(mes_transferts))

for i in range(len(transfert_new_final)):
	nouveau_transfert.write(str(transfert_new_final[i])+"\n")



sortie =  open("sortie_receveur.txt", "a") 

for i in range(len(transfert_disparu)):
	info = tansfert_disparu[i].split(";")
	disp.append(info[0])
	disp_score.append(info[2])


a_suppr=[]

for i in range(len(disp)):
    for j in range(len(disp)):
        if i!=j and j>i and disp[i] == disp[j] and float(disp_score[i]) < float(disp_score[j]) :
          disp_score[i] = float(disp_score[j])
		  a_suppr.append(j)



a_suppr=set(a_suppr)
a_suppr = sorted(a_suppr)

a_suppr.reverse()

for i in range(len(a_suppr)):
    index = a_suppr[i]
    del disp[index]
    del disp_score[index]

for i in range(len(disp)):
	transfert_disparu.append(disp[i] + ";" + "null" + ";" + str(disp_score[i]) + ";" + "0")


for i in range(len(transfert_disparu)):
	sortie.write(num_gene+ ";" +str(transfert_disparu[i])+"\n")