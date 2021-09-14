import uuid

class Message:
    def __init__(self, m_type, m_payload):
        self.m_type = m_type # int?
        self.m_payload = m_payload

class Event:
    def __init__(self, client_id, cycle_num, event_payload):
        self.client_id = client_id
        self.cycle_num = cycle_num
        self.event_payload = event_payload

class MessageType:
    EVENT = 0
    CLIENT_CONNECTED = 1
    CLIENT_DISCONNECTED = 2
    L_BUF_SIZE_CHANGE = 3
    CLIENT_SUSPENDED = 4

def gen_guid_client_id():
    return uuid.uuid3()