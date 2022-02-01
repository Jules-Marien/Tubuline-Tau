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
              sequence = 'alpha1')              # code of the target

"""
a = AutoModel(env,
              alnfile  = 'PIR_1jff_tubuline_alpha1.ali',     # alignment filename
              knowns   = '1jff',              # codes of the templates
              sequence = 'alpha1')              # code of the target
"""

a.starting_model= 1                 # index of the first model
a.ending_model  = 1                 # index of the last model
                                    # (determines how many models to calculate)
a.make()                            # do the actual comparative modeling