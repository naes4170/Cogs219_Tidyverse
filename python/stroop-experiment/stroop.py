import time
import sys
import os
import random
from psychopy import visual,event,core,gui

stimuli = ['red', 'orange', 'yellow', 'green', 'blue']

win = visual.Window([800,600],color="gray", units='pix',checkTiming=False)
placeholder = visual.Rect(win,width=180,height=80, fillColor="lightgray",lineColor="black", lineWidth=6,pos=[0,0])
word_stim = visual.TextStim(win,text="", height=40, color="black",pos=[0,0])
fixation_cross = visual.TextStim(win,text="+", height=15, color="black",pos=[0,0])
instruction = visual.TextStim(win,text="Press the first letter of the ink color", height=20, color="black",pos=[0,-200], autoDraw=True)
while True:
    cur_stim = random.choice(stimuli)
    word_stim.setText(cur_stim)
    word_stim.setColor(cur_stim)
    fixation_cross.draw()
    win.flip()
    core.wait(.5)
    win.flip()
    core.wait(.5)
    placeholder.draw()
    word_stim.draw()
    win.flip()
    key_pressed = event.waitKeys(keyList=['r','o','y','g','b','q'])
    placeholder.draw()
    win.flip()
    core.wait(.15)
    if key_pressed == ['q']:
        break
