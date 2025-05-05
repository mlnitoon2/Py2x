import json
from pyfox2x.sfs_types.SFSObject import SFSObject

class SFSPacket:
    def __init__(self, packet_data=None):
        self.packet_data = packet_data if packet_data else b''

    @staticmethod
    def compile_packet(packet) -> bytes:
        data = packet.compile()
        if len(data) < 65535:
            header = b'\x80' + len(data).to_bytes(2, 'big')
        else:
            header = b'\x88' + len(data).to_bytes(4, 'big')
        return header + data

    @staticmethod
    def decompile_packet(packet: bytes) -> 'SFSObject':
        return SFSObject.decompile(packet).get("p")

    def get_packet_data(self):
        return self.packet_data

    def getJsonDump(self):
        return json.dumps(self.packet_data.getJsonDump()) if self.packet_data else "{}"

    def get(self, key: str):
        return self.packet_data.get(key)
