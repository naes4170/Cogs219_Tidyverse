import time
from psychopy import visual, sound, event, core

# Assuming you have a list of dictionaries with 'audio' and 'Comp_Q' keys
experimental_list = [
    {'audio': 'sound1.wav', 'Comp_Q': 'Question 1'},
    {'audio': 'sound2.wav', 'Comp_Q': 'Question 2'},
    # Add more trials as needed
]

# Create a window
win = visual.Window([800, 600])

timer = core.Clock()


# Function to present sound and fixation cross
def present_sound_and_fixation(audio_file):
    snd = sound.Sound(audio_file)
    snd.play()
    fixation = visual.TextStim(win, text='+')
    fixation.draw()
    win.flip()
    core.wait(1)  # 1 second interstimuli interval

# Function to present comprehension question and get response
def present_comprehension_question(question):
    comp_q = visual.TextStim(win, text=question)
    comp_q.draw()
    win.flip()
    response = event.waitKeys(keyList=['y', 'n'])  # Assuming 'y' and 'n' are valid responses
    core.wait(1)  # 1 second interstimuli interval
    return response

# Main loop for trial structure
for trial in experimental_list:
    present_sound_and_fixation(trial['audio'])
    response1 = present_comprehension_question(trial['Comp_Q'])
    present_sound_and_fixation(trial['audio'])
    response2 = present_comprehension_question(trial['Comp_Q'])

timer.reset()

#Write the responses to a file, each response is a new row
data_file = open(os.path.join(os.getcwd(),'data', runtime_vars['subj_code']'_data.csv'), 'w')

# Close the window
win.close()
core.quit()

#Add instructions
#Add event code
#Add code to write the responses to a file
#Make sure the responses are written line by line
#Add event code sending structure
#Make sure to restart event each time you present a new trial
#Add eye-tracker code
#Add helper info
