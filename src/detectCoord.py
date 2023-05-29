#!/usr/bin/env python
"""
@file detectCoord.py
@brief Este codigo recive una imagen, detecta un objeto verde y obtiene sus cordenadas estas para publicarlas en un ros topic multiplicadas por cien.
"""
import cv2
import numpy as np
import ctypes
import rospy
from std_msgs.msg import Float64MultiArray
from ctypes import *

class greenDetector:
    """
    @brief Clase greenDetector para procesamiento de video y publicación de coordenadas.
    """

    def __init__(self):
        """
        @brief Inicializador de la clase greenDetector.
        """
        self.pub = rospy.Publisher('coord', Float64MultiArray, queue_size=10)
        libname = "/home/robotics/catkin_ws/src/Act_M4/lib/libmulti.so"
        self.mylib = ctypes.CDLL(libname)
        self.funct = self.mylib.multi
        self.funct.restype = ctypes.POINTER(ctypes.c_int)

    def video(self):
        """
        @brief Método para capturar y procesar el video.
        """
        while(True):
            img = cv2.imread("imagen.jpg", cv2.IMREAD_COLOR)
            mean = 0
            stddev = 50
            noise = np.zeros(img.shape, np.uint8)
            cv2.randn(noise, mean, stddev)
            noisy_img = cv2.add(img, noise)
            hsv = cv2.cvtColor(noisy_img, cv2.COLOR_BGR2HSV)
            low = np.array([50, 100, 100])
            up = np.array([80,255,255])
            greenMask = cv2.inRange(hsv, low, up)
            res = cv2.bitwise_and(noisy_img, noisy_img, mask=greenMask)
            invert = cv2.bitwise_not(greenMask)
            ret, thG = cv2.threshold(invert, 120, 255, cv2.THRESH_TOZERO)
            c, h = cv2.findContours(greenMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]
            threshold_blob_area = 1000
            for i in range(1, len(c)):
                index_level = int(h[0][i][1])
                if index_level <= i:
                    cnt = c[i]
                    area = cv2.contourArea(cnt)
            if(area) <= threshold_blob_area:
                cv2.drawContours(greenMask, [cnt], -1, 0, -1, 1)
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
            contour = cv2.morphologyEx(greenMask, cv2.MORPH_OPEN, kernel, iterations=4)
            x,y,w,h = cv2.boundingRect(contour)
            cv2.rectangle(noisy_img, (x, y), (x + w, y + h), (139,0,0), 4)
            cv2.putText(noisy_img, "x: "+str(x), (x, y+h+25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,255), 2, cv2.LINE_AA)
            cv2.putText(noisy_img, "y: "+str(y), (x+130, y+h+25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,255), 2, cv2.LINE_AA)
            ret_ptr = self.funct(ctypes.c_int(x), ctypes.c_int(y))
            ret_arr = ret_ptr[:2]
            timestamp = rospy.Time.now()
            msg = Float64MultiArray()
            msg.data = [float(ret_arr[0]), float(ret_arr[1]), float(timestamp.to_sec())]
            print(msg.data)
            self.pub.publish(msg)
            self.mylib.delete_arr.argtypes = [ctypes.POINTER(ctypes.c_int)]
            self.mylib.delete_arr.restype = None
            self.mylib.delete_arr(ret_ptr)
            cv2.imshow('noisy_img', noisy_img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cv2.destroyAllWindows()    

if __name__ == '__main__':
    m = greenDetector()
    rospy.init_node('greenDetector', anonymous=True)
    m.video()
    try:
        while not rospy.is_shutdown():
            rospy.Rate(100)
    except KeyboardInterrupt:
        print("Shutting down")