class Node:
    def __init__(self, value, next = None) -> None:
        self.value = value
        self.next = next

    
class LinkedList:
    def __init__(self, head =None) -> None:
        self.head = head

    def append(self, value):
        if self.head == None:
            self.head=Node(value)
        
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node=current_node.next
            current_node.next=Node(value)

    def display(self):
        current = self.head
        while current is not None:
            print(current.value)
            current=current.next

    def rerverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev=current
            current = next
        self.head=prev



list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(5)
list1.rerverse()
list1.display()
