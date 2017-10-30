
all: pose

generate-board:
	python3 generate_aruco_tags.py

calibrate:
	opencv_interactive-calibration -h=7 -w=5 --sz=.032 --t=charuco

pose-board:
	python3 charuco_pose.py

pose-aruco:
	python3 aruco_pose.py

