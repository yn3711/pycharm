import time
from concurrent import futures
import grpc
import sample_pb2
import sample_pb2_grpc
from grpc_reflection.v1alpha import reflection

class SampleServiceServicer(sample_pb2_grpc.SampleServiceServicer):

    def __init__(self):
        pass

    def ReplyMessage(self, request, context):
        print(f'Input: {request.input_message}')
        return sample_pb2.SampleResponse(output_message='Hello! {}'.format(request.input_message))
    def Login(self, request, context):
        return sample_pb2.LoginResponse(code=200, access_token='dummy', refresh_token='dummy')
        #except Exception as e:
        #    print(e)
        #    return sample_pb2.LoginResponse(code=401, error='Authorization error')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sample_pb2_grpc.add_SampleServiceServicer_to_server(SampleServiceServicer(), server)
    SERVICE_NAMES = (
        sample_pb2.DESCRIPTOR.services_by_name['SampleService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Starting gRPC sample server...')
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()