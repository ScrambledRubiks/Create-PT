from PIL import Image
import os
import gc
from Setup import debug
import copy
count = -1
dataset = []

class m_import:
    imageW = 0
    imageH = 0
    
    def initData(folder):
        global count
        global imageW
        global imageH
        global dataset
        dir_path = r"datasets\sets_" + folder
        for path in os.listdir(dir_path):
            if os.path.isfile(os.path.join(dir_path,  path)):
                count += 1

                im = Image.open(rf'datasets\sets_{folder}\{folder}{count}.png')
                imageSizeW, imageSizeH = im.size
                imageW = copy.copy(imageSizeW)
                imageH = copy.copy(imageSizeH)
                globals()[folder + str(count)] = []

                for i in range(imageSizeW):
                    for j in range(imageSizeH):
                        pixVal = im.getpixel((j, i))
                        if pixVal == (0, 0, 0, 255):
                            globals()[folder + str(count)].append(1)
                        else:
                            globals()[folder + str(count)].append(0)
        count = -1
        return [imageW, imageH]

    def getData(folder, value):
        dataset = globals()[folder + str(value)]
        return dataset
