import sys
import math

class Stack:
    def __init__(self):
        self.stack = []
        
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()
            
    def push(self,val):
        return self.stack.append(val)
        
    def peak(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]
            
    def size(self):
        return len(self.stack)
        
    def is_empty(self):
        return self.size() == 0
        
class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self,val):
        self.queue.insert(0,val)
        
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop()
            
    def size(self):
        return len(self.queue)
        
    def is_empty(self):
        return self.size() == 0
        
class PriorityQueue(object): 
    def __init__(self): 
        self.queue = [] 
  
    def __str__(self): 
        return ' '.join([str(i) for i in self.queue]) 
  
    def is_empty(self): 
        return len(self.queue) == [] 
  
    def insert(self, data): 
        self.queue.append(data) 
  
    def delete(self): 
        try: 
            max = 0
            for i in range(len(self.queue)): 
                if self.queue[i] > self.queue[max]: 
                    max = i 
            item = self.queue[max] 
            del self.queue[max] 
            return item 
        except IndexError: 
            return None

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    line = input().split()
    order = [(x[0], int(x[1:])) for x in line]
    in_order = [b for a, b in order if a == "i"]
    out_order = [b for a, b in line if a == "o"]
    print(i, file=sys.stderr)
    # test Stack
    validStack = True
    q = Stack()
    for a, val in order:
        if a == "i":
            q.push(val)
        else:
            get = q.pop()
            if val != get:
                validStack = False
                break
    print(validStack, file=sys.stderr)

    validQueue = True
    q = Queue()
    for a, val in order:
        if a == "i":
            q.enqueue(val)
        else:
            get = q.dequeue()
            if val != get:
                validQueue = False
                break
    print(validQueue, file=sys.stderr)
    
    validPrioQueue = True
    q = PriorityQueue()
    for a, val in order:
        if a == "i":
            q.insert(val)
        else:
            get = q.delete()
            if val != get:
                validPrioQueue = False
                break
    print(validPrioQueue, file=sys.stderr)
    
    if sum([validStack, validQueue, validPrioQueue]) > 1:
        print("unsure")
    elif sum([validStack, validQueue, validPrioQueue]) == 0:
        print("mystery")
    elif validStack: 
        print("stack")
    elif validQueue : 
        print("queue")
    else: 
        print("priority queue")
