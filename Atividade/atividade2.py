import socket
senha = "senha"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8000))

client.sendall(senha.encode())

response = client.recv(5000).decode()
print("Resposta do servidor:")
print(response)

client.close()
