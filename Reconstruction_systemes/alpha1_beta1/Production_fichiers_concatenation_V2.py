#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 16:25:18 2022

@author: marien
"""

#Ouvre le fichier brut pour lecture
with open('protein_tau_pour_beta1.txt','r') as file:
    data = file.readlines()

#La chaine est en position 21 dans la string pour un fichier PDB généré par VMD

nom_de_chaine = 'D' #Nom de chaine que l'on veut

longueur_fichier = len(data)

with open('protein_tau_pour_beta1_traite.txt','w') as outputfile:
    #Ecrit la première ligne
    outputfile.write(data[0])
    
    for i in range(1,longueur_fichier-1):
        line_to_modify = data[i]
        debut_de_ligne = line_to_modify[0:21]
        fin_de_ligne = line_to_modify[22:]
        ligne_modifiee = debut_de_ligne + nom_de_chaine + fin_de_ligne
        #with open('alpha1_pour_beta1_copie3.txt','w') as outputfile:
        outputfile.write(ligne_modifiee)
        print(i)
        
    #Ecrit la dernière ligne
    outputfile.write('TER')
    
    
    