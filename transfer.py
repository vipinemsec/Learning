import socket

def forward_data():
    send_socket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        
        data = input("enter desired input data: ")
        input_port1=54321
        input_port2=54322
        # sendto() function is used to send data for UDP in sockets
        message_bytes = data.encode('utf-8')
        send_socket1.sendto(message_bytes, ('127.0.0.1', input_port1))
        send_socket1.sendto(message_bytes, ('127.0.0.1', input_port2))

        # sendto() function is used to send data for UDP in sockets

if __name__ == "__main__":
    print("welcome in desktop")
    forward_data()