import socket

port = 8000
senha = "senha123"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', port))
server.listen(5)
print(f"Servidor rodando em localhost:{port}")

try:
    while True:
        cliente, endereco = server.accept()
        print(f"Conexao recebida de {endereco}")

        data = cliente.recv(5000).decode()
        print(f"Dados recebidos {data}")

        if data.strip() == senha:
            response = "HTTP/1.0 200 OK\r\n\r\n<html><body><h1>Bem-vindo ao servidor!</h1></body></html>\r\n\r\n"
        else:
            response = "HTTP/1.0 403 Forbidden\r\n\r\n<html><body><h1>Acesso negado!</h1></body></html>\r\n\r\n"

        

        cliente.sendall(response.encode())
        cliente.shutdown(socket.SHUT_WR)
        cliente.close()
except:
    server.cloes()