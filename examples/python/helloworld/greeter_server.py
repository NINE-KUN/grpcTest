# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc
import helloworld_pb2
import helloworld_pb2_grpc

"""服务端方法实现"""

class Greeter(helloworld_pb2_grpc.GreeterServicer):
  def SayHello(self, request, context):
    return helloworld_pb2.HelloReply(message="Hello, %s!" % request.name)

  def SayHelloAgain(self, request, context):
    return helloworld_pb2.HelloReply(message="Hello again, %s" % request.name)

"""服务实现准备就绪后，需要监听客户端的请求，将这些请求分发到服务器实现，并将服务器相应返回到客户端"""
def serve():
  port = "50051"
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
  server.add_insecure_port("[::]:" + port)
  server.start()
  print("Server started, listening on " + port)
  server.wait_for_termination()


if __name__ == "__main__":
  logging.basicConfig()
  serve()
