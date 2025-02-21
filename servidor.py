import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 6969))
server.listen(5)

try:
    while True:
        client, address = server.accept()
        data = client.recv(5000).decode()
        print(data)

        client.sendall(
            "HTTP/1.0 200 OK\r\n\r\n<html><body>Obrigado pela conexão</body></html>\r\n\r\n".encode()
        )

        client.shutdown(socket.SHUT_WR)
        client.close()
except:
    server.close()
