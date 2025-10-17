#Queue
#basic operations of queue
'''class Queue:
    def __init__(self):
        self.queue = []
    def is_empty(self):
        return len(self.queue) == 0
    def enqueue(self, item):
        self.queue.append(item)
        print(f"enqueud {item} to the queue.")
    def dequeue(self):
        if self.is_empty():
            print("queue is empty. cannot dequeued.")
            return None
        item = self.queue.pop(0)
        print(f"dequeued {item} from the queue.")
        return item
    def peek(self):
        if self.is_empty():
            print("queue is empty. cannot peek.")
            return None
        return self.queue[0]
    def size(self):
        return len(self.queue)
    def display(self):
        if self.is_empty():
            print("queue is empty.")
        else:
            print("queue:,self.queue")

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()
print("top element:", queue.peek())
queue.dequeue()
queue.dequeue()
queue.display()
print("queue size:", queue.size())
queue.dequeue()
queue.dequeue()
queue.display()'''

#reverse of queue
'''def reverse(arr,n):
    queue=[]
    for i in range(n):
        queue.append(arr[i])
    i=0
    while (len(queue)>0):
        rear=queue.pop() 
        arr[i]=rear
        i+=1
    for i in range(n):
        print(arr[i] , end = " ")

n=4
arr=[100,200,300,400] 
reverse(arr,n)'''

'''priority code
import heapq
priority_queue = []
heapq.heappush(priority_queue, (2, "Task B"))
heapq.heappush(priority_queue, (1, "Task A"))
heapq.heappush(priority_queue, (3, "Task C"))
print("Priority Queue:", priority_queue)
while priority_queue:
    print("Dequeued:", heapq.heappop(priority_queue))'''


#reversing first 5 elements and rewriting remaining elements as same
'''def revn(q,k):
    solve(q,k)
    s=len(q)-k
    for i in range(s):
        x=q.pop(0)
        q.append(x)
    return q
def solve(q,k):
    if k==0:
        return None
    e=q.pop(0)
    solve(q,k-1)
    q.append(e)
queue=list(map(int,input().split()))
k=int(input())
queue=revn(queue,k)

while queue:
    print(queue.pop(0),end=" ")'''


#double ended queue-deque(we can add or remove from both the ends)
'''from collections import deque
def revn(q,k):
    solve(q,k)
    s=len(q)-k
    for i in range(s):
        x=q.popleft()
        q.append(x)
    return q
def solve(q,k):
    if k==0:
        return None
    e=q.popleft()
    solve(q,k-1)
    q.append(e)
queue=deque(list(map(int,input().split())))
k=int(input())
queue=revn(queue,k)

while queue:
    print(queue.popleft(),end=" ")'''


#Circular Queue
'''class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1
    def enqueue(self,data):
        if(self.rear + 1)% self.size ==self.front:
            print("queue is full")
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data
    def dequeue(self):
        if self.front == -1:
            print("queue is empty")
        elif self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1)% self.size
    def display(self):
        if self.front == -1:
            print("queue is empty")
            return 
        i = self.front
        while True:
            print(self.queue[i],end=" ")
            if i == self.rear:
                break
            i = (i+1) % self.size
        print()
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.display()
cq.dequeue()
cq.display()'''


print(1%5)