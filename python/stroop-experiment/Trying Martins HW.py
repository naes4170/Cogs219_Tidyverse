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
    #Randomizing
    random.shuffle(trials)
    # write the trials to the file
    for trial in trials:
        f.write(separator.join(map(str, trial)) + '\n')
                
    return trials
    #close the file
    f.close()

generate_trials('test', 1, 25)