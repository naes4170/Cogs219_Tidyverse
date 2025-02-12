import time
import sys
import os
import random
import csv
from psychopy import visual,event,core,gui

stimuli = ['red', 'orange', 'yellow', 'green', 'blue']

win = visual.Window([800,600],color="gray", units='pix',checkTiming=False)
placeholder = visual.Rect(win,width=180,height=80, fillColor="lightgray",lineColor="black", lineWidth=6,pos=[0,0])
word_stim = visual.TextStim(win,text="", height=40, color="black",pos=[0,0])
fixation_cross = visual.TextStim(win,text="+", height=15, color="black",pos=[0,0])
instruction = visual.TextStim(win,text="Press the first letter of the ink color", height=20, color="black",pos=[0,-200], autoDraw=True)
Feedback = visual.TextStim(win,text="Incorrect", height=15, color="black")
RTs = open("RTs.csv", mode="w", newline="") #I tried what Chatgpt suggested but it didn't work, so I did it on my own through incorporating your in-class code!
key_pressed=False #Saw this in the answer key, put here in case
while True:
    cur_stim = random.choice(stimuli)
    Ans = list(cur_stim[0])
    print(cur_stim[0])
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
    timer = core.Clock()
    key_pressed = event.waitKeys(keyList=['r','o','y','g','b','q'])
    print(key_pressed)
    placeholder.draw()
    if key_pressed != Ans:
        Feedback.draw()
        core.wait(1)
        print(cur_stim)    
    win.flip()
    dur = timer.getTime()
    print(dur)
    RTs.write(str(dur)+'\n')
    timer.reset()

    core.wait(.15)
    if key_pressed == ['q']:
        break
