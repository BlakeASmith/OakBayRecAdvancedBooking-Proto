# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import VenueService_pb2 as VenueService__pb2


class VenueStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Book = channel.unary_unary(
                '/Venue/Book',
                request_serializer=VenueService__pb2.BookingRequest.SerializeToString,
                response_deserializer=VenueService__pb2.BookingRequestResult.FromString,
                )
        self.ValidateLogin = channel.unary_unary(
                '/Venue/ValidateLogin',
                request_serializer=VenueService__pb2.LoginInfo.SerializeToString,
                response_deserializer=VenueService__pb2.LoginVerification.FromString,
                )


class VenueServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Book(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ValidateLogin(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VenueServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Book': grpc.unary_unary_rpc_method_handler(
                    servicer.Book,
                    request_deserializer=VenueService__pb2.BookingRequest.FromString,
                    response_serializer=VenueService__pb2.BookingRequestResult.SerializeToString,
            ),
            'ValidateLogin': grpc.unary_unary_rpc_method_handler(
                    servicer.ValidateLogin,
                    request_deserializer=VenueService__pb2.LoginInfo.FromString,
                    response_serializer=VenueService__pb2.LoginVerification.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Venue', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Venue(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Book(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Venue/Book',
            VenueService__pb2.BookingRequest.SerializeToString,
            VenueService__pb2.BookingRequestResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ValidateLogin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Venue/ValidateLogin',
            VenueService__pb2.LoginInfo.SerializeToString,
            VenueService__pb2.LoginVerification.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
