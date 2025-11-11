import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = '192.168.88.128' #localhost
port = 12000
client.connect((hostname, port))
print('connected to the server')
message = client.recv(1024).decode()
print(message)

while True:
    message = input("Your query: ")
    client.send(message.encode())
    if message == "exit":
        break
client.close()