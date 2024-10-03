import json
import os
import socket
import threading


def load_contacts():
    if os.path.exists("contacts.json"):
        with open("contacts.json", 'r') as f:
            return json.load(f)
    return {}

def broadcast():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    print("Message: ", end='')
    while True:
        message = input()
        sock.sendto(message.encode(), ('<broadcast>', 37020))

def listen():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', 37020))
    local_ip = socket.gethostbyname(socket.gethostname())
    print(local_ip)
    while True:
        data, addr = sock.recvfrom(1024)
        if addr[0] == local_ip:
            sender = "You"
        elif addr[0] in contacts:
            sender = contacts[addr[0]]
        else:
            sender = addr[0]
        print(f"\r{sender} Said:\n"
              f"\t{data.decode()}\n\n"
              f"Message: ", end='')

if __name__ == "__main__":
    contacts = load_contacts()

    broadcast_thread = threading.Thread(target=broadcast, daemon=True)
    listen_thread = threading.Thread(target=listen, daemon=True)
    broadcast_thread.start()
    listen_thread.start()


    try:
        while broadcast_thread.is_alive():
            pass
    except KeyboardInterrupt:
        print("Stopping...")
