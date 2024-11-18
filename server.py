import socket

def start_server():

    IP = '127.0.0.1' # IP to listen on
    PORT = 8000 # Port to listen on
    BUFFER_SIZE = 1400  # 1.4 KB
    Timeout = 60  # Client timeout in seconds

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a TCP socket
    
    s.bind((IP, PORT)) # Bind the socket to the IP and port
    print(f"Server is running on {IP}:{PORT}") 
    
    s.listen(5)  # Listen for incoming connections
    print("Waiting for a connection...")

    while True:
        client_socket, addr = s.accept() # Accept a new connection
        print(f"Received data from {addr}") 
        
        client_socket.settimeout(Timeout) # Set a timeout for the client
        
        try:
            data = client_socket.recv(BUFFER_SIZE) # Receive data from the client
            if data:
                print(f"Received data from {addr}: {data.decode('utf-8')}")

            client_socket.sendall(b"Data received") # Send a response to the client
        except socket.timeout:
            print(f"Connection with {addr} timed out")
        finally:
            client_socket.close()
            print(f"Connection with {addr} closed")
            
if __name__ == "__main__":
    start_server()