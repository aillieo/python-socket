import socket
import threading


def new_connect(skt, adr):
    print('Accept new connection from %s:%s...' % adr)
    skt.send(b'Connected to server!')
    while True:
        data = skt.recv(1024)
        if not data or data.decode('utf-8') == 'exit':
            break
        skt.send(('server got message: %s' % data.decode('utf-8')).encode('utf-8'))
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
