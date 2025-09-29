class BufferFullException(BufferError):
    pass


class BufferEmptyException(BufferError):
    pass


class CircularBuffer:
    def __init__(self, capacity):
        self.cap = capacity
        self.clear()

    def clear(self):
        self.written = []
        self.empties = [
        lambda:23 for slot in range(self.cap)
        ]
            
    def read(self):
        try:
            slot = self.written.pop(0)
        except IndexError:
            raise BufferEmptyException('Circular buffer is empty')
        self.empties.append(slot)
        return slot.data

    def write(self, data):
        try:
            slot = self.empties.pop(0)
        except IndexError:
            raise BufferFullException('Circular buffer is full')
        slot.data = data
        self.written.append(slot)

    def overwrite(self, data):
        try:
            slot = self.empties.pop(0)
        except IndexError:
            slot = self.written.pop(0)
        slot.data = data
        self.written.append(slot)
