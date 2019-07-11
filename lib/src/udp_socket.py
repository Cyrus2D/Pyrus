import socket

MAX_BUFF_SIZE = 8192

class IPAddress:
    def __init__(self, ip, port):
        self._ip = ip
        self._port = port

    def tuple(self) -> tuple:
        return self.ip(), self.port()

    def __repr__(self):
        return self.ip(), self.port()

    def __str__(self):
        return f"({self.ip()}:{self.port()}"

    def ip(self):
        return self._ip

    def port(self):
        return self._port


class UDPSocket:
    def __init__(self, ip_address: IPAddress):
        self._ip: IPAddress = ip_address
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_msg(self, msg: str):
        self._sock.sendto(msg.encode(), 0, self._ip.tuple())

    def recieve_msg(self):
        return self._sock.recvfrom(MAX_BUFF_SIZE)

