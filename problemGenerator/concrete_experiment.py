import csv

from .classes.experiment import Experiment
from .classes.block import Block
from .classes.trial import Trial
from .classes.parameters import Trial_type, Instruction_type, Per
from .classes.instruction import Instruction

__author__ = 'ociepkam'


def load_csv(filename):
    experiment = []
    number_of_blocks = 0
    with open(filename, 'r') as f:
        spamreader = csv.reader(f)
        head = []
        for row_idx, row in enumerate(spamreader):
            if row_idx == 0:
                head = row
            else:
                trial = {}
                for column_idx, column in enumerate(row):
                    if column_idx == 13:
                        break
                    try:
                        trial.update({str(head[column_idx]): int(column)})
                    except:
                        trial.update({str(head[column_idx]): str(column)})
                if trial["BLOCK_NUMBER"] > number_of_blocks and trial["BLOCK_NUMBER"] is not "":
                    number_of_blocks = trial["BLOCK_NUMBER"]
                if trial['BLOCK_NUMBER'] is not "":
                    experiment.append(trial)
    return number_of_blocks, experiment


def concrete_experiment(filename, id, sex, age, randomize=True):
    number_of_blocks, data = load_csv(filename)

    experiment = Experiment([], id, sex, age)
    for idx in range(number_of_blocks):
        block = Block([])
        experiment.list_of_blocks.append(block)

    for idx in range(len(data)):
        trial_info = data[idx]
        block_number = trial_info['BLOCK_NUMBER']
        if trial_info['TYPE'] == Trial_type.instruction:
            if trial_info['TIP'][-3:] == 'txt':
                instruction_type = Instruction_type.text
            elif trial_info['TIP'][-3:] == 'bmp' or trial_info['TIP'][-3:] == 'jpg':
                instruction_type = Instruction_type.image
            else:
                raise AssertionError("wrong instruction file type")
            trial = Instruction(trial_info['TIP'], instruction_type, trial_info['SHOW_TIME'])
        elif trial_info['TYPE'] == Trial_type.training or trial_info['TYPE'] == Trial_type.experiment:
            trial = Trial(time=trial_info['SHOW_TIME'], per=Per.small, rel=trial_info['RELATIONS'],
                          feedb=trial_info['FEEDB'], wait=trial_info['WAIT_TIME'], exp=trial_info['TYPE'],
                          tip=trial_info.get('TIP'), tip_time=trial_info['TIP_TIME'], answers=eval(trial_info['ANSWERS']))
        else:
            raise AssertionError("wrong trial type")

        experiment.list_of_blocks[block_number - 1].list_of_experiment_elements.append(trial)

    if randomize:
        experiment.randomize()
    experiment.save()
