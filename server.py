import socket
import threading

def handle_client(client: socket.socket):
    while True:
        try:
            msg = client.recv(8192)
            broadcast(msg)
        except:
            alias = aliases[clients.index(client)]
            aliases.remove(alias)
            clients.remove(client)
            client.close()
            broadcast(f"{alias.decode('utf-8')} left.".encode("utf-8"))
            break


def recieve():
    print("Server running...")
    while True:
        client, addr = server.accept()
        print(f"{addr} connected.")

        client.sendall("alias?".encode("utf-8"))
        alias = client.recv(8192)
        aliases.append(alias)
        clients.append(client)
        print(f"{addr}'s alias is: {alias.decode('utf-8')}")
        broadcast(f"{alias.decode('utf-8')} connected.".encode("utf-8"))

        threading.Thread(target=handle_client, args=(client,)).start()


def broadcast(message: bytes):
    print(message.decode("utf-8"))
    for client in clients:
         client.sendall(message)


server = socket.socket()   
host = "127.0.0.1"
port = 3000     

server.bind((host, port))    
server.listen(5)    

clients: list[socket.socket] = []
aliases: list[bytes] = []

if __name__ == "__main__":
    recieve()
   