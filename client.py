import socket


PORT = 8000 
BUFFER_SIZE = 1400
IP = '127.0.0.1' 

class SocketClient():
    
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.socket = None

    def send_video(self,filename):
      try: 
         with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.host, self.port))
            print('接続されました！')
    
            with open(filename,'rb') as video_file:
            
                while(chunk := video_file.read(BUFFER_SIZE)):
                    sock.sendall(chunk)
                    print(f"{len(chunk)}バイト送信されました")
        
         print("動画の送信を完了しました") 
        
      except Exception as e:
          
          print(f"エラーが発生しました:{e}") # エラーが発生した場合の処理
          
          
if __name__ == '__main__':
    client = SocketClient(IP,PORT)
    client.send_video('test.mp4')