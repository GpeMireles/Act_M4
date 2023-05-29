# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import coords_pb2 as coords__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class CoordsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCoords = channel.unary_unary(
                '/coords.Coords/GetCoords',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=coords__pb2.MessageResponse.FromString,
                )


class CoordsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetCoords(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CoordsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetCoords': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCoords,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=coords__pb2.MessageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'coords.Coords', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Coords(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetCoords(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/coords.Coords/GetCoords',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            coords__pb2.MessageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)