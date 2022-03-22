# ascii image renderer

from PIL import Image
import numpy as np
import pathlib

# light to dark ascii characters for brightness
monochrome_ascii = [' ', '.', ':', '=', '+', '*', '#', '%', '@']

# be careful when adjusting w and h the aspect ratio needs to be 2 (since notepad text is around 2:1 w:h)
def im_to_array(path = None, img = [] , w=200, h=100):
    if path != None:
        with Image.open(path) as path_im:
            path_im = path_im.convert('L')
            path_im = path_im.resize((w, h))
            im_data = np.array(path_im)
            return im_data

    elif img != []:
        img = img.convert('L')
        img = img.resize((w, h))
        im_data = np.array(img)

        return im_data



# based on brightness of pixels 0-255 creates an array with an ascii characters
def ascii_array(path):
    im_data = im_to_array(path)

    ascii_matrix = []

    for im_row in im_data:

        cur_ascii_row = []
        for cur_brightness in im_row:

            if 0 <= cur_brightness <= 27:
                cur_ascii_row.append(monochrome_ascii[8])
            elif 28 <= cur_brightness <= 55:
                cur_ascii_row.append(monochrome_ascii[7])
            elif 56 <= cur_brightness <= 83:
                cur_ascii_row.append(monochrome_ascii[6])
            elif 84 <= cur_brightness <= 111:
                cur_ascii_row.append(monochrome_ascii[5])
            elif 112 <= cur_brightness <= 139:
                cur_ascii_row.append(monochrome_ascii[4])
            elif 140 <= cur_brightness <= 167:
                cur_ascii_row.append(monochrome_ascii[3])
            elif 168 <= cur_brightness <= 195:
                cur_ascii_row.append(monochrome_ascii[2])
            elif 196 <= cur_brightness <= 223:
                cur_ascii_row.append(monochrome_ascii[1])
            elif 224 <= cur_brightness <= 255:
                cur_ascii_row.append(monochrome_ascii[0])

        ascii_matrix.append(cur_ascii_row)

    return ascii_matrix

# turns brightness matrix into ascii string for the textfile directly
def ascii_str(path = None, img = [], w=200, h=100):
    if path != None:
        im_data = im_to_array(path=path, w=w, h=h)
    elif img != []:
        im_data = img

    ascii_str = ''

    for im_row in im_data:

        for cur_brightness in im_row:

            if 0 <= cur_brightness <= 27:
                ascii_str += monochrome_ascii[8]
            elif 28 <= cur_brightness <= 55:
                ascii_str += monochrome_ascii[7]
            elif 56 <= cur_brightness <= 83:
                ascii_str += monochrome_ascii[6]
            elif 84 <= cur_brightness <= 111:
                ascii_str += monochrome_ascii[5]
            elif 112 <= cur_brightness <= 139:
                ascii_str += monochrome_ascii[4]
            elif 140 <= cur_brightness <= 167:
                ascii_str += monochrome_ascii[3]
            elif 168 <= cur_brightness <= 195:
                ascii_str += monochrome_ascii[2]
            elif 196 <= cur_brightness <= 223:
                ascii_str += monochrome_ascii[1]
            elif 224 <= cur_brightness <= 255:
                ascii_str += monochrome_ascii[0]

        ascii_str += '\n'

    ascii_str.rstrip('\n')

    return ascii_str

# turns ascii arrays data into strings
# dont use this if u only care about the final ascii txt image use ascii_str
def ascii_arr_tostr(ascii_array):
    ascii_s = ''

    for ascii_row in ascii_array:
        for ascii_ch in ascii_row:
            ascii_s += ascii_ch
        ascii_s += '\n'

    return ascii_s


# void saves ascii strings into a txt file in the current directory named saveas or pathname.txt if saveas is not specified
def im_to_ascii(pathname, w=200, h=100):

    saveas = pathlib.Path(pathname).stem + '.txt'


    ascii_data = ascii_str(path=pathname, w=w, h=h)

    ascii_txt = open(saveas, 'w')
    ascii_txt.write(ascii_data)
    ascii_txt.close()

#im_to_ascii('images\\nenechandayo.jfif', w=50, h=25)
