package demo.server.impl;

import demo_server.FormatDataGrpc;
import demo_server.actionrequest;
import demo_server.actionresponse;
import io.grpc.stub.StreamObserver;

public class DemoServerImpl extends FormatDataGrpc.FormatDataImplBase {


    @Override
    public void doFormat(actionrequest request, StreamObserver<actionresponse> responseObserver) {
//        super.doFormat(request, responseObserver);

        String input1=request.getInput1();
        String input2=request.getInput2();

        String res=input1+"-----"+input2;

        actionresponse replay=actionresponse.newBuilder().setRes(res).build();
        responseObserver.onNext(replay);
        responseObserver.onCompleted();

    }
}
