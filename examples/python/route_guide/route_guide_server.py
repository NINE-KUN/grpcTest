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
"""The Python implementation of the gRPC route guide server."""

from concurrent import futures
import logging
import math
import time

import grpc
import route_guide_pb2
import route_guide_pb2_grpc
import route_guide_resources


def get_feature(feature_db, point):
    """Returns Feature at given location or None."""
    for feature in feature_db:
        if feature.location == point:
            return feature
    return None


def get_distance(start, end):
    """Distance between two points."""
    coord_factor = 10000000.0
    lat_1 = start.latitude / coord_factor
    lat_2 = end.latitude / coord_factor
    lon_1 = start.longitude / coord_factor
    lon_2 = end.longitude / coord_factor
    lat_rad_1 = math.radians(lat_1)
    lat_rad_2 = math.radians(lat_2)
    delta_lat_rad = math.radians(lat_2 - lat_1)
    delta_lon_rad = math.radians(lon_2 - lon_1)

    # Formula is based on http://mathforum.org/library/drmath/view/51879.html
    a = pow(math.sin(delta_lat_rad / 2), 2) + (
      math.cos(lat_rad_1)
      * math.cos(lat_rad_2)
      * pow(math.sin(delta_lon_rad / 2), 2)
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    R = 6371000
    # metres
    return R * c


"""子类 生成的类：RouteGuideServicer route_guide_pb2_grpc.RouteGuideServicer"""

"""RouteGuideServicer实现所有服务方法。Route Guide"""
"""Provides methods that implement functionality of route guide server."""


class RouteGuideServicer(route_guide_pb2_grpc.RouteGuideServicer):

    def __init__(self):
        self.db = route_guide_resources.read_route_guide_database()

    def GetFeature(self, request, context):
        """ 从客户端获取一个，并从其返回相应的特征信息 数据库中的数据库
            该方法将传递对 RPC 的请求，以及一个提供特定于 RPC 的信息的对象，
            例如 超时限制。它返回一个响应。route_guide_pb2.Pointgrpc.ServicerContextroute_guide_pb2.Feature"""
        feature = get_feature(self.db, request)
        if feature is None:
            return route_guide_pb2.Feature(name="", location=request)
        else:
            return feature

    def ListFeatures(self, request, context):
        """响应流式 RPC 向客户端发送多个特征
          这里的请求消息是其中 客户想要找到 s。而不是返回单个响应 方法产生零个或多个响应
          context 对象包含一些元数据，比如终端用户授权的令牌的标识和请求戒指时间，这些元数据在
          请求的生命周期内一直存在"""
        left = min(request.lo.longitude, request.hi.longitude)
        right = max(request.lo.longitude, request.hi.longitude)
        top = max(request.lo.latitude, request.hi.latitude)
        bottom = min(request.lo.latitude, request.hi.latitude)
        for feature in self.db:
            if (
                feature.location.longitude >= left
                and feature.location.longitude <= right
                and feature.location.latitude >= bottom
                and feature.location.latitude <= top
            ):
                yield feature

    def RecordRoute(self, request_iterator, context):
        """请求流式 RPC
        request-streaming 方法使用RecordRoute迭 代之 请求值并返回单个响应值"""
        point_count = 0
        feature_count = 0
        distance = 0.0
        prev_point = None

        start_time = time.time()
        for point in request_iterator:
            point_count += 1
            if get_feature(self.db, point):
                feature_count += 1
            if prev_point:
                distance += get_distance(prev_point, point)
            prev_point = point

        elapsed_time = time.time() - start_time
        return route_guide_pb2.RouteSummary(
          point_count=point_count,
          feature_count=feature_count,
          distance=int(distance),
          elapsed_time=int(elapsed_time),
        )

    def RouteChat(self, request_iterator, context):
        """此方法的语义是请求流式处理的语义的组合 方法和响应流式处理方法。
          它被传递一个请求的迭代器 values 并且本身就是响应值的迭代器"""
        prev_notes = []
        for new_note in request_iterator:
            for prev_note in prev_notes:
                if prev_note.location == new_note.location:
                    yield prev_note
            prev_notes.append(new_note)


def serve():
    """启动 gRPC 服务器，以便客户端可以实际使用您的服务
    服务器方法是非阻塞的。将实例化一个新线程 处理请求。
    线程调用通常会 在此期间没有任何其他工作要做。
    在这种情况下，您可以调用以完全阻止调用线程，直到 服务器终止。
    start() server.start()server.wait_for_termination()"""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    """添加服务器方法至线程池"""
    route_guide_pb2_grpc.add_RouteGuideServicer_to_server(
      RouteGuideServicer(), server
    )
    """启动服务器等待客户端链接"""
    a = server.add_insecure_port("[::]:50052")
    print(a)
    server.start()
    print("服务器启动等待客户端链接")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
