import socket
import threading

HOST = "127.0.0.1"
PORT = 5010

# Store connected clients
clients = {}  # socket -> username

def broadcast(message, sender_socket=None):
    for client_socket in clients:
        if client_socket != sender_socket:
            try:
                client_socket.send(message.encode("utf-8"))
            except:
                client_socket.close()
                remove_client(client_socket)

def handle_client(client_socket, address):
    try:
        # First message should be username
        username = client_socket.recv(1024).decode("utf-8").strip()
        clients[client_socket] = username
        print(f"[NEW USER] {username} connected from {address}")
        broadcast(f"🔔 {username} has joined the chat!")

        while True:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            print(f"[{username}] {message}")
            broadcast(f"[{username}] {message}", sender_socket=client_socket)
    except:
        pass
    finally:
        remove_client(client_socket)

def remove_client(client_socket):
    if client_socket in clients:
        username = clients[client_socket]
        print(f"[DISCONNECT] {username} left.")
        broadcast(f"❌ {username} has left the chat.")
        del clients[client_socket]
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[STARTING] Server is running on {HOST}:{PORT}")

    while True:
        client_socket, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.start()

if __name__ == "__main__":
    start_server()