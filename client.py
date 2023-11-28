import socket
import threading
from image2ascii import convert

def client_recieve():
    while True:
        try:
            msg = client.recv(8192).decode("utf-8")
            if msg == "alias?":
                client.send(alias.encode("utf-8"))
            else:
                print(msg)
        except:
            client.close()
            break


def get_text_file(path: str):
    try:
        with open(path, "r") as f:
            return f.read()
    except:
        pass


def get_image(path: str):
    try:
        return convert(path, 150)
    except:
        return ""


def client_send():
    while True:
        try:
            inp = input("")
        except KeyboardInterrupt and EOFError:
            break
        
        space = " "

        filename = ""
        if("file:\\\\" in inp and ".txt" in inp):
            filename = inp.split("file:\\\\")[1]
            inp = get_text_file(filename)
        elif("image:\\\\" in inp):
            filename = inp.split("image:\\\\")[1]
            inp = get_image(filename)
            space = "\n"

        

        try:
            msg = f"<{alias}>{space}{inp}"

            client.sendall(msg.encode("utf-8"))
        except:
            pass

alias = input("Your Name: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 3000))

threading.Thread(target=client_recieve).start()
threading.Thread(target=client_send).start()