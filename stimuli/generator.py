from lxml import etree
from os import listdir
from os.path import join

width = "150.0pt"
height = "150.0pt"
stroke_color = "black"
colors = ["ghostwhite", "lightgrey", "dimgrey"]
stroke_widths = ["10", "30", "60"]
color_names = dict(white="white", ghostwhite="white", lightgrey="gray", dimgrey='slate')
stroke_names = {'10': "thin",'30':"narrow", '60':'wide'} 
all_possible_options = [(color, stroke) for color in colors for stroke in stroke_widths]
filenames = listdir('org')

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

        res_file_name = filename[3:5].split('.')[0] +"_" + color_names[color] + "_" + stroke_names[stroke] + "_0.svg"
        with open(join('all', res_file_name), 'w') as res_file:
            res_file.write(etree.tostring(tree, pretty_print = True))
