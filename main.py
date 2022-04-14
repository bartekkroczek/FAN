#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import join
from yaml import load, Loader
from psychopy import visual, core, logging, event, gui
import csv
import codecs
from misc.screen import get_screen_res
import atexit
from problemGenerator.concrete_experiment import concrete_experiment

STIMULI_PATH = join('.', 'stimuli', 'all')
VISUAL_OFFSET = 150
TEXT_SIZE = 30
SCALE = 0.65
TRIGGER_LIST = []
RESULTS = [['choosed_option', 'ans_accept', 'rt', 'corr', 'time', 'rel', 'feedb', 'wait', 'exp', 'type']]


@atexit.register
def save_beh_results():
    with open(join('results', PART_ID + '_beh.csv'), 'w') as beh_file:
        beh_writer = csv.writer(beh_file)
        beh_writer.writerows(RESULTS)
    logging.flush()
    # with open(join('results', PART_ID + '_triggermap.txt'), 'w') as trigger_file:
    #     trigger_writer = csv.writer(trigger_file)
    #     trigger_writer.writerows(TRIGGER_LIST)


def read_text_from_file(file_name, insert=''):
    """
    Method that read message from text file, and optionally add some
    dynamically generated info.
    :param file_name: Name of file to read
    :param insert:
    :return: message
    """
    if not isinstance(file_name, str):
        logging.error('Problem with file reading, filename must be a string')
        raise TypeError('file_name must be a string')
    msg = list()
    with codecs.open(file_name, encoding='utf-8', mode='r') as data_file:
        for line in data_file:
            if not line.startswith('#'):  # if not commented line
                if line.startswith('<--insert-->'):
                    if insert:
                        msg.append(insert)
                else:
                    msg.append(line)
    return ''.join(msg)


def check_exit(key='f7'):
    stop = event.getKeys(keyList=[key])
    if len(stop) > 0:
        logging.critical('Experiment finished by user! {} pressed.'.format(key))
        exit(1)


def show_info(win, file_name, insert=''):
    """
    Clear way to show info message into screen.
    :type insert: text
    :param file_name: 
    :param win:
    :return:
    """
    msg = read_text_from_file(file_name, insert=insert)
    msg = visual.TextStim(win, color='black', text=msg, height=TEXT_SIZE - 5, wrapWidth=SCREEN_RES['width'])
    msg.draw()
    win.flip()
    key = event.waitKeys(keyList=['f7', 'return', 'space'])
    if key == ['f7']:
        abort_with_error('Experiment finished by user on info screen! F7 pressed.')
    win.flip()


def abort_with_error(err):
    logging.critical(err)
    raise Exception(err)


class StimulusCanvas(object):
    def __init__(self, win, figs_desc, scale=1.0, frame_color=u'crimson', pos=None):
        self._figures = list()
        self._frame = visual.Rect(win, width=390 * scale, height=390 * scale, lineColor=frame_color, lineWidth=5)
        inner_shift = 95 * scale
        shifts = [(-inner_shift, inner_shift), (inner_shift, inner_shift), (-inner_shift, -inner_shift),
                  (inner_shift, -inner_shift)]
        for fig_desc, inner_shift in zip(figs_desc, shifts):
            fig = "{figure}_{brightness}_{frame}_{rotation}.png".format(**fig_desc)
            fig = join(STIMULI_PATH, fig)
            fig = visual.ImageStim(win, fig, interpolate=True)
            fig.size = fig.size[0] * scale, fig.size[1] * scale
            fig.pos += inner_shift
            self._figures.append(fig)
        if pos:
            self.setPos(pos)

    def setFrameColor(self, color):
        self._frame.setLineColor(color)

    def setAutoDraw(self, draw):
        self._frame.setAutoDraw(draw)
        [x.setAutoDraw(draw) for x in self._figures]

    def draw(self):
        self._frame.draw()
        [x.draw() for x in self._figures]

    def setPos(self, pos):
        self._frame.pos += pos
        for fig in self._figures:
            fig.pos += pos


