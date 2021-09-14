class NetTopState:
    def __init__(self, client_id):
        pass

    def send_message_to_all_clients(self, message):
        pass

    def set_handler_for_msg_received(self, handler):
        pass

    # Called by msg_processing when a new client connects
    # We need to notify all clients that this new client connected
    def notify_client_connected(self, client_id):
        pass

    def notify_client_disconnected(self, client_id):
        pass

    def get_client_id(self)
