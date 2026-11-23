class Node:
    def __init__(self, key=None, val=None, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> Node()

        # init linkedlist
        self.head = Node() # least recently used
        self.tail = Node(prev=self.head) # most recently used
        self.head.next = self.tail

    # decouple given node from LL
    def remove(self, node):
        # pn <-> node <-> nn
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        node.prev = node.next = None

    # insert at tail
    def insert(self, node):
        # mru <-> tail
        # mru <-> node <-> tail
        mru = self.tail.prev
        mru.next, node.prev = node, mru
        node.next, self.tail.prev = self.tail, node

    def get(self, key: int) -> int:
        if key in self.cache:
            # update recency
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node) 

        if len(self.cache) > self.capacity:
            lru = self.head.next
            del self.cache[lru.key]
            self.remove(lru)
        


