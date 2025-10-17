#LINKED LIST
#Singly Linked List
'''class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")

sll = SinglyLinkedList()
sll.insert_at_end(10)
sll.insert_at_end(20)
sll.insert_at_end(30)
sll.display()'''


#Double Linked list
'''class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="<->")
            temp = temp.next
        print("None")

dll = DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_end(40)
dll.display()'''


#Circular singly linkedlist
'''class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        temp = self.head
        while temp.next!=self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next =self.head
    def display(self):
        if not self.head:
            return 
        temp = self.head
        while True:
            print(temp.data,end = "->")
            temp = temp.next
            if temp==self.head:
                break
        print("(Back to Head)")
cll = CircularLinkedList()
cll.insert_at_end(10)
cll.insert_at_end(20)
cll.insert_at_end(30)
cll.display()'''


#Circular Doubly linked list
'''class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        temp = self.head
        while temp.next!=self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next =self.head
        new_node.prev = temp
    def display(self):
        if not self.head:
            return 
        temp = self.head
        while True:
            print(temp.data,end = "<->")
            temp = temp.next
            if temp==self.head:
                break
        print("(Back to Head)")
cdll = CircularDoublyLinkedList()
cdll.insert_at_end(10)
cdll.insert_at_end(20)
cdll.insert_at_end(30)
cdll.display()'''




