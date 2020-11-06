print("tcp client")
import sys
import socket
import signal
import time

argument_count = len(sys.argv)

if (argument_count != 4):
    print(f"there are too little arguments: {argument_count}")
    print("python script_name(1) ip address(2) port(3) message(4)")
    exit(0)

# extract data from passed arguments
ip_address = sys.argv[1]
port = int(sys.argv[2])
message = sys.argv[3]
connected = False


print(f"connecting to ip {ip_address} port {port}")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while not connected:
    try:
        client_socket.connect((ip_address, port))
        connected = True
    except:
        print("not connected")
        time.sleep(3)


def close_connection(sig, frame):
    print("closing a connection")
    client_socket.close()

signal.signal(signal.SIGINT, close_connection)

counter = 0
while True:
    s.send(f"{message}{counter}")
    data = s.recv(20)
    print(data)
    counter = counter + 1

exit(0)