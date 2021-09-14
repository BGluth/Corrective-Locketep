from lockstep import LockstepState
from msg_processing import MessageProcessingState
from net_topology import NetTopState

# Contains all the state that the user of the library needs to send/recv msgs
class NetworkState:


    def __init__(self, server_ip_and_port):
        client_id = gen_guid_client_id()

        self._lockstep_state = LockstepState()
        self._msg_proc_state = MessageProcessingState(client_id)
        self._net_top_state = NetTopState(gen_guid_client_id)


def init():
    return NetworkState()
