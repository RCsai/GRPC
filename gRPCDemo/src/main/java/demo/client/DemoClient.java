package demo.client;

import demo_server.FormatDataGrpc;
import demo_server.actionrequest;
import demo_server.actionresponse;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;

import java.util.concurrent.TimeUnit;

public class DemoClient {

    public static void main(String[] args) throws Exception {
        String input1="rc";
        String input2="zxd";
        String target = "localhost:50051";
        ManagedChannel channel = ManagedChannelBuilder.forTarget(target)
                .usePlaintext()
                .build();
        FormatDataGrpc.FormatDataBlockingStub blockingStub = FormatDataGrpc.newBlockingStub(channel);
        actionrequest.Builder requestBuilder = actionrequest.newBuilder();
        requestBuilder.setInput1(input1);
        requestBuilder.setInput2(input2);
        actionrequest request=requestBuilder.build();

        try {
            actionresponse reply = blockingStub.doFormat(request);
            System.out.println("返回内容：" + reply.getRes());

//            blockingStub.doFormat(request);
        } finally {
            channel.shutdownNow().awaitTermination(5, TimeUnit.SECONDS);
        }
    }
}
