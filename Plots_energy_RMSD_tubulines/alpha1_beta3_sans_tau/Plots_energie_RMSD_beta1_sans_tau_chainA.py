#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 15:35:17 2022

@author: marien
"""

import numpy as np
import matplotlib.pyplot as plt

"""Energies"""
#Ouvre le fichier contenant le score DOPE
path_fichier_energie = '/ibpc/tethys/marien/Documents/Analyse_modeles_tubulines/Resultats_energie/alpha1_beta3_sans_tau/Brut_score_DOPE_chainA_beta3_sans_tau.txt'


Energies = np.genfromtxt(path_fichier_energie)


"""RMSDs"""
#Ouvre les fichiers contenant les RMSD du coeur et de la Cter
path_fichier_RMSD_coeur = '/ibpc/tethys/marien/Documents/Analyse_modeles_tubulines/Resultats_RMSD/alpha1_beta3_sans_tau/RMSD_coeurs_tubulines_alpha1_beta3_sans_tau_chainA.txt'


path_fichier_RMSD_Cter = '/ibpc/tethys/marien/Documents/Analyse_modeles_tubulines/Resultats_RMSD/alpha1_beta3_sans_tau/RMSD_Cter_tubulines_alpha1_beta3_sans_tau_chainA.txt'


RMSD_coeur = np.genfromtxt(path_fichier_RMSD_coeur)
RMSD_Cter  = np.genfromtxt(path_fichier_RMSD_Cter)


#We take the first 5 elements of the sorted table including the reference
energies_sorted = np.sort(Energies)
energies_five_last = energies_sorted[:5]

def table_indices(table_ref,table_to_compare):
    """Return the indices in table_ref of the elements in table_to_compare"""
    len_ref = len(table_ref)
    len_compare = len(table_to_compare)
    
    array_indices = np.array([])
    
    for i in range(len_compare):
        for j in range(len_ref):
            if table_to_compare[i] == table_ref[j]:
                array_indices = np.append(array_indices, j)
                
    return array_indices

#Indices of the 5 elements
tableau_indices = table_indices(Energies,energies_five_last)

#creation of the tables of corresponding RMSD
lowest_energie_RMSD_coeur = np.array([])
lowest_energie_RMSD_Cter = np.array([])

for i in range(len(tableau_indices)):
    lowest_energie_RMSD_coeur = np.append(lowest_energie_RMSD_coeur, RMSD_coeur[int(tableau_indices[i])])
    lowest_energie_RMSD_Cter = np.append(lowest_energie_RMSD_Cter, RMSD_Cter[int(tableau_indices[i])])
    


print("Les structures à sélectionner sont :", tableau_indices +1)
print("La structure de référence est la", int(tableau_indices[0] +1))

"""Plots"""
#Coeur tubuline
plt.figure()
plt.title('Energie en fonction de la RMSD du coeur de la tubuline beta3 \n pour alpha1/beta3 sans Tau')
plt.xlabel('RMSD coeur(A)')
plt.ylabel('Energie (DOPE)')
plt.scatter(RMSD_coeur,Energies,label='Structures générées')
plt.scatter(lowest_energie_RMSD_coeur,energies_five_last,color='red',label='Structures sélectionnées')

for i in range(len(tableau_indices)):
    plt.annotate(str(int(tableau_indices[i]) +1), (lowest_energie_RMSD_coeur[i],energies_five_last[i] + 20))
    
plt.legend()
#plt.show()
plt.savefig('Plot_energie_RMSD_coeur_tubuline_beta3_sans_tau.png')


#Cter tubuline
plt.figure()
plt.title('Energie en fonction de la RMSD de la Cter de la tubuline beta3 \n pour alpha1/beta3 sans Tau')
plt.xlabel('RMSD Cter(A)')
plt.ylabel('Energie (DOPE)')
plt.scatter(RMSD_Cter,Energies,label='Structures générées')
plt.scatter(lowest_energie_RMSD_Cter,energies_five_last,color='red',label='Structures sélectionnées')

for i in range(len(tableau_indices)):
    plt.annotate(str(int(tableau_indices[i]) +1), (lowest_energie_RMSD_Cter[i],energies_five_last[i] + 20))

plt.legend()
#plt.show()
plt.savefig('Plot_energie_RMSD_Cter_tubuline_beta3_sans_tau.png')

