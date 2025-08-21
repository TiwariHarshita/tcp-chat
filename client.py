import socket
import threading

HOST = "127.0.0.1"
PORT = 5010

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode("utf-8")
            if message:
                print(message)
        except:
            print("⚠️ Disconnected from server.")
            sock.close()
            break

def start_client():
    username = input("Enter your username: ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    client.send(username.encode("utf-8"))  # Send username first

    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.daemon = True
    thread.start()

    print("✅ Connected to chat! Start typing...")

    while True:
        try:
            msg = input()
            if msg.lower() == "/quit":
                client.close()
                break
            client.send(msg.encode("utf-8"))
        except:
            break

if __name__ == "__main__":
    start_client()