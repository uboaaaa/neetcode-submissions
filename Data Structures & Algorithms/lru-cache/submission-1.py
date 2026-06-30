class ListNode: # doubly linked list where left = most recently used, right = least recently used
    def __init__(self, key=None, value=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hm = {} # key: node
        self.head, self.tail = ListNode(), ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def make_head(self, node):
        # prelim stuff
        tmp = self.head.next

        # head <-> node updates
        self.head.next = node
        node.prev = self.head

        # node <-> tmp updates
        node.next = tmp
        tmp.prev = node

    def get(self, key: int) -> int:
        if key in self.hm:
            node = self.hm[key]
            self.remove_node(node)
            self.make_head(node)
            return node.value
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            node = self.hm[key]
            node.value = value
            self.remove_node(node)
            self.make_head(node)
        else:
            self.hm[key] = ListNode(key, value)
            self.make_head(self.hm[key])
            self.capacity -= 1
            while self.capacity < 0:
                to_remove = self.tail.prev
                del self.hm[to_remove.key]
                self.remove_node(to_remove)
                self.capacity += 1

        
