#Try reading trial file
from generate_trials import generate_trials
from helper import get_runtime_vars, import_trials, load_files, get_keyboard_response

generate_trials(runtime_vars['subj_code'],runtime_vars['seed'], runtime_vars['num_repetitions'])

trial_path = os.path.join(os.getcwd(),'trials',runtime_vars['subj_code']+'_trials.csv')
trial_list = import_trials(trial_path)
print(trial_list)