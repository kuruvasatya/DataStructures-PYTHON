#implementing stack using linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    def push(self,num):
        newnode = Node(num)
        if self.head == None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode
    def pop(self):
        if self.head == None:
            return None
        p = self.head.data
        self.head = self.head.next
        return p
    def peek(self):
        return self.head.data

stack = Stack()

stack.push(0)
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.peek())
stack.push(15)
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())