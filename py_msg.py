import struct


class Message:
    def __init__(self, msg_type=0, msg_content=''):
        self.type = msg_type
        self.content = msg_content

    def __str__(self):
        return self.content

    def parse_from_string(self, data):
        head_length, self.type = struct.unpack('2I', data[:8])
        self.content = data[8:8 + head_length].decode('utf-8')

    def serialize_to_string(self):
        head_length = len(self.content.encode('utf-8')) + 4
        ret = struct.pack('2I', head_length, self.type)
        ret += self.content.encode('utf-8')
        return ret
