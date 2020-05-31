import socket
import argparse

parser = argparse.ArgumentParser('TCP port scanner')
parser.add_argument('hostname', help='enter hostname')
parser.add_argument('start_port', help='port to start from')
parser.add_argument('end_port', help='last port to check')

arguments = parser.parse_args()
hostname = arguments.hostname
start_port = int(arguments.start_port)
end_port = int(arguments.end_port)

ip = socket.gethostbyname(hostname)

flag = False

try:
    for port in range(start_port, end_port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        res = sock.connect_ex((ip, port))
        if res == 0:
            flag = True
            print(f'Порт {port} открыт')
    if not flag:
        print('Нет открытых портов в заданном диапазоне.')
except Exception:
    pass
