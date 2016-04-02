from psychopy import visual, core, event
import yaml
from screen_misc import get_frame_rate, get_screen_res
from os import path







if __name__ == '__main__':
    data = yaml.load(open('TestM24.yaml', 'r'))
    prob_no = 1
    data = data['list_of_blocks'][0]['experiment_elements'][prob_no]['matrix_info']
    SCREEN_RES = get_screen_res()
    window = visual.Window(SCREEN_RES.values(), fullscr=True, monitor='TestMonitor',
                           units='pix', screen=0, color='Gainsboro')

    box = data[0]['parameters']
    print box[0]
    first_fig = "{figure}_{brightness}_{frame}_{rotation}.png".format(**box[0])
    sec_fig = "{figure}_{brightness}_{frame}_{rotation}.png".format(**box[1])
    third_fig = "{figure}_{brightness}_{frame}_{rotation}.png".format(**box[2])
    forth_fig = "{figure}_{brightness}_{frame}_{rotation}.png".format(**box[3])
    first_fig = path.join('stimuli', 'all', first_fig)
    first_fig = visual.ImageStim(window, first_fig)
    first_fig.setAutoDraw(True)
    window.flip()
    core.wait(3)

