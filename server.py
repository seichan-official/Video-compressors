import socket

def start_server():
    IP = '127.0.0.1'  # IP to listen on
    PORT = 8000       # Port to listen on
    BUFFER_SIZE = 1400  # Buffer size for receiving data
    TIMEOUT = 60       # Client timeout in seconds

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket
    s.bind((IP, PORT))  # Bind the socket to the IP and port
    print(f"Server is running on {IP}:{PORT}")
    
    s.listen(5)  # Listen for incoming connections
    print("Waiting for a connection...")

    while True:
        client_socket, addr = s.accept()  # Accept a new connection
        print(f"Connection established with {addr}")
        
        client_socket.settimeout(TIMEOUT)  # Set a timeout for the client

        while True:
            client_socket, addr = s.accept()
            print(f"Connection established with {addr}")

            try:
                file_size = int.from_bytes(client_socket.recv(4), 'big')  # 最初の32ビットを受信してファイルサイズを取得
                print(f"Receiving file of size {file_size} bytes")

                with open('received_file.mp4', 'wb') as file:
                    total_received = 0
                    while total_received < file_size:
                        data = client_socket.recv(BUFFER_SIZE)
                        if not data:
                            break
                        file.write(data)
                        total_received += len(data)
                        print(f"Received {len(data)} bytes ({total_received}/{file_size})")

                print(f"File received from {addr} and saved as 'received_file.mp4'")
                client_socket.sendall(b"Data received")
            except Exception as e:
                print(f"An error occurred: {e}")
            finally:
                client_socket.close()
                print(f"Connection with {addr} closed")

if __name__ == "__main__":
    start_server()
