class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.seen={}
        

    def get(self, key: int) -> int:
        return self.seen.get(key,-1)
        

    def put(self, key: int, value: int) -> None:
        self.seen[key]=self.seen.get(key,0)+value
        if len(self.seen)>self.capacity:
            self.seen.pop(next(iter(self.seen)))
        
