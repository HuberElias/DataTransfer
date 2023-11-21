import socket
import threading

def handle_client(client: socket.socket):
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg)
        except:
            clients.remove(client)
            client.close()
            index = clients.index(client)
            print(index)
            alias = aliases[index]
            broadcast(f"{alias} left.".encode("utf-8"))
            aliases.remove(alias)
            break


def recieve():
    while True:
        print("Server running...")
        client, addr = server.accept()
        print(f"{addr} connected.")

        client.sendall("alias?".encode("utf-8"))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f"{addr}'s alias is: {alias.decode('utf-8')}")
        broadcast(f"{alias.decode('utf-8')} connected.".encode("utf-8"))

        thread = threading.Thread(target=handle_client, args=(client,)).start()


def broadcast(message):
    print(message.decode("utf-8"))
    for client in clients:
         client.sendall(message)


server = socket.socket()   
host = "127.0.0.1"
port = 3000     

server.bind((host, port))    
server.listen(5)    

clients: list[socket.socket] = []
aliases = []

if __name__ == "__main__":
    recieve()
   