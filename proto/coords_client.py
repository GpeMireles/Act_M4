"""
@file coords_client.py
@brief Este código genera un cliente de grpc para testear el server del wrapper de grpc
"""
import grpc
import coords_pb2 as pb2
import coords_pb2_grpc as pb2_grpc
import google.protobuf.empty_pb2 as empty_pb2

def run_client():
    """
    Function to run the gRPC client.
    """
    channel = grpc.insecure_channel('localhost:50052')
    client = pb2_grpc.CoordsStub(channel)
    request = empty_pb2.Empty()
    response = client.GetCoords(request)
    print("Response data:")
    for value in response.data:
        print(value)

if __name__ == '__main__':
    run_client()