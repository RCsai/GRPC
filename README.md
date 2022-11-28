# GRPC

### 项目介绍

1、该项目包含GRPC的Java版本以及Python版本的Demo,两者之间的服务器以及客户端之间能够相互进行调用。

2、项目文件夹中的.sh文件是根据.proto文件自动生成相应文件的脚本。



### 注意事项

1、Java版本与Python版本的proto文件需要一致，否则两者之间无法进行调用。

2、Java版本使用IDEA软件运行时，通过File->Setting->Build->Build Tools->Gradle将项目的Build and Run Using改为IDEA,Run tests Using改为IDEA。

3、Java版本运行过程中如果出现什么函数接口不存在的问题，需要修改build.gradle中关于grpc的版本，同时需要将关于grpc的各个依赖的版本号保持一致。
