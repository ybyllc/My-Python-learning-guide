
# 导入socket这个库
import socket

# 创建一个socket对象
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 开始建立TCP连接
s.connect(("127.0.0.1",8888))
# 接收数据
buffer = []
d = s.recv(1024)
buffer.append(d)

# 把字节连接起来
data = b''.join(buffer)
print(data)

# 关闭连接
s.close()