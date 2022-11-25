class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next=next

class Linked_list:
    def __init__(self, head=None) -> None:
        self.head=head
        
    def append(self, value):
        if self.head==None:
            self.head=Node(value)
        else:
            current_node=self.head
            while current_node.next is not None:
                current_node=current_node.next
            current_node.next=Node(value)
         
    def showElements(self):
        current_node=self.head
        while current_node is not None:
            print(current_node.value)
            current_node=current_node.next
    
    def reverse_iterative(self, head: Node)->Node:
        prev=None
        current=head
        while current is not None:
            next=current.next
            current.next=prev
            prev=current
            current=next
        return prev
    
    
list1=Linked_list()
list1.append(1)
# list1.append(2)
# list1.append(3)
# list1.append(4)
# list1.append(5)
list1.showElements()