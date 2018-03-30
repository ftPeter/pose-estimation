
import cv2
import cv2.aruco as aruco

marker_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)

square=0.0355
marker=0.0270
board = aruco.CharucoBoard_create(5,7,square,marker,marker_dict)
charuco_img = board.draw((200*5,200*7))
filename_str = "CHARUCO_DICT_5_7_{}_{}_6X6_250.jpg".format(square,marker)
cv2.imwrite( filename_str, charuco_img )

