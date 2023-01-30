from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = OrderedDict()

    def get(self, key: int):
        if key in self.values:
            self.values.move_to_end(key)
            return self.values[key]
        else:
            return -1

    def put(self, key: int, value: int):
        self.values[key]=value
        self.values.move_to_end(key)
        if len(self.values)>self.capacity:
            self.values.popitem(last=False)
    
