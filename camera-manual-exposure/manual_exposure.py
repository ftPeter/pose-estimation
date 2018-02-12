#!/usr/bin/python3 
import cv2 
import subprocess

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-e", "--exposure", type=int, default=10,
                            help="exposure in 100 us units (default 10)")
args = parser.parse_args()
print(args)

cap = cv2.VideoCapture(0) 
command = "v4l2-ctl -d 0 -c auto_exposure=1 -c exposure_time_absolute={}".format(args.exposure)
output = subprocess.call(command, shell=True)
while(True): 
  ret, frame = cap.read() 
  cv2.imshow('frame', frame) 
  if( cv2.waitKey(1) & 0xFF == ord('q') ): 
    break 
cap.release() 
cv2.destroyAllWindows()
