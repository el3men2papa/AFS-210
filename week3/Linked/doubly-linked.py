class Node:
    # A doubly-linked node.
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    # A doubly-linked list.
    def __init__(self):
        # Create an empty list.
        self.tail = None
        self.head = None
        self.count = 0

    def iter(self):
        # Iterate through the list.
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val
            

    def size(self) -> int:
        # Returns the number of elements in the list
        return self.count

    def addFirst(self, data) -> None:
        # Add a node at the front of the list

        node = Node(data)
        
        if not self.head:
            self.head = node
            self.tail = node # Per Instructor Review
        else:
            node.next = self.head
            self.head.prev = node # Per Instructor Review
            self.head = node
            
        self.count += 1
        
    def addLast(self, data) -> None:
        # Add a node at the end of the list

        node = Node(data)
        
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail # Per Instructor Review
            self.tail = node
            
        self.count += 1
        
    def addAtIndex(self, data, index):
        # Add a node to the list at the given index position
        # If index equals to the length of linked list, the node will be appended to the end of linked list
        # If index is greater than the length, the data will not be inserted.
        # This function does not replace the data at the index, but pushes everything else down.
        
        #need to incorporate back link (Per Instructor Review)
        
        node = Node(data)
        
        if (index > (self.count)):
            return
        if (index == self.count): 
            self.addLast(data)
        else:
            temp = self.head
            for i in range(1, index):
                if(temp != None):
                    temp = temp.next
            if(temp != None):
                node.next = temp.next
                temp.next = node
                
                #temp.prev = node # Per Instructor Review?
                
        self.count += 1
            
    def indexOf(self, data):
        # Search through the list. Return the index position if data is found, otherwise return -1
        #curIndx = -1 # Per Instructor Review
        curIndx = 0
        current_item = self.head
        
        while current_item != None:
            if current_item.data == data:
                return curIndx
            
            curIndx += 1
            current_item = current_item.next
            
        return -1 #curIndx
    
    def add(self, data) -> None:
        # Append an item to the end of the list
        self.addLast(data)
        
    def clear(self) -> None:
        # Remove all of the items from the list
        self.head = None
        self.tail = None
        self.count = 0

    def deleteAtIndex(self, index) -> None:
        # Delete the node at the index-th in the linked list, if the index is valid.
        
        if (index > self.count):
            return
            
        curr = self.head
        prev = self.head

        for n in range(index):
            prev = curr
            curr = curr.next
            
        prev.next = curr.next
        curr.prev = prev
        self.count -= 1

        if (curr == self.head):
            self.head = curr.next
            curr.prev = None
        elif (curr == self.tail):
            prev.next = None
            self.tail = prev
            
        self.count -= 1     

        return

    def delete(self, data) -> None:
        # Delete a node from the list who's value matches the supplied value
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.tail:
                    prev.next = None
                    self.tail = prev
                elif current == self.head:
                    current.next.prev = None
                    self.head = current.next
                else:
                    prev.next = current.next
                    current.next = prev
                self.count -= 1
                return
            prev = current
            current = current.next

    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        current.data = value

    def __str__(self):
        myStr = ""
        for node in self.iter():
             myStr += str(node)+ " "
        return myStr

items = DoublyLinkedList()

items.add('May')
items.add('the')
items.add('Force')
items.add('be')
items.add('with')
items.add('you')
items.add('!')

print(items)

print(items.indexOf('with'))
#It will delete you
items.delete('you')
#is going to add us in the fith possition after deleting you 
items.addAtIndex('us', 5)
#is going to add all in the sixth spot well the seventh starts from 0
items.addAtIndex('all', 6)
#it will print the new list
print(items)