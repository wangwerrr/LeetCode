# dict + double linked list
# dict for searching, double linked list for recording recent usage

class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    # when getting an item, remove it from the original place and add it to the tail of the linked list
    def get(self, key):
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1
    # when adding an item, add it to the tail of the linked list, as well as the dict
    def put(self, key, value):
        # if key already exist, remove that node
        if key in self.dic:
            self._remove(self.dic[key])
        # add a new node to the tail; update/add dict[key]
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n
        # if there's exceed amout of cache, delete the head node from linked list & dict
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]
            
    # remove from the head
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        
    # add to the tail
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
