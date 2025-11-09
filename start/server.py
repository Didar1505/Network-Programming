import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = '0.0.0.0' #localhost
port = 12000
server.bind((hostname, port))
server.listen(10)
print("server stared")

def handle_client(client:socket.socket):
    try:
        while True:
            message = client.recv(1024).decode()
            if not message:
                break

            if message == 'exit':
                client.close()
                server.close()
                print("Server closed")
                exit()
                break
            else:
                print("Client: ", message)
    except:
        client.close()      


while True:
    try:
        client, address = server.accept()
        print("Connected client: ", address)
        client.send("Hello, this is a message from server".encode())
        message = client.recv(1024).decode()
        threading.Thread(target=handle_client, args=(client,), daemon=True).start()
    except:
        print("server closed")
        break
