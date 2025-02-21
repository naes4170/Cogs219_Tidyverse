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


def generate_trials(subj_code, seed, num_reps):
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
    for num in range (num_reps):
        for tr_ty in trial_type:
            for ori in orientation:
                cur_stim = random.choice(colors)
                if tr_ty == "incongruent":
                    cur_color = make_incongruent(colors, cur_stim)
                else:
                    cur_color = cur_stim
                trials.append([subj_code,seed,cur_stim, cur_color, tr_ty, ori])
    #Randomizing
    random.shuffle(trials)
    # write the trials to the file
    for trial in trials:
        f.write(separator.join(map(str, trial)) + '\n')
                
    return trials
    #close the file
    f.close()

#Copied the following from mental rotation practice we did in class
def get_runtime_vars(defaults, order):
    core.wait(0.1)  # Small delay before dialog
    dlg = gui.DlgFromDict(dictionary=defaults, order=order, title="Stroop Setup")
    core.wait(0.1)  # Small delay after dialog
    return defaults if dlg.OK else None
order = ['subj_code', 'seed', 'num_reps']
runtime_vars = get_runtime_vars({'subj_code':'stroop_101','seed': 101, 'num_reps': 25}, order)

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
key_pressed=False #Saw this in the answer key, put here in case
timer = core.Clock()

#Try reading trial file
from helper import get_runtime_vars, import_trials, load_files, get_keyboard_response

generate_trials(runtime_vars['subj_code'],runtime_vars['seed'], runtime_vars['num_reps'])
script_dir = os.path.dirname(os.path.abspath(__file__))
trial_path = os.path.join(script_dir,'trials',runtime_vars['subj_code']+'_trials.csv')
trial_list = import_trials(trial_path)
print(trial_list)

try:
    os.mkdir(os.path.join(script_dir,'data'))
except FileExistsError:
    pass

separator = ','
subj_data = open(os.path.join(script_dir, 'data', f"{runtime_vars['subj_code']}_data.csv"), mode="w", newline="")
header = separator.join(["subj_code","seed","word", 'color','trial_type','orientation', 'trial_num', 'response', 'is_correct', 'rt'])
subj_data.write(header+'\n')
trial_num = 0

#Looping trials through the lists
for trial in trial_list:
    cur_stim = trial['word']
    color = trial['color']
    trial_type = trial['trial_type']
    ori = trial['orientation']
    Ans = list(cur_stim[0])
    print(cur_stim[0])
    word_stim.setText(cur_stim)
    word_stim.setColor(color)
    fixation_cross.draw()
    if ori == 'upright':
        word_stim.setOri(0)
    else:
        word_stim.setOri(180)
    win.flip()
    core.wait(.5)
    win.flip()
    core.wait(.5)
    placeholder.draw()
    word_stim.draw()
    win.flip()

    timer.reset()
    key_pressed = event.waitKeys(keyList=['r','o','y','g','b','q'], maxWait=2)
    rt = round(timer.getTime(), 3)
    if not key_pressed:
        response = "No response"
        is_correct = 0
        Too_slow.draw()
        win.flip()
        core.wait(1)
    elif key_pressed == Ans:
         is_correct = 1
         response = key_pressed[0]
    elif key_pressed == ['q']:
        break
    else:
        is_correct = 0
        response = key_pressed[0]
        Feedback.draw()
        win.flip()
        core.wait(1)
    print(rt)

    trial_num += 1
    row = separator.join(map(str, [runtime_vars['subj_code'], runtime_vars['seed'], cur_stim, color, trial_type, ori, trial_num, response, is_correct, rt]))

    subj_data.write(row+'\n')
    timer.reset()

    core.wait(.15)
    if key_pressed == ['q']:
        break

subj_data.close()



# while True:
#     cur_stim = random.choice(stimuli)
#     Ans = list(cur_stim[0])
#     print(cur_stim[0])
#     incongruent_choice = make_incongruent(cur_stim)
#     word_stim.setText(cur_stim)
#     word_stim.setColor(incongruent_choice)
#     fixation_cross.draw()
#     win.flip()
#     core.wait(.5)
#     win.flip()
#     core.wait(.5)
#     placeholder.draw()
#     word_stim.draw()
#     win.flip()
#     timer.reset()
#     dur = timer.getTime()
#     key_pressed = event.waitKeys(keyList=['r','o','y','g','b','q'], maxWait=2)
#     if not key_pressed:
#         Too_slow.draw()
#         win.flip()
#         core.wait(1)
#     elif key_pressed == Ans:
#         pass
#     elif key_pressed == ['q']:
#         break
#     else:
#         Feedback.draw()
#         win.flip()
#         core.wait(1)
#     print(dur)

#     RTs.write(str(dur)+'\n')
#     timer.reset()

#     core.wait(.15)
#     if key_pressed == ['q']:
#         break
