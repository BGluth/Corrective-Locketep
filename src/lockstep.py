from ring_buffer import RingBuffer

class LockstepState:
    __slots__ = ("_curr_cycle", "_lockstep_bufs", "_lbuf_size")

    def __init__(self, lbuf_size, curr_cycle, num_clients):
        self._curr_cycle = curr_cycle # For when a client connects mid game

        # Each client has their own buffer of events
        # Indexing 
        self._lockstep_bufs = {RingBuffer(lbuf_size) * 2} * num_clients
        self._lbuf_size = lbuf_size
        
    def advance_cycle(self):
        self._curr_cycle += 1

        # Clear events for the next cycle we just "opened" in the lbuf
        for lbuf in self._lockstep_bufs.items():
            lbuf.push_ahead(None, 2 * self._lbuf_size)

    def handle_event_recvd(self, event):
        cycle_idx_in_buf = self._get_idx_in_lbuf_for_cycle(event.cycle)
        self._lockstep_bufs[event.player_id].push_ahead(event, cycle_idx_in_buf)


    def handle_events_recvd(self, events):
        """
        Pass received events to the lockstep state
        Separate thread?
        """
        for event in events:
            self.handle_event_recvd(event)

    def set_lbuf_size(self, lbuf_size):
        for client_lbuf in self._lockstep_bufs.items:
            client_lbuf.resize(lbuf_size)

        self._lbuf_size = lbuf_size

    def get_events_for_cycle(self):
        """
        Returns all the events for all clients for the current cycle
        Blocks if we have not yet received events from all clients for the current cycle
        Note that this should be run from the core loop thread!
        """
        events_for_cycle = []

        for player_lbuf in self._lockstep_bufs.items():
            
            while True:
                if player_lbuf.peek() == None:
                    self._block_until_change_in_lbuf()
                    continue

                events_for_cycle.append(player_lbuf.pop())
                break

        return events_for_cycle
            

    def add_new_client(self, client_id):
        self._num_clients += 1
        self._lockstep_bufs.insert(client_id, RingBuffer(self._lbuf_size))

    def remove_client(self, client_id):
        self._num_clients -= 1
        self._lockstep_bufs.remove(client_id)

    def _get_idx_in_lbuf_for_cycle(self, cycle: int):
        return cycle - self._curr_cycle

    def _block_until_change_in_lbuf(self):
        """
        This is what will cause the actual stall when we haven't heard from a client by the time we reach the end of the buffer
        """
        pass