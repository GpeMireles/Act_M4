#!/usr/bin/env python
# Detect green object through webcam and print coordinates

# Libraries
import cv2
import numpy as np
import ctypes
import rospy
from std_msgs.msg import Float64MultiArray
from ctypes import *

class m4_t1:

  def __init__(self):
    # Publish of coord*100
    self.pub = rospy.Publisher('coord', Float64MultiArray, queue_size=10)

    # Cpp library
    libname = "/home/robotics/catkin_ws/src/Act_M4/lib/libmulti.so"
    self.mylib = ctypes.CDLL(libname)
    self.funct = self.mylib.multi
    self.funct.restype = ctypes.POINTER(ctypes.c_int)

  def video(self):
    # Define a video capture object
    while(True):
          
        # Capture the video
        img = cv2.imread("imagen.jpg", cv2.IMREAD_COLOR)

        # Generate random Gaussian noise
        mean = 0
        stddev = 50
        noise = np.zeros(img.shape, np.uint8)
        cv2.randn(noise, mean, stddev)

        # Add noise to image
        noisy_img = cv2.add(img, noise)

        # Convert the BGR image to HSV colour space
        hsv = cv2.cvtColor(noisy_img, cv2.COLOR_BGR2HSV)

        # Set the lower and upper bounds for the green hue
        low = np.array([50, 100, 100])
        up = np.array([80,255,255])

        # Create mask
        greenMask = cv2.inRange(hsv, low, up)

        # Perform bitwise_and on original image using the mask
        res = cv2.bitwise_and(noisy_img, noisy_img, mask=greenMask)

        # Invert black & white
        invert = cv2.bitwise_not(greenMask)
        ret, thG = cv2.threshold(invert, 120, 255, cv2.THRESH_TOZERO)

        # Eliminate small blobs
        c, h = cv2.findContours(greenMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]
        # Minimum area for accepted blobs
        threshold_blob_area = 1000

        # Noise blobs
        for i in range(1, len(c)):
          index_level = int(h[0][i][1])
          if index_level <= i:
            cnt = c[i]
            area = cv2.contourArea(cnt)
            #print(area)
          if(area) <= threshold_blob_area:
            cv2.drawContours(greenMask, [cnt], -1, 0, -1, 1)

        # Find contour of blob
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        contour = cv2.morphologyEx(greenMask, cv2.MORPH_OPEN, kernel, iterations=4)
        
        # Get coordinates
        x,y,w,h = cv2.boundingRect(contour)
        
        # Draw rectangle 
        cv2.rectangle(noisy_img, (x, y), (x + w, y + h), (139,0,0), 4)
        # Display text with coordinates 'x' and 'y' on noisy_img
        cv2.putText(noisy_img, "x: "+str(x), (x, y+h+25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,255), 2, cv2.LINE_AA)
        cv2.putText(noisy_img, "y: "+str(y), (x+130, y+h+25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,255), 2, cv2.LINE_AA)

        # Coordinates 100 times
        #x_100 = 


        # Use library 
        ret_ptr = self.funct(ctypes.c_int(x), ctypes.c_int(y))
        ret_arr = ret_ptr[:2]
        
        # Display original coordinates
        timestamp = rospy.Time.now()
        msg = Float64MultiArray()
        msg.data = [float(ret_arr[0]), float(ret_arr[1]), float(timestamp.to_sec())]
        print(msg.data)
        # Print the result
        # print(ret_arr)

        # Publish coordinates to topic
        self.pub.publish(msg)

        # Elimiante return value
        self.mylib.delete_arr.argtypes = [ctypes.POINTER(ctypes.c_int)]
        self.mylib.delete_arr.restype = None
        self.mylib.delete_arr(ret_ptr)

        # Displays
        cv2.imshow('noisy_img', noisy_img)
        #cv2.imshow("Contour", contour)

        # 'q' = quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Destroy all the windows
    cv2.destroyAllWindows()    

if __name__ == '__main__':
  m = m4_t1()
  rospy.init_node('m4_t1', anonymous=True)
  m.video()
  try:
    while not rospy.is_shutdown():
      rospy.Rate(100)
  # Exit
  except KeyboardInterrupt:
    print("Shutting down")
