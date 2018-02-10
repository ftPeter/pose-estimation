# I was having issues with blurry images
# disrupting the tag identification.
#
# These commands are testings the capability
# of the camera to operate in shutter-priority
# mode above 1/60th of a second to stop the motion
#
# French currently has 8MP Sony RPi V2 Camera

all: test shutter-priority-60th shutter-priority-125th shutter-priority-250th

FILENAME-BASE=cam-$(shell hostname)
test:
	raspistill -o $(FILENAME-BASE)-exposure-automatic.jpg

shutter-priority-60th:
	raspistill -ss 16666.7  -o $(FILENAME-BASE)-exposure-60th.jpg

shutter-priority-125th:
	raspistill -ss 8000 -o $(FILENAME-BASE)-exposure-125th.jpg

shutter-priority-250th:
	raspistill -ss 4000 -o $(FILENAME-BASE)-exposure-250th.jpg


