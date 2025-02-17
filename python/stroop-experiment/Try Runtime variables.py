import time
import sys
import os
import random
import csv
from psychopy import visual,event,core,gui
#Try Runtime variables
#Copied the following from mental rotation practice we did in class
def get_runtime_vars(defaults, order):
    core.wait(0.1)  # Small delay before dialog
    dlg = gui.DlgFromDict(dictionary=defaults, order=order, title="Stroop Setup")
    core.wait(0.1)  # Small delay after dialog
    return defaults if dlg.OK else None
order = ['subj_code', 'seed', 'num_reps']
runtime_vars = get_runtime_vars({'subj_code':'stroop_101','seed': 101, 'num_reps': 25}, order)
