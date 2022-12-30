class Node:
    def __init__(self, value, next = None) -> None:
        self.value= value
        self.next=next

class LinkedList:
    def __init__(self) -> None:
        self.head=None
    
    def append(self, value):
        if self.head is None:
            self.head=Node(value)
        else:
            current = self.head
            while current.next is not None:
                current=current.next
            current.next=Node(value)
    def show(self):
        current = self.head
        while current is not None:
            print(current.value, end="=>")
            current=current.next
            
list1=LinkedList()
list1.append(1)
list1.append(1)
list1.append(2)
list1.append(2)
list1.append(2)
list1.append(3)
list1.append(3)
# list1.show()

def removeDuplicates(head=list1.head):
    if head is None or head.next is None:
        return
    while head.next.next is not None:

        print(head.value)
        if head.value==head.next.value:
            head.next=head.next.next
            head=head.next
        else:
            head=head.next
            
removeDuplicates()
list1.show()