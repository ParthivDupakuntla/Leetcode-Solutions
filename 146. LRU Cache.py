# hash map contains keys and values, values are nodes.
# linked list contains order within which everything is stored. lru is to the left
# mru is to the right. 
# 2 helper functions
# one to remove node from list
# one to insert node to the right
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.cap = capacity
        
        #LRU to the left and MRU to the right
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self, node): # remove node from the linked list
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert(self, node): # insert node at the right most 
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache)>self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
