class Stack:
    def __init__(self):
        self.items = []
        
    # Adds the element ‘e’ to the top of the stack
    def push(self, e):
        self.items.append(e)
        
    #  Deletes the top most element of the stack
    def pop(self):
        return self.items.pop()

    # Returns the size of the stack
    def size(self): 
        return len(self.items)
        
    # Returns whether the stack is empty
    def isEmpty(self):
        return self.items == []
        
    # Returns a reference to the top most element of the stack value. Does not remove the element.
    def peek(self): 
        return self.items[len(self.items) -1]
        
class Queue:
    def __init__(self):
        self.items = []
        
    # Adds the element 'e' to the queue. 
    def enqueue(self, e):
        self.items.insert(0, e)
    
    # Removes an item from the queue. 
    def dequeue(self):
        return self.items.pop()
        
    # Returns the size of the queue
    def size(self):
        return len(self.items)
        
    # Returns whether the queue is empty
    def isEmpty(self):
        return self.items == []
        
    # Returns a reference to the front item in the queue. Does not remove the element.
    def peek(self):
        return self.items[len(self.items)-1]
    
def isPalindrome(word):
    myStack = Stack()
    
    for elm in word:
        myStack.push(elm)
        
    revWord = ''
    while not myStack.isEmpty():
        revWord += myStack.pop()

    if(word == revWord):
        return True
    
    return False
    
print(isPalindrome('racecar'))
print(isPalindrome('noon'))
print(isPalindrome('python'))
print(isPalindrome('madam'))