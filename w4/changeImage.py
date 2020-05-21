#!/usr/bin/env python3

from PIL import Image
import os
import sys

work_dir = "./supplier-data/images/"
for parent, dirnames, filenames in os.walk(work_dir, followlinks=True):
    for filename in filenames:
        if len(filename.split(".")) == 2:
            img = Image.open(work_dir + filename)
            img = img.resize((600, 400))
            img = img.convert("RGB")
            img.save(work_dir+filename.split(".")[0]+".jpeg", format="JPEG")
