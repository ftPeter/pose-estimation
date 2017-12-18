import cv2
import cv2.aruco as aruco

marker_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)

for i in range( 41, 100 ):
    marker_img = marker_dict.drawMarker(i, 100)
    filename_str = "ARUCO_DICT_6X6_250/ARUCO_DICT_6X6_250_ID_" + str(i) + ".jpg"
    cv2.imwrite( filename_str, marker_img )

