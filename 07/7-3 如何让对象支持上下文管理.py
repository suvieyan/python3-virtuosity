"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/8/16'
"""

from sys import stdin, stdout
import getpass
import telnetlib
from collections import deque

class TelnetClient:
    def __init__(self, host, port=23):
        self.host = host
        self.port = port

    def __enter__(self):
        # 进入环境之前的操作
        self.tn = telnetlib.Telnet(self.host, self.port)
        self.history = deque([])
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        print('IN __exit__', exc_type, exc_value, exc_tb)

        self.tn.close()
        self.tn = None

        with open('history.txt', 'a') as f:
            f.writelines(self.history)
        # 异常
        return True

    def login(self):
        # user
        self.tn.read_until(b"login: ")
        user = input("Enter your remote account: ")
        self.tn.write(user.encode('utf8') + b"\n")

        # password
        self.tn.read_until(b"Password: ")
        password = getpass.getpass()
        self.tn.write(password.encode('utf8') + b"\n")
        out = self.tn.read_until(b'$ ')
        stdout.write(out.decode('utf8'))

    def interact(self):
        while True:
            cmd = stdin.readline()
            if not cmd:
                break

            self.history.append(cmd)
            self.tn.write(cmd.encode('utf8'))
            out = self.tn.read_until(b'$ ').decode('utf8')

            stdout.write(out[len(cmd)+1:])
            stdout.flush()

# client = TelnetClient('192.168.0.105')
# client.connect()
# client.login()
# client.interact()
# client.cleanup()

with TelnetClient('10.0.0.103') as client:
    # raise Exception('TEST')
    client.login()
    client.interact()

print('END')

