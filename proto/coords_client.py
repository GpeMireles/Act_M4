import grpc
import coords_pb2 as pb2
import coords_pb2_grpc as pb2_grpc
import google.protobuf.empty_pb2 as empty_pb2

def run_client():
    channel = grpc.insecure_channel('localhost:50052')  # Dirección y puerto del servidor
    client = pb2_grpc.CoordsStub(channel)

    # Crear una solicitud vacía
    request = empty_pb2.Empty()
    # Realizar la llamada al servidor
    response = client.GetCoords(request)

    # Procesar la respuesta
    print("Response data:")
    for value in response.data:
        print(value)

if __name__ == '__main__':
    run_client()