class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
class Queue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    
    def peekFront(self):
        if self.head is None:
            return None
        
        return self.head.data
    
    def peekBack(self):
        if self.head is None:
            return None

        return self.tail.data

    def enqueue(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    def dequeue(self):
        if self.head is None:
            return None

        temp = self.head
        self.head = self.head.next
        
        return temp.data

q = Queue()
q.enqueue(4)
print(q.peekFront())
print(q.peekBack())
q.enqueue(50)
print(q.peekFront())
print(q.peekBack())
q.enqueue(64)
print(q.peekFront())
print(q.peekBack())
print(q.dequeue())
