#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 17:02:35 2022

@author: marien
"""

from modeller import * 
from modeller.scripts import complete_pdb 
env = Environ() 
env.libs.topology.read(file='$(LIB)/top_heav.lib') 
env.libs.parameters.read(file='$(LIB)/par.lib') 
# Read a model previously generated by Modeller's automodel class 
mdl = complete_pdb(env, '/ibpc/tethys/marien/Documents/Essai_Alphafold/alpha1/prediction/selected_prediction_alpha1.pdb') 
zscore = mdl.assess_normalized_dope()