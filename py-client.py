import socket
import threading
from py_msg import Message


def recv(skt):
    while True:
        data = skt.recv(1024)
        msg = Message()
        msg.parse_from_string(data)
        print(str(msg))


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # s.connect(('192.168.4.56', 6666))
    s.connect(('127.0.0.1', 6666))

    t = threading.Thread(target=recv, args=[s])
    t.start()

    send_str = ''
    while send_str != 'exit':
        send_str = input('input what you want to send:')
        send_msg = Message(0, send_str)
        s.send((send_msg.serialize_to_string()))
    s.close()
