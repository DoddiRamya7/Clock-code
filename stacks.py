#STACKS
#basic operations of stack
'''class  stack:
    def __init__(self):
        self.stack = []
    def is_empty(self):
        return len(self.stack) == 0
    def push(self, item):
        self.stack.append(item)
        print(f"pushed {item} to the stack")
    def pop(self):
        if self.is_empty():
            print("stack is empty. cannot pop.")
            return None
        item = self.stack.pop()
        print(f"popped {item} from the stack.")
        return item
    def peek(self):
        if self.is_empty():
            print("stack is empty. cannot peek.")
            return None
        return self.stack[-1]
    def size(self):
        return len(self.stack)
    def display(self):
        if self.is_empty():
            print("stack is empty.")
        else:
            print("stack:,self.stack")

stack = stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
print("top element:", stack.peek())
stack.pop()
stack.pop()
stack.display()
print("stack size:", stack.size())
stack.pop()
stack.pop()
stack.display()'''

#reverse elements using stack
'''def reverse(arr,n):
    st=[]
    for i in range(n):
        st.append(arr[i])
    i=0
    while (len(st)>0):
        top=st.pop() 
        arr[i]=top
        i+=1
    for i in range(n):
        print(arr[i] , end = " ")

n=4
arr=[100,200,300,400] 
reverse(arr,n)'''          


#reverse of stack when input is given by user
'''sdef reverse(arr,n):
    st=[]
    for i in range(n):
        st.append(arr[i])
    i=0
    while (len(st)>0):
        top=st.pop() 
        arr[i]=top
        i+=1
    for i in range(n):
        print(arr[i] , end = " ")

n=int(input())
arr=list(map(int,input().split(",")))
reverse(arr,n)'''
           
'''removing k digits using stack
def removek(nums,k):
    stack = []
    for i in nums:
        while stack and stack[-1]>i and k>0:
            stack.pop()
            k-=1
        stack.append(i)
    if k>0:
        stack = stack[:k]
    result=''.join(stack)
    i=0
    while i<len(result) and result[i] == '0':
        i+=1
    result=result[i:]
    return result if result else '0'
nums=input()
k=int(input())
print(removek(nums,k))'''


'''class stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
        print(f"pushed {item} to the stack")
stack = stack()
stack.push(100)
stack.push(400)
stack.push(1000)
stack.display()'''