import PIL
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from random import *


img2 = mpimg.imread('input4.png')
imgplot2 = plt.imshow(img2)
plt.show()

def rnd():
    r = randint(1, 225)
    g = randint(1, 225)
    b = randint(1, 225)
    resault = (r, g, b)
    return resault

from random import *
for i in range(20):
    for j in range(20):
        print(rnd())
        pix3[i, j] = rnd()
        
image3.save('test.png')


img2 = mpimg.imread('test.png')
imgplot2 = plt.imshow(img2)
plt.show()
