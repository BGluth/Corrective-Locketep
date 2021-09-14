class RingBuffer:
    """
    Circular buffer
    """
    __slots__ = ("buf_size", "items", "next_idx")
    RESIZE_MULT = 2.0

    def __init__(self, buf_size: int):
        self.buf_size = buf_size
        self.items = [None] * buf_size
        self.next_idx = 0

    def is_full(self):
        return len(self.items) == self.buf_size

    def push(self, item):
        if self.is_full():
            self.resize(int(self.buf_size * RingBuffer.RESIZE_MULT))

        self.items[self.next_idx] = item
        self._inc_idx()

    def push_ahead(self, item, offset):
        pass

    def pop(self):
        self._dec_idx()
        return self.items[self.next_idx]

    def peek(self):
        return self.items[self.next_idx]

    def resize(self, new_size: int):
        new_buf = [None] * new_size

        for old_item in self.items:
            new_buf.append(old_item)

    def _inc_idx(self):
        self.next_idx = (self.next_idx + 1) % self.buf_size

    def _dec_idx(self):
        self.next_idx = (self.next_idx - 1 ) % self.buf_size
        