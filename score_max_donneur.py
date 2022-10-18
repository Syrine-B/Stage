#!/usr/bin/python3
###############
########### Utilisation
########### Python3 sortie.py [uts prune] [numero de gene]
########### a besoin pour fonctionner du fichier new_transfert obtenua l'aide de code.py
###############
################## Importation ##################

from ete3 import Tree
import argparse
import sys


################## declaration ##################
score_1 = []
score_2 = []

transfert_ale_1 = []
transfert_ale_2 = []
resume = []

num_gene = sys.argv[2]

sortie =  open("sortie_donneur.txt", "a") 

################## Fonction ##################

def recherche_inverse(dico, valeur):
    for k in dico:
        if dico[k] == valeur:
            return k
    raise LookupError()


###############################################################################################


ale_1 = open("new_transfert_donneur.txt","r")
ale_2 = open(sys.argv[1],"r")

################## isolement des espèces donneuses et receveuses ##################
ligne_ale_1 = ale_1.readlines()
lignes_ale_2 = ale_2.readlines()
try:
    info = ligne_ale_1[1].split(" ")

except:
    
    try:
        info = lignes_ale_2[1].split()
    
    except:
        sortie.write(num_gene+";"+"null"+";"+"null"+";"+"0"+";"+"0"+"\n")
        exit()
    
    del lignes_ale_2[0]
    for i in lignes_ale_2:
        info = i.split()
        donneur_a = info[0].split("(")
        receveur_a = info[1].split("(")
        transfert_ale_2.append(donneur_a[0])
        score = info[2].split()
        score_2.append(score[0])
    
    for j in range(len(transfert_ale_2)):
        sortie.write(num_gene+";"+"null"+";"+str(transfert_ale_2[j])+";"+"0"+";"+str(score_2[j])+"\n")
    
    exit()

for i in ligne_ale_1:
    info = i.split(" ")
    transfert_ale_1.append(info[0])
    score = info[4].split()
    score_1.append(score[0])
       
################## lecture du fichier transfert de ALE ##################



try: 
    info = lignes_ale_2[1].split()

except: 
    for i in range(len(transfert_ale_1)):
        sortie.write(num_gene+";"+str(transfert_ale_1[i])+";"+"null"+";"+str(score_1[i])+";"+"0"+"\n")
    exit()

################## Si fichier transfert Ale non vide ##################
del lignes_ale_2[0]
for i in lignes_ale_2:
    info = i.split()
    donneur_a = info[0].split("(")
    receveur_a = info[1].split("(")
    transfert_ale_2.append(donneur_a[0])
    score = info[2].split()
    score_2.append(score[0])
        
################## vérification correspondance transfert ##################

to_del=[]

for i in range(len(transfert_ale_1)):
    for j in range(len(transfert_ale_1)):
        if i!=j and j>i and transfert_ale_1[i] == transfert_ale_1[j] and float(score_1[i]) < float(score_1[j]):
            score_1[i] =float(score_1[j])


to_del=set(to_del)
to_del = sorted(to_del)

to_del.reverse()

for i in range(len(to_del)):
    index = to_del[i]
    del transfert_ale_1[index]
    del score_1[index]

to_del_2=[]

for i in range(len(transfert_ale_2)):
    for j in range(len(transfert_ale_2)):
        if i!=j and j>i and transfert_ale_2[i] == transfert_ale_2[j] and float(score_2[i]) < float(score_2[j]) :
          score_2[i] = float(score_2[j])


to_del_2=set(to_del_2)
to_del_2 = sorted(to_del_2)

to_del_2.reverse()

for i in range(len(to_del_2)):
    index = to_del_2[i]
    del transfert_ale_2[index]
    del score_2[index]

a_suppr=[]

for i in range(len(transfert_ale_1)):
    for j in range(len(transfert_ale_1)):
        if i!=j and i<j:
            if transfert_ale_1[i] == transfert_ale_1[j]:
                a_suppr.append(j)

a_suppr=set(a_suppr)
a_suppr = sorted(a_suppr)

a_suppr.reverse()

for i in range(len(a_suppr)):
    index = a_suppr[i]
    del transfert_ale_1[index]
    del score_1[index]

a_suppr_2 =[]

for i in range(len(transfert_ale_2)):
    for j in range(len(transfert_ale_2)):
        if i!=j and i<j:
            if transfert_ale_2[i] == transfert_ale_2[j]:
                a_suppr_2.append(j)

a_suppr_2=set(a_suppr_2)
a_suppr_2 = sorted(a_suppr_2)

a_suppr_2.reverse()

for i in range(len(a_suppr_2)):
    index = a_suppr_2[i]
    del transfert_ale_2[index]
    del score_2[index]




for i in range(len(transfert_ale_1)):
    for j in range(len(transfert_ale_2)):
        if transfert_ale_1[i]==transfert_ale_2[j]:
            resume.append(transfert_ale_1[i] + ";" + transfert_ale_2[j]+";"+str(score_1[i])+";"+str(score_2[j]))

for i in range(len(transfert_ale_1)):
    if transfert_ale_1[i] not in transfert_ale_2:
        resume.append(transfert_ale_1[i]+";"+"null"+";"+str(score_1[i])+";"+"0")

for i in range(len(transfert_ale_2)):
    if transfert_ale_2[i] not in transfert_ale_1:
        resume.append("null"+";"+transfert_ale_2[i]+";"+"0"+";"+str(score_2[i]))


for i in range(len(resume)):
	sortie.write(num_gene+";"+str(resume[i])+"\n")
