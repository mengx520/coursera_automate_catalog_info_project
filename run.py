#! /usr/bin/env python3
import os, sys
import requests
import json


''' automatically POST the fruit images and their respective description in JSON format.'''

path = "/home/student-01-536256626c85/supplier-data/descriptions/"
pic_dir = os.listdir(path)

for txt in pic_dir:
    if '.txt' in txt:
        with open(path + txt, 'r') as f:
            fruit = txt.split('.')[0]
            data = f.read()
            data = data.split('\n')
            # creating fruit dictionary weight needs to be int
            dict = {'name': data[0], 'weight':int(data[1].strip(' lbs')), 'description': data[2], 'image_name': fruit + '.jpeg'}
            # use post method from Python requests library to upload all the data 
            req = requests.post("http://localhost/fruits/", json=dict)
            req.raise_for_status()
            print(req.status_code)



