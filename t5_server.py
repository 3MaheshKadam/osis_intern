import socket
import threading

def handle_client(client_socket, client_address, clients):
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            broadcast(message, clients, client_socket)
    except Exception as e:
        print(f"Error handling client {client_address}: {e}")
    finally:
        client_socket.close()
        clients.remove(client_socket)

def broadcast(message, clients, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except Exception as e:
                print(f"Error broadcasting message: {e}")
                clients.remove(client)

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5555))
    server.listen(5)

    print("Server listening on port 5555...")

    clients = []

    try:
        while True:
            client_socket, client_address = server.accept()
            print(f"Accepted connection from {client_address}")
            clients.append(client_socket)

            client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address, clients))
            client_handler.start()

    except KeyboardInterrupt:
        print("Server shutting down.")
        server.close()

if __name__ == "__main__":
    main()
