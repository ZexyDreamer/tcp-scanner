import socket
import argparse
import threading
from queue import Queue

parser = argparse.ArgumentParser('TCP port scanner')
parser.add_argument('hostname', help='hostname')
parser.add_argument('start_port', help='port to start from')
parser.add_argument('end_port', help='last port to check')

arguments = parser.parse_args()
hostname = arguments.hostname
start_port = int(arguments.start_port)
end_port = int(arguments.end_port)

ip = socket.gethostbyname(hostname)
queue = Queue()
open_ports = []


def check_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        return True
    except:
        return False


def helper():
    while not queue.empty():
        port = queue.get()
        if check_port(port):
            open_ports.append(port)


for p in range(start_port, end_port + 1):
    queue.put(p)
thread_list = []
for _ in range(500):
    thread = threading.Thread(target=helper)
    thread_list.append(thread)
for t in thread_list:
    t.start()
for t in thread_list:
    t.join()

with open('result.txt', 'w') as file:
    file.write(f'The host {hostname} has ports open: ' +
               str(sorted(open_ports))[1:-1])
