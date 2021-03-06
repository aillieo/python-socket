import socket
import threading
from py_msg import Message


def new_connect(skt, adr):
    print('Accept new connection from %s:%s...' % adr)
    skt.send(Message(0, 'Connected to server!').serialize_to_string())
    while True:
        data = skt.recv(1024)
        msg = Message()
        msg.parse_from_string(data)
        print('receive: ' + str(msg))

        if not data or data.decode('utf-8') == 'exit':
            break
        send_str = 'server got message: ' + msg.content
        skt.send(Message(0, send_str).serialize_to_string())
    skt.close()
    print('Connection from %s:%s closed.' % adr)


if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 6666))
    s.listen(5)
    print('Waiting for connection...')

    while True:
        sock, addr = s.accept()
        t = threading.Thread(target=new_connect, args=(sock, addr))
        t.start()
