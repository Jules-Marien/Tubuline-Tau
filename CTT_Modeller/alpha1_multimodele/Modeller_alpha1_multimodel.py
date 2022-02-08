#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 10:49:12 2022

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
              alnfile  = 'PIR_1SA0_tubuline_alpha1.ali',     # alignment filename
              knowns   = '1SA0',              # codes of the templates
              sequence = 'alpha1',            # code of the target
              assess_methods=(assess.DOPE,
                              #soap_protein_od.Scorer(),
                              assess.GA341))              #Permettent d'obtenir une évaluation des modèles générés



a.starting_model= 1                 # index of the first model
a.ending_model  = 5                 # index of the last model
                                    # (determines how many models to calculate)
a.make()                            # do the actual comparative modeling

"""
# Get a list of all successfully built models from a.outputs
ok_models = [x for x in a.outputs if x['failure'] is None]

# Rank the models by DOPE score
key = 'DOPE score'
if sys.version_info[:2] == (2,3):
    # Python 2.3's sort doesn't have a 'key' argument
    ok_models.sort(lambda a,b: cmp(a[key], b[key]))
else:
    ok_models.sort(key=lambda a: a[key])

# Get top model
m = ok_models[0]
print("Top model: %s (DOPE score %.3f)" % (m['name'], m[key]))
"""