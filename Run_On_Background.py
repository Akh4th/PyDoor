import os
import subprocess as sp


def running():
    if os.name == "posix":
        sp.run(["python", "Entrance.py", "&"])
    elif os.name == "NT":
        sp.run(["pythonw", "Entrance.py"])


if __name__ == '__main__':
    running()
