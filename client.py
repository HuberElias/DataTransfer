import socket
import threading

def client_recieve():
    while True:
        try:
            msg = client.recv(1024).decode("utf-8")
            if msg == "alias?":
                client.send(alias.encode("utf-8"))
            else:
                print(msg)
        except:
            client.close()
            break


def client_send():
    while True:
        msg = f"{alias}: {input('')}"
        client.send(msg.encode("utf-8"))

alias = input("Your Name: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 3000))

r_thread = threading.Thread(target=client_recieve).start()
s_thread = threading.Thread(target=client_send).start()