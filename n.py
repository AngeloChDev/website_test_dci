from abc import ABC , abstractmethod

class A(ABC):
    def __init__(self, n):
        self.n = n

    def __add__(self, o):
        return A(self.n - o.n)
    @abstractmethod
    def nn(self):
        print('mp')
    
class B(A):
    def __init__(self, n):
        super().__init__(n)
b = B(7)

b.nn()

print(b)