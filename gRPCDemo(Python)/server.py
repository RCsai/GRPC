import grpc
import time
from concurrent import futures
import demo_pb2, demo_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_HOST = 'localhost'
_PORT = '50051'


class FormatData(demo_pb2_grpc.FormatDataServicer):
    # 重写接口函数
    def DoFormat(self, request, context):
        input1= request.input1
        input2=request.input2
        res1="返回结果"
        res2=input1+"------"+input2
        return demo_pb2.actionresponse(res=res2)  # 返回一个类实例


def serve():
    # 定义服务器并设置最大连接数,corcurrent.futures是一个并发库，类似于线程池的概念
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=4))  # 创建一个服务器
    demo_pb2_grpc.add_FormatDataServicer_to_server(FormatData(), grpcServer)  # 在服务器中添加派生的接口服务（自己实现了处理函数）
    grpcServer.add_insecure_port(_HOST + ':' + _PORT)  # 添加监听端口
    grpcServer.start()  # 启动服务器
    try:
        while True:
            print("python 服务启动")
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        print("服务关闭")
        grpcServer.stop(0)  # 关闭服务器


if __name__ == '__main__':
    serve()
