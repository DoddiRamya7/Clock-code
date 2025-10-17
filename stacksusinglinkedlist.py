#stacks using linked list
'''class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
    def pop(self):
        if self.is_empty():
            print("Stack underflow!Cannot pop from an empty")
            return None
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data
    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.top.data
    def is_empty(self):
        return self.top is None
    def display(self):
        if self.is_empty():
            print("stack is empty!")
            return
        temp = self.top
        while temp:
            print(temp.data,end =" ")
            temp = temp.next
        print("None")
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
print("Popped:", stack.pop())
print("Top element:", stack.peek())
stack.display()'''



#queue using linkedlist
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class  Queue:
    def __init__(self):
        self.front = None
        self.front=self.rear=None
    def enqueue(self,data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return 
        self.rear.next = new_node
        self.rear = new_node
    def dequeue(self):
        if self.front == None:
            print("queue underflow!Cannot pop from an empty")
            return None
        dequeued_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_data
    def peek(self):
        if self.is_empty():
            print("queue is empty!")
            return None
        return self.front.data
    def is_empty(self):
        return self.front is None
    def display(self):
        if self.is_empty():
            print("queue is empty!")
            return
        temp = self.front
        while temp:
            print(temp.data,end =" ")
            temp = temp.next
        print("None")
queue =Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()
print("Dequeued:", queue.dequeue())
print("Top element:", queue.peek())
queue.display()