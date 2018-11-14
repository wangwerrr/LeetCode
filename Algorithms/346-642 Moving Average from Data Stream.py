from Queue import Queue

class MovingAverage(object):

    def __init__(self, size):
        self.queue = Queue()
        self.size = size
        self.sum = 0.0
        

    # @param {int} val an teger
    def next(self, val):
        self.sum += val
        if self.queue.qsize() == self.size:
            self.sum -= self.queue.get()
        self.queue.put(val)
        return self.sum * 1.0 / self.queue.qsize()


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)
