class Jar:

    def __init__(self, capacity=12):
        self.capacity = capacity
        self.n = 0


    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if not capacity >= 0:
            raise ValueError
        self._capacity = capacity

    def deposit(self, n):
        if self.n + n > self.capacity:
            raise ValueError
        self.n += n

    def withdraw(self, n):
        if self.n - n < 0:
            raise ValueError
        self.n -= n

    @property
    def size(self): 
        return self.n

    def __str__(self):
        return self.n * "🍪"