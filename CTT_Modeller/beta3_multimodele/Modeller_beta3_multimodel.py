#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 17:01:00 2022

@author: marien
"""


# Comparative modeling by the AutoModel class
from modeller import *              # Load standard Modeller classes
from modeller.automodel import *    # Load the AutoModel class

log.verbose()    # request verbose output
env = Environ()  # create a new MODELLER environment to build this model in

# directories for input atom files
env.io.atom_files_directory = ['.']


a = AutoModel(env,
              alnfile  = 'PIR_beta3.ali',     # alignment filename
              knowns   = '5ij0',              # codes of the templates
              sequence = 'beta3',              # code of the target
              assess_methods=(assess.DOPE,
                              #soap_protein_od.Scorer(),
                              assess.GA341))             #Permettent d'obtenir une évaluation des modèles générés

      


a.starting_model= 1                 # index of the first model
a.ending_model  = 5                 # index of the last model
                                    # (determines how many models to calculate)
a.make()                            # do the actual comparative modeling