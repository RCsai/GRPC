import grpc
import demo_pb2, demo_pb2_grpc

_HOST = 'localhost'
_PORT = '50051'


def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)  # 监听频道
    client = demo_pb2_grpc.FormatDataStub(channel=conn)  # 客户端使用Stub类发送请求,参数为频道,为了绑定链接
    response = client.DoFormat(demo_pb2.actionrequest(input1="rc2121",input2="zxd"))  # 返回的结果就是proto中定义的类
    print(response)

    # print("received: " + response.text)


if __name__ == '__main__':
    run()