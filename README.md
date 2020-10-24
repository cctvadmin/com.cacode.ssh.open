# CACode-DockerConsole
 CACode-DockerConsole
## webscoket
基于websocket处理的请求通讯，保持与远程主机的通讯  
通讯携带：key,command  
key:通讯的身份验证  
还没写  
## 这个功能是用来执行shell的
## 接口
/init_server:初始化服务器携带执行的命令，默认使用本机shell执行命令，位于项目部署路径下的config/init.conf  
/ssh/&lt;host/&gt;:执行命令，携带参数：host,port,user,password,command,返回执行  