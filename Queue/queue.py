class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.start = None
        self.end = None
    def Enqueue(self,data):
        newnode = Node(data)
        if self.start == None:
            self.start = newnode
            self.end = newnode
        else:
            self.end.next = newnode
            self.end = newnode
    def Dequeue(self):
        if self.start == None:
            return None
        p = self.start.data
        if self.start.next == None:
            self.start = None
            self.end = None
        else:
            self.start = self.start.next
        return p

q = Queue()
q.Enqueue(1)
q.Enqueue(2)
q.Enqueue(3)
print(q.Dequeue())
print(q.Dequeue())
print(q.Dequeue())
print(q.Dequeue())
