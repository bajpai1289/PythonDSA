class Node:
    def __init__(self, value) -> None:
        self.data=value
        self.next = None
    
class LinkedList:
    def __init__(self) -> None:
        self.head=None
    
    def append(self, value):
        if self.head == None:
            self.head=Node(value)
        else:
            currentNode=self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            currentNode.next=Node(value)
    
    def showElements(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next
        
    def length(self):
        result = 0
        current = self.head
        while current is not None:
            result+=1
            current=current.next
        return result
    def sumOfElements(self):
        result = 0
        current = self.head
        while current is not None:
            result+=current.data
            current=current.next
        return result
    
    def getElement(self, position):
        i=0
        current = self.head
        while current is not None:
            if i==position:
                return current.data
            current=current.next
            i+=1
        return None

list1=LinkedList()
list1.append(2)
list1.append(3)
list1.append(5)
list1.append(9)
# print(list1.length())
# print(list1.sumOfElements())
# print(list1.getElement(2))
list1.showElements()

def reverse(l):
    if l.head is None:
        return
    
    current_node = l.head
    prev_node = None
    
    while current_node is not None:
        # Track the next node
        next_node = current_node.next
        
        # Modify the current node
        current_node.next = prev_node
        
        # Update prev and current
        prev_node = current_node
        current_node = next_node
        
    l.head = prev_node 
reverse(list1)
list1.showElements()