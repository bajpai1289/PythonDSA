class Node:
    def __init__(self, value, next=None) -> None:
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
    
    def reverse_iterative(self):
        prev= None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
    # def reverse_recursive(self):
    #     if self.head is None or self.head.next is None:
    #         return self.head
    #     reverse0 = self.head.next
    #     reverse1 = reverse0.self.reverse_recursive()
    #     self.head.next.next =self.head
    #     self.head=None
    #     return reverse1


list1=Linked_list()
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
list1.append(5)
list1.reverse_recursive()
list1.showElements()