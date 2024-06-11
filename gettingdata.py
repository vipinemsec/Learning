import socket

listen_address = '127.0.0.1'
listen_port = 54321 

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((listen_address, listen_port))

print(f"listening on {listen_address}:{listen_port}")
print(listen_address)

while True:
    
    data, addr = sock.recvfrom(1024)
    print(f"Received message: {data} from {addr}")
    print("we are getting data from our desired port ")