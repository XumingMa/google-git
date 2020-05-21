#!/usr/bin/env python3

import os
import sys
import requests

url = "http://localhost/upload/"
work_dir = "./supplier-data/images/"
for parent, dirnames, filenames in os.walk(work_dir, followlinks=True):
    for filename in filenames:
        if len(filename.split(".")) == 2 and filename.split(".")[1] == "jpeg":
            with open(work_dir + filename, 'rb') as opened:
                r = requests.post(url, files={"file": opened})
                print(r.status_code)
