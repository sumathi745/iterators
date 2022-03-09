class Circle:
    
    def __init__(self, sequence, count):
        self.sequence = sequence
        self.count = count
        self.latest_iter = -1
        self.lst = []
        
    def __iter__(self):
        
        if self.latest_iter > self.count:
            raise StopIteration
            
        i = 0 
        
        while i < self.count:
            index = i % len(self.sequence)
            self.lst.append(self.sequence[index])
            i += 1
        
        return self
    
    def __next__(self):
        
        self.latest_iter += 1
        
        if self.latest_iter > self.count:
            raise StopIteration
        else:
            index = self.latest_iter % len(self.sequence)
            return self.sequence[index]
            
        
  


c = Circle('abc', 5)
iterable = iter(c)
for i in range(5):
    print(next(iterable))

    