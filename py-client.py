import socket
import struct

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # s.connect(('192.168.4.56', 6666))
    s.connect(('127.0.0.1', 6666))

    print(s.recv(1024).decode('utf-8'))

    send_str = ''
    while send_str != 'exit':
        send_str = input('input what you want to send:')

        head_length = len(send_str.encode('utf-8')) + 4
        head_type = 0
        send_data = struct.pack('2I', head_length, head_type)
        send_data = send_data + send_str.encode('utf-8')

        s.send(send_data)
        print(s.recv(1024).decode('utf-8'))
    s.close()
