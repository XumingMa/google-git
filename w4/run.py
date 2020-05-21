#!/usr/bin/env python3

import os
import sys
import requests

url = "http://localhost/fruits/"
work_dir = "./supplier-data/descriptions/"

for parent, dirnames, filenames in os.walk(work_dir, followlinks=True):
    for filename in filenames:
        with open(work_dir + filename, encoding="utf-8") as f:
            lines = f.readlines()
                
            dic = {"name": lines[0].rstrip('\n'), "weight":lines[1].split(" ")[0], "description": lines[2].rstrip('\n'), "image_name": filename.split(".")[0]+".jpeg"}
            r = requests.post(url, data=dic)
            print(r.status_code)
