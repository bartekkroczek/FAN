import colormath
from colormath iport color_objects
from colormath import color_objects

# Definiuje kolory z kodów hex
ghost_white = color_objects.AdobeRGBColor.new_from_rgb_hex("#F8F8FF")
white_smoke = color_objects.AdobeRGBColor.new_from_rgb_hex("#F5F5F5")
light_grey = color_objects.AdobeRGBColor.new_from_rgb_hex("#D3D3D3")
dimgrey = color_objects.AdobeRGBColor.new_from_rgb_hex("#696969")
gainsboro = color_objects.AdobeRGBColor.new_from_rgb_hex("#DCDCDC")
darkgrey = color_objects.AdobeRGBColor.new_from_rgb_hex("#A9A9A9")
gray = color_objects.AdobeRGBColor.new_from_rgb_hex("#808080")
slategray = color_objects.AdobeRGBColor.new_from_rgb_hex("#708090")
silver = color_objects.AdobeRGBColor.new_from_rgb_hex("#C0C0C0")
black = color_objects.AdobeRGBColor.new_from_rgb_hex("#000000")

#Tworzę listę kolorów
color_names = [_ for _ in dir() if not _.startswith('_')][2:]
import pandas as pd
color_names.remove('quit')
color_names.remove('color_object')
color_names.remove('color_objects')
color_names.remove('colormath')
color_names.remove('get_ipython')
color_names.remove('exit')
df = pd.DataFrame(index=color_names, columns=color_names)
from colormath.color_diff import delta_e_cie1976
delta_e_cie1976(white, black)
delta_e_cie1976(white, black)
from colormath.color_conversions import convert_color
from colormath.color_objects import LabColor

#Zmieniam format kolorów
a = [('{} = convert_color({}, LabColor)'.format(x, x)) for x in color_names]

for _ in a:
    exec(_)
white
#liczę odległość
from colormath.color_diff import delta_e_cie1994
delta_e_cie1994(black, white)
for c1 in color_names:
    for c2 in color_names:
        df[c1][c2] = delta_e_cie1994(eval(c1), eval(c2))

ls
cd PycharmProjects/
ls
cd test_analogii/
ls
cd colors_diff/
df.to_excel('color_difs.xlsx')
