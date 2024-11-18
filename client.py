import socket
import threading

PORT = 8000
BUFFER_SIZE = 1400

def send_video(sock,filename):
    