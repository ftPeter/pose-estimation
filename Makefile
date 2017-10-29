
all: pose

calibrate:
	opencv_interactive-calibration -h=7 -w=5 --sz=.032 --t=charuco

pose:
	python3 charuco_pose.py
