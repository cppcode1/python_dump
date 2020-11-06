print("tcp client")
import sys
import socket
import signal
import time

argument_count = len(sys.argv)

if (argument_count != 3):
    print(f"there are too little arguments: {argument_count}")
    print("python script_name(1) ip address(2) port(3)")
    exit(0)

# extract data from passed arguments
ip_address = sys.argv[1]
port = int(sys.argv[2])


print(f"starting a server with ip {ip_address} port {port}")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.bind((ip_address, port))
client_socket.listen(1)

conn, addr = s.accept()
with conn:
    print('connected to ', addr)
    while True:
        data = conn.recv(20)
        if not data: continue
        conn.sendall(data) # echo

exit(0)