class Solution:

    def __init__(self):
        self.tmp_buf, self.head, self.tail = [None] * 4, 0, 0

    # @param {char[]} buf destination buffer
    # @param {int} n maximum number of characters to read
    # @return {int} the number of characters read
    def read(self, buf, n):
        # Write your code here
        i = 0
        while i < n:
            if self.head == self.tail:
                self.head, self.tail = 0, Reader.read4(self.tmp_buf)   # when queue is empty, enque
                if not self.tail:
                    break
            buf[i], i, self.head = self.tmp_buf[self.head], i + 1, self.head + 1    # else, deque to satisfy the need
        return i
