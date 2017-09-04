import socket

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(('127.0.0.1', 6666))

    print(s.recv(1024).decode('utf-8'))

    send_data = ''
    while send_data != 'exit':
        send_data = input('input what you want to send:')
        s.send(send_data.encode('utf-8'))
        print(s.recv(1024).decode('utf-8'))
    s.close()
