#!/usr/bin/env python3
import requests
import os, sys

# takes the jpeg images from the supplier-data/images directory 
#  uploads them to the web server fruit catalog

url = "http://localhost/upload/"

path = "/home/student-01-536256626c85/supplier-data/images/"
pic_dir = os.listdir(path)

for pic in pic_dir:
    if '.jpeg' in pic:
        with open(path + pic, 'rb') as opened:
            r = requests.post(url, files={'file': opened})