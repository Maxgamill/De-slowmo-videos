#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 22:38:48 2025

@author: Maxgamill

Quick little script to reduce the number of frames within slow-motion images.
"""

import cv2
import numpy as np
from pathlib import Path

# set input and output variables
base = Path("/Users/Maxgamill/Desktop/Tenerife_paragliding/TONI/")
in_file = base / "GX014093.MP4"
out_file = base / "GX014093_fast.mp4"
new_fps = 40

# load video file into cv2
cap = cv2.VideoCapture(in_file)

# extract image properties
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

print(f"Length: {length} \nWidth: {width} \nHeight: {height} \nFrames per Second: {fps}")

# obtain the ith frame index to keep i.e. 240/4 = 6 -> keep 1 in every 6 frames
ith_frame = np.round(fps / new_fps)

# set video writer codec
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # codec is system dependent, see cv2 documentation
out = cv2.VideoWriter(out_file, fourcc, new_fps, (width, height), True)
ret = True

# read input image frames, and only write the frame into the output file if it's
#   a multiple of the ith frame
i = 0
while ret:
    ret, img = cap.read() # read one frame from the 'capture' object; img is (H, W, C)
    if i % ith_frame == 0 and ret:
        out.write(img)
    i += 1

# release the files from cv2
out.release()
cap.release()
