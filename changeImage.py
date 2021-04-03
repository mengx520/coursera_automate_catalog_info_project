#!/usr/bin/env python3
import os, sys
from PIL import Image

dir = os.listdir('/home/student-01-536256626c85/supplier-data/images/')

for ogpic in dir:
  if 'tiff' in ogpic:
    # only select file name without .tiff
    pic_name = ogpic.split('.')[0]
    file_path = '/home/student-01-536256626c85/supplier-data/images/' + pic_name + '.jpeg'
    im = Image.open('/home/student-01-536256626c85/supplier-data/images/' + ogpic)
    im.convert('RGB').resize((600,400)).save(file_path,'JPEG' )