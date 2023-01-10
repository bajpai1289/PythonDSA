class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head=None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value)

    def show(self):
        current = self.head
        while current is not None:
            print(current.value, end="=>")
            current = current.next
    def removefromLast(self, index):
        length = 1
        current = self.head
        while current.next is not None:
            current = current.next 
            length+=1
        if index>length-1:
            return
        currIndex = 0
        currHead = self.head
        while currIndex!=length-index:
            currHead=currHead.next
            currIndex+=1
        if currHead.next is None:
            pass

list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
list1.append(5)
list1.show()

list1.removefromLast(2)