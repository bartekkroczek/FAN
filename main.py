#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path

import yaml
from psychopy import visual, core

from misc.screen import get_screen_res

STIMULI_PATH = path.join('.', 'stimuli', 'all')
ABSOLUT_SHIFT = 90


class StimulusCanvas(object):
    def __init__(self, win, figs_desc, scale=1.0, frame_color=u'crimson'):
        self.figures = list()
        self.frame = visual.Rect(win, width=375 * scale, height=375 * scale, lineColor=frame_color, lineWidth=5)
        shift = ABSOLUT_SHIFT * scale
        shifts = [(-shift, shift), (shift, shift), (-shift, -shift), (shift, -shift)]
        for fig_desc, shift in zip(figs_desc, shifts):
            fig_desc['figure'] += 1
            fig = "{figure}_{brightness}_{frame}_{rotation}.png".format(**fig_desc)
            fig = path.join(STIMULI_PATH, fig)
            fig = visual.ImageStim(win, fig, interpolate=True)
            fig.size = fig.size[0] * scale, fig.size[1] * scale
            fig.pos += shift
            self.figures.append(fig)

    def setAutoDraw(self, draw):
        self.frame.setAutoDraw(draw)
        [x.setAutoDraw(draw) for x in self.figures]

    def draw(self):
        self.frame.draw()
        [x.draw() for x in self.figures]

    def setPos(self, pos):
        self.frame.pos += pos
        for fig in self.figures:
            fig.pos += pos


if __name__ == '__main__':
    data = yaml.load(open('TestM41.yaml', 'r'))
    prob_no = 2
    data = data['list_of_blocks'][0]['experiment_elements'][prob_no]['matrix_info']
    SCREEN_RES = get_screen_res()
    window = visual.Window(SCREEN_RES.values(), fullscr=True, monitor='TestMonitor',
                           units='pix', screen=0, color='Gainsboro')

    # data[1]['parameters'][2], data[1]['parameters'][3] = data[1]['parameters'][3], data[1]['parameters'][2]
    # for i in range(3, 9):
    #     data[i]['parameters'][0], data[i]['parameters'][1] = data[i]['parameters'][1], data[i]['parameters'][0]

    print data[0]['parameters']
    A = StimulusCanvas(win=window, figs_desc=data[0]['parameters'], scale=0.8, frame_color=u'black')
    B = StimulusCanvas(win=window, figs_desc=data[1]['parameters'], scale=0.8, frame_color=u'black')
    C = StimulusCanvas(win=window, figs_desc=data[2]['parameters'], scale=0.8, frame_color=u'black')
    shift = 170
    A.setPos((-SCREEN_RES['width'] / 2.0 + shift, SCREEN_RES['height'] / 2.0 - shift))
    A.setAutoDraw(True)
    B.setPos((-SCREEN_RES['width'] / 2.0 + shift, SCREEN_RES['height'] / 2.0 - shift - SCREEN_RES['height'] / 3.0))
    B.setAutoDraw(True)
    C.setPos((-SCREEN_RES['width'] / 2.0 + shift, SCREEN_RES['height'] / 2.0 - shift - 2 * SCREEN_RES['height'] / 3.0))
    C.setAutoDraw(True)
    ma_sie_do = visual.TextStim(window, text=u'To:', color=u'black', height=50,
                                pos=(-SCREEN_RES['width'] / 2.0 + shift,
                                     SCREEN_RES['height'] / 2.0 + 0.07 * shift - SCREEN_RES['height'] / 3.0))
    ma_sie_do.setAutoDraw(True)
    tak_jak = visual.TextStim(window, text=u'Is Like:', color=u'black', height=50,
                              pos=(-SCREEN_RES['width'] / 2.0 + shift,
                                   SCREEN_RES['height'] / 2.0 + 0.07 * shift - 2 * SCREEN_RES['height'] / 3.0))
    tak_jak.setAutoDraw(True)
    line = visual.Line(window, start=(-600, -550), end=(-600, 550), lineColor=u'black', lineWidth=10)
    line.setAutoDraw(True)

    solutions = [StimulusCanvas(window, data[i]['parameters'], scale=0.8, frame_color=u'dimgray') for i in range(3, 9)]
    solutions[3].frame.setLineColor(u'green')
    [solution.setPos((150, 0)) for solution in solutions]

    shifts = [(-SCREEN_RES['width']/4.0, SCREEN_RES['height'] / 6.0), (0, SCREEN_RES['height'] / 6.0), (SCREEN_RES['width']/4.0, SCREEN_RES['height'] / 6.0),
              (-SCREEN_RES['width']/4.0, -SCREEN_RES['height'] / 6.0), (0, -SCREEN_RES['height'] / 6.0), (SCREEN_RES['width']/4.0, -SCREEN_RES['height'] / 6.0)]
    for solution, shift in zip(solutions, shifts):
        solution.setPos(shift)
    [solution.setAutoDraw(True) for solution in solutions]

    ma_sie_do2 = visual.TextStim(window, text=u'To: (Choose one)', color=u'black', height=50, wrapWidth=1500,
                                pos=(50, 2.7 * SCREEN_RES['height'] / 7.0))
    ma_sie_do2.setAutoDraw(True)
    pozostalo_ci = visual.TextStim(window, text=u'16 seconds left.', height=50, color=u'black', wrapWidth=1000,
                                   pos=(-1.5*SCREEN_RES['width']/13.0, -3 * SCREEN_RES['height']/7.0))
    pozostalo_ci.setAutoDraw(True)
    zatwierdz_box = visual.Rect(window, fillColor=u'dimgray', width=600, height=100, pos=(4.5 * SCREEN_RES['width']/13.0, -3 * SCREEN_RES['height']/7.0 - 40), lineColor=u'black')
    zatwierdz_box.setAutoDraw(True)
    zatwierdz = visual.TextStim(window, text=u'Accept answer', height=50, color=u'ghostwhite', wrapWidth=900,
                                pos = (4.5 * SCREEN_RES['width']/13.0, -3 * SCREEN_RES['height']/7.0 - 40))
    zatwierdz.setAutoDraw(True)
    window.flip()
    core.wait(8)