if __name__ == '__main__':
    info = {'Part_id': '', 'Part_age': '20', 'Part_sex': ['MALE', "FEMALE"],
            'ExpDate': '06.2016'}
    dictDlg = gui.DlgFromDict(dictionary=info, title='FAN', fixed=['ExpDate'])
    if not dictDlg.OK:
        exit(1)
    PART_ID = str(info['Part_id'] + info['Part_sex'] + info['Part_age'])
    logging.LogFile(join('results', PART_ID + '.log'), level=logging.INFO)

    concrete_experiment(join('problemGenerator', 'experiment.csv'), info['Part_id'], info['Part_sex'], info['Part_age'])
    data = load(open(join('results', PART_ID + '.yaml'), 'r'), Loader=Loader)
    SCREEN_RES = get_screen_res()
    print(SCREEN_RES)
    window = visual.Window(list(SCREEN_RES.values()), fullscr=False, units='pix', screen=0, color='Gainsboro')

    to_label = visual.TextStim(window, text=u'To:', color=u'black', height=50, pos=(
        -SCREEN_RES['width'] / 2.0 + VISUAL_OFFSET, SCREEN_RES['height'] / 1.96 - SCREEN_RES['height'] / 3.0))
    is_like_label = visual.TextStim(window, text=u'Is Like:', color=u'black', height=50, pos=(
        -SCREEN_RES['width'] / 2.0 + VISUAL_OFFSET, SCREEN_RES['height'] / 2.02 - 2 * SCREEN_RES['height'] / 3.0))
    line = visual.Line(window, start=(-SCREEN_RES['width'] / 3.8, -550), end=(-SCREEN_RES['width'] / 3.8, 550),
                       lineColor=u'black', lineWidth=10)
    to_choose_one_label = visual.TextStim(window, text=u'To: (Choose one)', color=u'black', height=50,
                                          wrapWidth=1500,
                                          pos=(50, 2.7 * SCREEN_RES['height'] / 7.0))
    time_left_label = visual.TextStim(window, text=u'16 seconds left.', height=50, color=u'black',
                                      wrapWidth=1000,
                                      pos=(-1.5 * SCREEN_RES['width'] / 13.0, -3 * SCREEN_RES['height'] / 7.0))
    accept_box = visual.Rect(window, fillColor=u'dimgray', width=600, height=100,
                             pos=(4.6 * SCREEN_RES['width'] / 13.0, -3 * SCREEN_RES['height'] / 7.0 - 40),
                             lineColor=u'black')
    accept_label = visual.TextStim(window, text=u'Accept answer', height=50, color=u'ghostwhite', wrapWidth=900,
                                   pos=(
                                       4.6 * SCREEN_RES['width'] / 13.0, -2.8 * SCREEN_RES['height'] / 7.0 - 60))
    LABELS = [to_label, is_like_label, line, to_choose_one_label, time_left_label, accept_box, accept_label]
    for block in data['list_of_blocks']:
        # TODO: ADD break support
        for trial in block['experiment_elements']:
            if trial['type'] == 'instruction':
                show_info(window, join('.', 'messages', trial['path']))
                continue
            [lab.setAutoDraw(True) for lab in LABELS]
            A = StimulusCanvas(win=window, figs_desc=trial['matrix_info'][0]['parameters'], scale=SCALE,
                               frame_color=u'black', pos=(
                    -SCREEN_RES['width'] / 2.0 + VISUAL_OFFSET, SCREEN_RES['height'] / 2.0 - VISUAL_OFFSET))
            B = StimulusCanvas(win=window, figs_desc=trial['matrix_info'][1]['parameters'], scale=SCALE,
                               frame_color=u'black', pos=(-SCREEN_RES['width'] / 2.0 + VISUAL_OFFSET,
                                                          SCREEN_RES['height'] / 2.05 - VISUAL_OFFSET - SCREEN_RES[
                                                              'height'] / 3.0))
            C = StimulusCanvas(win=window, figs_desc=trial['matrix_info'][2]['parameters'], scale=SCALE,
                               frame_color=u'black', pos=(-SCREEN_RES['width'] / 2.0 + VISUAL_OFFSET,
                                                          SCREEN_RES['height'] / 2.1 - VISUAL_OFFSET - 2 * SCREEN_RES[
                                                              'height'] / 3.0))
            figures = [A, B, C]
            solutions = [
                StimulusCanvas(window, trial['matrix_info'][i]['parameters'], scale=SCALE, frame_color=u'dimgray') for i
                in range(3, 9)]
            [print(f"{i}:{trial['matrix_info'][i]['parameters']}") for i in range(3, 9)]
                # TODO: Relacje sie gybia??? 4
            [solution.setPos((150, 0)) for solution in solutions]

            shifts = [(-SCREEN_RES['width'] / 4.0, SCREEN_RES['height'] / 6.0), (0, SCREEN_RES['height'] / 6.0),
                      (SCREEN_RES['width'] / 4.0, SCREEN_RES['height'] / 6.0),
                      (-SCREEN_RES['width'] / 4.0, -SCREEN_RES['height'] / 6.0), (0, -SCREEN_RES['height'] / 6.0),
                      (SCREEN_RES['width'] / 4.0, -SCREEN_RES['height'] / 6.0)]
            for solution, shift in zip(solutions, shifts):
                solution.setPos(shift)
            figures.extend(solutions)
            timer = core.CountdownTimer(trial['time'])
            [fig.setAutoDraw(True) for fig in figures]
            mouse = event.Mouse()
            choosed_option = -1
            ans_accept = False
            rt = -1
            while timer.getTime() > 0.0 and not ans_accept:
                for idx, sol in enumerate(solutions, 3):
                    if mouse.isPressedIn(accept_box) and choosed_option != -1:
                        ans_accept = True
                        rt = trial['time'] - timer.getTime()
                        break
                    if mouse.isPressedIn(sol._frame):
                        sol.setFrameColor('green')
                        choosed_option = idx
                    if choosed_option != idx:
                        if sol._frame.contains(mouse):
                            sol.setFrameColor('yellow')
                        else:
                            sol.setFrameColor('gray')
                time_left_label.setText(u'{} seconds left.'.format(int(timer.getTime())))
                window.flip()
                check_exit()
            if choosed_option != -1:
                choosed_option = trial['matrix_info'][choosed_option]['name']
            corr = choosed_option == 'D1'
            RESULTS.append([choosed_option, ans_accept, rt, corr, trial['time'], trial['rel'], trial['feedb'],
                            trial['wait'], trial['exp'], trial['type']])
            [fig.setAutoDraw(False) for fig in figures]
            [lab.setAutoDraw(False) for lab in LABELS]
    save_beh_results()
    logging.flush()
    show_info(window, join('.', 'messages', 'end.txt'))
window.close()
