from lxml import etree
from os import listdir
from os.path import join

width = "130.0pt"
height = "130.0pt"
stroke_color = "black"
colors = ["ghostwhite", "lightgrey", "dimgrey"]
stroke_widths = ["8", "16", "32"]


all_possible_options = [(color, stroke) for color in colors for stroke in stroke_widths]
filenames = [listdir('org')[0]]

for filename in filenames:
    tree = etree.parse(open(join('org', filename), 'r'))
    for color, stroke in all_possible_options:
        for element in tree.iter():
            curr_tag =  element.tag.split("}")[1]
            if curr_tag == "svg":
                element.set("width", width)
                element.set("height", height)
            elif curr_tag == "g":
                element.set("fill", color)
                element.set("stroke", stroke_color)
                element.set("stroke-width", stroke)

        res_file_name = "fig:" + filename[3:5].split('.')[0] + "_color:" + color + "_stroke:" + stroke + ".svg"
        with open(join('all', res_file_name), 'w') as res_file:
            res_file.write(etree.tostring(tree, pretty_print = True))
