import time
import sys
import os
import random
import csv
from psychopy import visual,event,core,gui

#I did multiple testings on Jupyter notebook fpr this following function (an environment I am more familiar on)
#I also tried it in a separate .py file
#I then realized there are some problems, I've been using the wrong list of words for the incongruent function
#Trying Martin's HW
def generate_trials(subj_code, seed,num_repetitions=25):
    '''
    Writes a file named {subj_code_}trials.csv, one line per trial. Creates a trials subdirectory if one does not exist
    subj_code: a string corresponding to a participant's unique subject code
    seed: an integer specifying the random seed
    num_repetitions: integer specifying total times that combinations of trial type (congruent vs. incongruent) and orientation (upright vs. upside_down) should repeat (total number of trials = 4 * num_repetitions)
    '''
    import os
    import random

    # define general parameters and functions here
    colors = ['red', 'orange', 'yellow', 'green', 'blue']
    trial_type = ['congruent','incongruent']
    orientation = ['upright', 'upside_down']

    # This part I learned from the code on course website
    random.seed(seed)
    def make_incongruent(stimuli, color):
        possible_incongruent_colors = [stimulus for stimulus in stimuli if stimulus != color]
        incongruent_color = random.choice(possible_incongruent_colors)
        return incongruent_color

    # create a trials folder if it doesn't already exist
    script_dir = os.path.dirname(os.path.abspath(__file__))
    try:
        os.mkdir(os.path.join(script_dir,'trials'))
    except FileExistsError:
        print('Trials directory exists; proceeding to open file')
    f= open(os.path.join(script_dir, f"trials/{subj_code}_trials.csv"), "w")
    # f= open(f"trials/{subj_code}_trials.csv","w")

    # write header
    separator = ','
    header = separator.join(["subj_code","seed","word", 'color','trial_type','orientation'])
    f.write(header+'\n')
    
    # write code to loop through creating and adding trials to the file here
    trials = []
    for num in range (num_repetitions):
        for tr_ty in trial_type:
            for ori in orientation:
                cur_stim = random.choice(colors)
                if tr_ty == "incongruent":
                    cur_color = make_incongruent(colors, cur_stim)
                else:
                    cur_color = cur_stim
                trials.append([subj_code,seed,cur_stim, cur_color, tr_ty, ori])

    # write the trials to the file
    for trial in trials:
        f.write(separator.join(map(str, trial)) + '\n')
                
    return trials
    #close the file
    f.close()

incongruent_list = ['red', 'orange', 'yellow', 'green', 'blue']

def make_incongruent(cur_stim):
    filtered_list = list(filter(lambda word: word != cur_stim, incongruent_list))
    return random.choice(filtered_list)# I laid down the ground work but did pipe it into Chatgpt to bugfix the filter function

stimuli = ['red', 'orange', 'yellow', 'green', 'blue']

win = visual.Window([800,600],color="gray", units='pix',checkTiming=False)
placeholder = visual.Rect(win,width=180,height=80, fillColor="lightgray",lineColor="black", lineWidth=6,pos=[0,0])
word_stim = visual.TextStim(win,text="", height=40, color="black",pos=[0,0])
fixation_cross = visual.TextStim(win,text="+", height=15, color="black",pos=[0,0])
instruction = visual.TextStim(win,text="Press the first letter of the ink color", height=20, color="black",pos=[0,-200], autoDraw=True)
Feedback = visual.TextStim(win,text="Incorrect", height=15, color="black")
Too_slow = visual.TextStim(win,text="Too slow", height=15, color="black")
RTs = open("RTs.csv", mode="w", newline="") #I tried what Chatgpt suggested but it didn't work, so I did it on my own through incorporating your in-class code!
key_pressed=False #Saw this in the answer key, put here in case
timer = core.Clock()
while True:
    cur_stim = random.choice(stimuli)
    Ans = list(cur_stim[0])
    print(cur_stim[0])
    incongruent_choice = make_incongruent(cur_stim)
    word_stim.setText(cur_stim)
    word_stim.setColor(incongruent_choice)
    fixation_cross.draw()
    win.flip()
    core.wait(.5)
    win.flip()
    core.wait(.5)
    placeholder.draw()
    word_stim.draw()
    win.flip()
    timer.reset()
    dur = timer.getTime()
    key_pressed = event.waitKeys(keyList=['r','o','y','g','b','q'], maxWait=2)
    if not key_pressed:
        Too_slow.draw()
        win.flip()
        core.wait(1)
    elif key_pressed == Ans:
        pass
    elif key_pressed == ['q']:
        break
    else:
        Feedback.draw()
        win.flip()
        core.wait(1)
    print(dur)

    RTs.write(str(dur)+'\n')
    timer.reset()

    core.wait(.15)
    if key_pressed == ['q']:
        break
