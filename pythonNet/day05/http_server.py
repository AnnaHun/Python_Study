from socket import *


# 处理浏览器的http请求
def handle(connfd):
    print("Request from ", connfd.getpeername())
    # 接受http请求
    request = connfd.recv(4096)
    # 放置客户端断开
    if not request:
        return

    # 将request按行分割
    request_line = request.splitlines()[0].decode()
    info = request_line.split(" ")[1]
    print(info)

    if info == "/":
        f = open('index.html')
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type: text/html\r\n"
        response += '\r\n'
        response += f.read()
    else:
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type: text/html\r\n"
        response += '\r\n'
        response += "<h1>sorry ......</h1>"

    connfd.send(response.encode())


def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(('0.0.0.0', 8000))
    sockfd.listen(3)
    print("Listen the port 8000 ....")
    while True:
        connfd, addr = sockfd.accept()
        # 处理浏览器请求
        handle(connfd)


if __name__ == "__main__":
    main()
