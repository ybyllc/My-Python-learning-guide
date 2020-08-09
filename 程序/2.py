import socket

# 创建socket对象
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 绑定监听端口
s.bind(('127.0.0.1',8888))

# 监听
s.listen(1)

while True:
    # 接收连接
    sock,addr = s.accept()
    print("有人连进来了")
    sock.send(b'hei man, are you ok?')
    sock.close