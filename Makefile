
all: pose

generate-board:
	python3 generate_aruco_tags.py

calibrate:
	opencv_interactive-calibration -h=7 -w=5 --sz=.032 --t=charuco

# The Aruco Tag Board attached to the USPS box
# that was used for the February 2018 series of
# calibrations had black box edge of 0.036
calibrate-mailbox:
	opencv_interactive-calibration -h=7 -w=5 --sz=.036 --t=charuco

# The Aruco Tag Board attached to the chipboard in my office
# that was used for the February 2018 series of
# calibrations had black box edge of 0.0345
calibrate-chipboard:
	opencv_interactive-calibration -h=7 -w=5 --sz=.0345 --t=charuco


pose-charuco:
	python3 charuco_pose.py

pose-aruco-board:
	python3 aruco-calibration/aruco_board_pose.py

pose-aruco:
	python3 aruco-calibration/aruco_pose.py

