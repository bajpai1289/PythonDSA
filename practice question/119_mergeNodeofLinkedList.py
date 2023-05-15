class Node:
    def __init__(self, val) -> None:
        self.val=val
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.length = 0
    
    def append(self, value)->None:
        if self.head is None:
            self.head = Node(value)
            self.length+=1
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next=Node(value)
            self.length+=1
            
    def show(self)->None:
        """Displays the linked list, without trailing EOL charachter"""
        curr = self.head
        while curr is not None:
            print(curr.val, end="=>")
            curr = curr.next
        print() 
        
    def mergeNodes(self):
        curr = self.head
        temp = []
        while curr is not None:
            temp.append(curr.val)
            curr=curr.next
        print(temp)


list1=LinkedList()
list1.append(0)
list1.append(3)
list1.append(1)
list1.append(0)
list1.append(4)
list1.append(5)
list1.append(2)
list1.append(0)
list1.mergeNodes()
list1.show()