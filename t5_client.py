import socket
import threading

def receive_messages(client_socket):
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
    except Exception as e:
        print(f"Error receiving message: {e}")

def send_messages(client_socket):
    try:
        while True:
            message = input()
            client_socket.send(message.encode('utf-8'))
    except Exception as e:
        print(f"Error sending message: {e}")

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5555))

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    send_thread = threading.Thread(target=send_messages, args=(client,))

    receive_thread.start()
    send_thread.start()

if __name__ == "__main__":
    main()
