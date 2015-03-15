import os
import sys
import subprocess
import matplotlib
matplotlib.use('Agg')
import numpy as np
from skimage import io
from skimage.util import img_as_ubyte
from skimage.morphology import black_tophat, white_tophat, disk

fi = "/data/Kaggle-National_Data_Science_Bowl/Data/test/"
fo = "/data/Kaggle-National_Data_Science_Bowl/Data_morph/test/"

cmd = " -resize 64x64 -gravity center -background white -extent 64x64 PNG24:"

try:
    os.mkdir(fo)
except:
    pass

selem = disk(1)

imgs = os.listdir(fi)
#print imgs
for img in imgs:

    img_orig = img_as_ubyte(io.imread(fi + img, as_grey=True))
    img_btop = 255-black_tophat(img_orig, selem)
    img_wtop = 255-white_tophat(img_orig, selem)

    img_out = np.zeros((img_orig.shape[0], img_orig.shape[1], 3), dtype=np.uint8)
    img_out[:, :, 0] = img_orig
    img_out[:, :, 1] = img_btop
    img_out[:, :, 2] = img_wtop

    io.imsave("/dev/shm/test_tmp.png", img_out)

    md = "convert /dev/shm/test_tmp.png" + cmd
    md += fo + img + ".png"
    os.system(md)

