#!/usr/bin/env python
# Detect green object through webcam and print coordinates

# Ros & libraries
import cv2
import numpy as np
import ctypes
import rospy
from std_msgs.msg import Float64MultiArray
from ctypes import *
import signal
import threading

# gRPC libraries
import grpc
from concurrent import futures
import time
import coords_pb2_grpc as pb2_grpc
import coords_pb2 as pb2
from std_msgs.msg import Float64MultiArray


class CoordsService:

    def __init__(self):
        rospy.Subscriber("/coord", Float64MultiArray, self.getCoordsCallback)
        self.coords = [0,0,0]
    
    def getCoordsCallback(self, msg):
        self.coords[0] = msg.data[0]
        self.coords[1] = msg.data[1]
        self.coords[2] = msg.data[2]

    def GetCoords(self, request, context):

        response = pb2.MessageResponse()
        response.data.extend(self.coords)  # Ejemplo de respuesta con valores de prueba
        print("Response")
        return response

 
def terminate_server(signum, frame):
    print("Got signal: ", frame)
    rospy.signal_shutdown("Ending rosnode")
    terminate.set()

if __name__ == '__main__':
    terminate = threading.Event()
    signal.signal(signal.SIGINT, terminate_server)
    service = CoordsService()
    rospy.init_node('wrapper', anonymous=True)
    
    print("Start Server")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_CoordsServicer_to_server(service, server)
    server.add_insecure_port('[::]:50052')
    server.start()
    rospy.spin()
    print("Exit")
    terminate.wait()








# import grpc
# from concurrent import futures
# import time
# import coords_pb2_grpc as pb2_grpc
# import coords_pb2 as pb2


# class CoordsService(pb2_grpc.CoordsServicer):

#     def __init__(self, *args, **kwargs):
#         pass

#     def GetCoords(self, request, context):
        
#         response = pb2.MessageResponse()
#         response.data.extend([1.0, 2.0, 3.0])  # Ejemplo de respuesta con valores de prueba
#         print("Response")
#         return response


# def serve():
#     server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
#     pb2_grpc.add_CoordsServicer_to_server(CoordsService(), server)
#     server.add_insecure_port('[::]:50052')
#     server.start()
#     server.wait_for_termination()


# if __name__ == '__main__':
#     serve()
